#include <Arduino_FreeRTOS.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <FreeRTOS.h>
#include <task.h>

#define sensorPin D2
String lastVisitorID = "";
int visitor;
int visitorDetected;

const char* ssid = "IoT";
const char* password = "AccessPoint.2024";
const char* host = "http://192.168.248.196";

LiquidCrystal_I2C lcd(0x27, 16, 2);

void taskSensor(void *pvParameters) {
  for (;;) {
    visitorDetected = digitalRead(sensorPin);
    if (visitorDetected == HIGH) {
      visitor++;
      newVisit();
      vTaskDelay(200 / portTICK_PERIOD_MS);
    }
  }
}

void taskVisualFeedback(void *pvParameters) {
  for (;;) {
    Serial.print("Visitor #: ");
    Serial.println(visitor);

    lcd.clear();
    lcd.setCursor(0, 0); 
    lcd.print("Visitor #: ");
    lcd.setCursor(11, 0); 
    lcd.print(visitor);

    vTaskDelay(200 / portTICK_PERIOD_MS);
  }
}

void setup() {
  Serial.begin(9600);
  wifiConfig();
  initCount();

  lcd.init();
  lcd.backlight();

  xTaskCreate(taskSensor, "Sensor", 1000, NULL, 1, NULL);
  xTaskCreate(taskVisualFeedback, "VisualFeedback", 1000, NULL, 1, NULL);
}

void loop() {
  // Not used in FreeRTOS
}

void newVisit() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    WiFiClient wifi;
    String server_newVisit = String(host) + "/laser-visitor-counter-IoT-NodeMCU-RFID/queries/new_visitor.php?vID=" + String(visitor);
    http.begin(wifi, server_newVisit); 
    http.addHeader("Content-Type", "text/plain");
    int httpCode = http.GET();
    if (httpCode > 0) {
      String response = http.getString();
    } else {
      Serial.println("HTTP Error: " + http.errorToString(httpCode));
    }
    http.end();
  } else {
    Serial.println("Error in WiFi connection");
  }
}

void wifiConfig() {
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());  
}

void initCount() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    WiFiClient wifi;
    String server_fetch = String(host) + "/laser-visitor-counter-IoT-NodeMCU-RFID/queries/count_visitor.php";
    http.begin(wifi, server_fetch); 
    int httpCode = http.GET();
    if (httpCode > 0) {
      String response = http.getString();
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, response);
      const char* visitor_id = doc["visitor_id"];
      visitor = atoi(visitor_id);
    } else {
      Serial.println("HTTP Error: " + http.errorToString(httpCode));
    }
    http.end();
  } else {
    Serial.println("Error in WiFi connection");
  }
}

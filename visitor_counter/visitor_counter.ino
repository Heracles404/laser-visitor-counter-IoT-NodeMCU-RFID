// Internet Components
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "IoT";
const char* password = "09071132324";
const char* host = "192.168.248.196";


#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

#define sensorPin D4

int visitor = 0;
int visitorDetected;

void setup() {
  Serial.begin(9600);

  wifiConfig();   // WiFi Configuration / SetUp
  initCount():    // Fetch latest visitor count from DB

  // Program starts here
  lcd.init();
  lcd.backlight();

  pinMode(sensorPin, INPUT);
}

void loop() {
    visitorDetected = digitalRead(sensorPin);

    // Insert here
    // get value from state table
    // while state value fetch is zero, get value from state table

    if (visitorDetected == HIGH) {
      visitor++;
      Serial.print("Visitor #: ");
      Serial.println(visitor);

      lcd.setCursor(0, 0); 
      lcd.print("Visitor #: ");
      lcd.setCursor(11, 0); 
      lcd.print(visitor);

      while(visitorDetected == HIGH){
        visitorDetected = digitalRead(sensorPin);
      }
      newVisit();
    }

    delay(200);
}

void newVisit(){
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    WiFiClient wifi;
    http.begin(wifi, "http://192.168.248.196/visitor_counter/new_visitor.php"); 
    http.addHeader("Content-Type", "text/plain");
    int httpCode = http.GET();
    if (httpCode > 0) {
      String response = http.getString();
      Serial.println(response);
    } else {
      Serial.println("HTTP Error: " + http.errorToString(httpCode));
    }
    http.end();
  } else {
    Serial.println("Error in WiFi connection");
  }
  return;
}

void wifiConfig(){
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);  // Start the Wi-Fi connection

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());  
}

void initCount(){

}
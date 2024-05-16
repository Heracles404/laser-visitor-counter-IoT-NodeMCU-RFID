#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

// WiFi credentials
const char* ssid = "uan";
const char* password = "123456789";

// Server address
const char* serverName = "http://192.168.111.226/get_visitor_ids.php"; // Change this to your actual server address

String lastVisitorID = "";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to ");
  Serial.println(ssid);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void fetchLatestVisitorID() {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client; // Create a WiFiClient object
    HTTPClient http;
    http.begin(client, serverName); // Use WiFiClient with the HTTPClient

    int httpCode = http.GET();

    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println("HTTP Response code: " + String(httpCode));

      // Parse JSON payload
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);
      String newVisitorID = doc["visitor_id"].as<String>();

      // Check if the new visitor ID is different from the last displayed ID
      if (newVisitorID != lastVisitorID && !newVisitorID.isEmpty()) {
        Serial.println("New Visitor ID: " + newVisitorID);
        lastVisitorID = newVisitorID; // Update the last displayed ID
      } else if (!lastVisitorID.isEmpty()) {
        Serial.println("Last Visitor ID: " + lastVisitorID);
      }
    } else {
      Serial.println("Error on HTTP request");
    }

    http.end();
  } else {
    Serial.println("WiFi not connected");
  }
}

void loop() {
  fetchLatestVisitorID(); // Fetch and display the latest visitor ID
  delay(2000); // Check for new data every 5 seconds
}

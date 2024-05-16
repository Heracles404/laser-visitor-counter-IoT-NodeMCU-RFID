// Internet Components
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "IoT";
const char* password = "09071132324";
const char* host = "192.168.248.196";

#define laserPin D5

int incomingByte;

void setup() {
  Serial.begin(9600);

  wifiConfig();   // WiFi Configuration / SetUp

  pinMode(laserPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
    incomingByte = Serial.read();

    if (incomingByte == '1'){
      digitalWrite(laserPin, HIGH);
    }
    else if (incomingByte == '2'){
      digitalWrite(laserPin, LOW);
    }
  }
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

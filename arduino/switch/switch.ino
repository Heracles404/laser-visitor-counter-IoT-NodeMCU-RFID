#define powerPin 2

int swtch;

void setup() {
  Serial.begin(9600);
  
  pinMode(powerPin, OUTPUT);
  digitalWrite(powerPin, LOW);
}

void loop() {
  if (Serial.available() > 0){
    swtch = Serial.read();

    if (swtch == 'N'){
      digitalWrite (powerPin, HIGH);
    }

    if (swtch == 'F'){
      digitalWrite(powerPin, LOW);
    }
  }

  delay(500);
}

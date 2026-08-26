void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(50, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');


    if (comando == "LED_ON") {
      digitalWrite(50, HIGH);
      Serial.println("LED encendido");
    }
    else if(comando == "LED_OFF") {
      digitalWrite(50, LOW);
      Serial.println("LED apagado");
    }
  }
}
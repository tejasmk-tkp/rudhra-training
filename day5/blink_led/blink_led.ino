const int led = 13;
int ledState = LOW;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, ledState);
  Serial.println("Press 1");
}
void loop() {
  if (Serial.available()) {
    int key_press = Serial.parseInt();

    if (key_press == 1 && ledState == LOW) {
      ledState = HIGH;
    }

    else if (key_press == 1 && ledState == HIGH) {
      ledState = LOW;
    }
    digitalWrite(led, ledState);
  }
}

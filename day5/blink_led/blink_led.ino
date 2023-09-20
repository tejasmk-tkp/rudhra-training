const int led = 13;
int ledState = LOW;
int key_press = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, ledState);
  Serial.println("Press 1 to turn on LED and 0 to turn off");
}
void command() {
  if (Serial.available() == 0) {

    key_press = Serial.parseInt();

    switch (key_press) {
      case 0:
        ledState = LOW;
        break;
      case 1:
        ledState = HIGH;
        break;
      default:
        Serial.println("Enter only 1 or 0");
        break;
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
    command();
    digitalWrite(led, ledState);
}


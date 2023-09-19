const int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
  Serial.println("Press 1 to turn on LED and 0 to turn off");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() == 0) {

    int key_press = Serial.parseInt();

    if (key_press == 1) {
        digitalWrite(led, HIGH);
        key_press = Serial.parseInt();
        if (key_press == 0) {
          digitalWrite(led, LOW);
          key_press = Serial.parseInt();
          if (key_press == 1) {
            digitalWrite(led, HIGH);
            break;
          }
        }
      }
    }
  }


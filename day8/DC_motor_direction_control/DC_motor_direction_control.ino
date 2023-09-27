const int IN1 = 6;
const int IN2 = 7;
const int ENA = 5;
const int POT = A0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(POT, INPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Direction 1
  if (Serial.available()) {

    int key = Serial.parseInt();
    int PWM = analogRead(POT);
    PWM = map(PWM, 403, 1023, 0, 255);
    
    if (key == 1) {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(ENA, PWM);
    }
  
    if (key == 2) {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, PWM);
    }

    if (key == 0) {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, PWM);
    }
  }
}
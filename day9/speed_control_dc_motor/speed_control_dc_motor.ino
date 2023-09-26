const int IN1 = 6;
const int IN2 = 7;
const int PWM = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(PWM, 255);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Direction 1
  if (Serial.available()) {

    int key = Serial.read();
    int PWM_val = Serial.parseInt();

    if (key == '1') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(PWM, PWM_val);
    }
  
    if (key == '2') {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(PWM, PWM_val);
    }

    if (key == '0') {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(PWM, PWM_val);
    }
  }
}
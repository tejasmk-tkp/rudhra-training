const int IN1 = 6;
const int IN2 = 7;
const int PWM = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(PWM, OUTPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {

    int PWM_val = Serial.read();
    Serial.println(PWM_val); 

    if (PWM_val > 0) {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(PWM, PWM_val);
    }

    if (PWM_val < 0) {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(PWM, PWM_val);
    }

    if (PWM_val == 0) {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(PWM, PWM_val);
    }
  }
}
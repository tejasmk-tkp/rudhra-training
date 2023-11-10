const int IN1 = 4;
const int IN2 = 5;
const int PWM = 6;

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

    byte PWM_val = Serial.read();
    Serial.println(PWM_val);
    
    int PWM_val_R = map(PWM_val, 1, 128, 255, 0);
    int PWM_val_L = map(PWM_val, 129, 255, 0, 255);

    if (PWM_val > 0 && PWM_val < 129) {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(PWM, PWM_val_R);
    }

    if (PWM_val > 128 && PWM_val < 256) {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(PWM, PWM_val_L);
    }

    if (PWM_val == 0) {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(PWM, PWM_val);
    }
  }
}
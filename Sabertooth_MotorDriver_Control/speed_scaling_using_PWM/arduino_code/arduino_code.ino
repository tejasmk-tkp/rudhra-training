const int PWM1 = 3;
const int PWM2 = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PWM1, OUTPUT);
  pinMode(PWM2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    byte PWM_val = Serial.read();
    Serial.println(PWM_val); 
    PWM_val = map(PWM_val, 0, 100, 0, 255);
    analogWrite(PWM1, PWM_val);
    analogWrite(PWM2, PWM_val);
  }
}
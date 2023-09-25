const int IN1 = 4;
const int IN2 = 5;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Direction 1
  //if (Serial.available()) {
    //Serial.println("A");
    
    //int key = Serial.parseInt();
    //Serial.println(key);
      //if (key == 0) {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
      //}
      delay(5000);
      //if (key == 1) {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      //}
  //}
}

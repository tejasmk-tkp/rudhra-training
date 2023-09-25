int led = 9;
int pot = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(pot, INPUT);
  digitalWrite(led, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val = analogRead(pot);
  val = map(val, 403, 1023, 255, 0);
  analogWrite(led, val);
}

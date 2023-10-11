#include <math.h>

const int trig = 4;
const int echo = 5;
const int led = 13;

double v, d, t;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig, LOW);
  delayMicroseconds(5);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  t = pulseIn(echo, HIGH); //in microsecond
  //Serial.println(t);
  v = 343; //in m/s
  d = (v * pow(10, -2))  * (((t * pow(10, 6)))/2); //distance in cm

  if (d < 10) {
    Serial.println("Too Close!!");
    digitalWrite(led, HIGH);
  }

  if (d >= 10 && d < 20) {
    Serial.println("Getting Close!!");
    digitalWrite(led, HIGH);
    delay(1000);
    digitalWrite(led, LOW);
    delay(1000);
  }

  if (d >= 20) {
    Serial.println("NVM");
    digitalWrite(led, LOW);
  }
}
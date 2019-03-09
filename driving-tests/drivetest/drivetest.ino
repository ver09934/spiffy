#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

int leftPower;
int rightPower;

byte myBuffer[2] = {0, 0};

void setup() {

  leftMotor.attach(5);
  rightMotor.attach(6);

  leftMotor.write(0);
  rightMotor.write(0);

  Serial.begin(9600);
}

void loop() {

  while (Serial.available() > 0) {
    int inByte = Serial.read();
    myBuffer[0] = myBuffer[1];
    myBuffer[1] = inByte;
  }

  leftPower = map(myBuffer[0], 0, 0xff, 0, 180);
  rightPower = map(myBuffer[1], 0, 0xff, 0, 180);

  leftMotor.write(leftPower);
  rightMotor.write(rightPower);
  
  // Serial.println(myBuffer[0] + " " + myBuffer[1]);
  // delay(500);
  delay(10);
}


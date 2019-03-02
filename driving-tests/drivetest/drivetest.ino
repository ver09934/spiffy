#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

byte myBuffer[2] = {0, 0};

void setup() {

  leftMotor.attach(5);
  rightMotor.attach(6);

  leftMotor.write(0);
  rightMotor.write(0);

  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {

    Serial.readBytesUntil(0xff, myBuffer, 1000);

    leftPower = map(myBuffer[0], 0, 0xff, 0, 180);
    rightPower = map(myBuffer[1], 0, 0xff, 0, 180);

    leftMotor.write(leftPower);
    rightMotor.write(rightPower);

  }
  delay(10);
}


#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

void setup() {

  leftMotor.attach(5);
  rightMotor.attach(6);

  writeBoth(0);

  delay(3000);

  writeBoth(90);

  delay(3000);

}

void loop() {
  writeBoth(180);
  delay(1000);
}

void writeBoth(int val) {
  leftMotor.write(val);
  rightMotor.write(val);
}


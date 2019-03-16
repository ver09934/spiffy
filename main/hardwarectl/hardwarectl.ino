#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

int leftPower;
int rightPower;

// The Pi will always send four bytes whenever it wants to update any values

#define BUFFER_LENGTH 4
byte serialBuffer[BUFFER_LENGTH] = {0x80, 0x80, 0x00, 0x00}; // Neutral values

void setup() {

    Serial.begin(9600);

    leftMotor.attach(5);
    rightMotor.attach(6);

    leftMotor.writeMicroseconds(1050);
    rightMotor.writeMicroseconds(1050);

    delay(3000);

    leftMotor.writeMicroseconds(1500);
    rightMotor.writeMicroseconds(1500);

    delay(1000);
}

void loop() {

    while (Serial.available() > 0) {
        int inByte = Serial.read();
        for (int i = 0; i < BUFFER_LENGTH - 1; i++) {
            serialBuffer[i] = serialBuffer[i + 1];
        }
        serialBuffer[BUFFER_LENGTH - 1] = inByte;
    }

    leftPower = map(serialBuffer[0], 0, 0xff, 0, 180);
    rightPower = map(serialBuffer[1], 0, 0xff, 0, 180);

    // TODO: Get values
    // stepperPosition = map(serialBuffer[2], 0, 0xff, 0, MAX);

    leftMotor.write(leftPower);
    rightMotor.write(rightPower);

    delay(10);
}

int getBytes(byte val) {
    int out[8];
    for (int i = 0; i < 8; i++) {
        out[8 - i - 1] = val & 1;
       	val = val >> 1;
    }
    return out;
}

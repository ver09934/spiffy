#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

// The Pi will always send four bytes whenever it wants to update any values

byte serialBuffer[4] = {0x80, 0x80, 0x00, 0x00}; // Neutral values

void setup() {

    leftMotor.attach(5);
    rightMotor.attach(6);

    leftMotor.write(0);
    rightMotor.write(0);

    Serial.begin(9600);

    // TODO: ESC initialization procedure - potentially methodize...
    // TODO: Stepper motor setup
}

void loop() {

    while (Serial.available() > 0) {
        int inByte = Serial.read();
        for (int i = 0; i < serialBuffer.length - 1; i++) {
            serialBuffer[i] = serialBuffer[i + 1];
        }
        serialBuffer[serialBuffer.length] = inByte;
    }

    leftPower = map(serialBuffer[0], 0, 0xff, 0, 180);
    rightPower = map(serialBuffer[1], 0, 0xff, 0, 180);

    // TODO: Get values
    // stepperPosition = map(serialBuffer[2], 0, 0xff, 0, MAX);

    leftMotor.write(leftPower);
    rightMotor.write(rightPower);

    delay(10);
}

int[] getBytes(byte val) {
    int[] out = [8];
    for (int i = 0; i < 8; i++) {
        out[8 - i - 1] = val & 1;
       	x = x >> 1
    }
}


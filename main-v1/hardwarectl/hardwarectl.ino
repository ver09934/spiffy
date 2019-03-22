#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

int leftPower;
int rightPower;

// Min 0, Max 28,000
int stepperCount = 0; // Current position
int stepperPosition = 0; // Desired position

int relayByte[8] = {1, 1, 0, 0, 0, 0, 0, 0};

#define BUFFER_LENGTH 4
byte byteIdVals[BUFFER_LENGTH] = {0b00000000, 0b01000000, 0b10000000, 0b11000000};
byte serialBuffer[BUFFER_LENGTH] = {0b00000000, 0b01000000, 0b10000000, 0b11000000};

void setup() {

    // Stepper pins
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);

    // Relay pins
    pinMode(11, OUTPUT);
    pinMode(12, OUTPUT);
    digitalWrite(11, HIGH);
    digitalWrite(12, HIGH);

    Serial.begin(9600);

    leftMotor.attach(5);
    rightMotor.attach(6);

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

    for (int i = 0; i < BUFFER_LENGTH; i++) {
        
        int val = serialBuffer[i];
        
        int bits[8];
        for (int i = 0; i < 8; i++) {
            bits[8 - i - 1] = val & 1;
            val = val >> 1;
        }

        // TODO: See if mapped vals need to be converted to int (add 0.5 and cast to int to round)
        if (bits[0] == 0 && bits[1] == 0) {
            leftPower = map(serialBuffer[i] - byteIdVals[i], 0, 0xff, 90, 180);
        }
        else if (bits[0] == 0 && bits[1] == 1) {
            rightPower = map(serialBuffer[i] - byteIdVals[i], 0, 0xff, 90, 180);
        }
        else if (bits[0] == 1 && bits[1] == 0) {
            stepperPosition = map(serialBuffer[i] - byteIdVals[i], 0, 0xff, 0, 28000);
        }
        else if (bits[0] == 1 && bits[1] == 1) {
            for (int i = 0; i < 8; i++) {
                relayByte[i] = bits[i];
            }
        }
    }

    leftMotor.write(leftPower);
    rightMotor.write(rightPower);

    if (relayByte[7] == 1) {
        digitalWrite(11, LOW);
    }
    else {
        digitalWrite(11, HIGH);
    }

    if (relayByte[6] == 1) {
        digitalWrite(12, LOW);
    }
    else {
        digitalWrite(12, HIGH);
    }

    if ((stepperCount < stepperPosition) && (stepperCount + 1 <= 28000)) {
        stepUp();
    }
    else if ((stepperCount > stepperPosition) && (stepperCount - 1 >= 0)) {
        stepDown();
    }
    else {
        delay(10);
    }
}

void stepUp() {
    digitalWrite(9, LOW);
    digitalWrite(8, HIGH);
    delayMicroseconds(250);          
    digitalWrite(8, LOW); 
    delayMicroseconds(250);  
    stepperCount += 1; 
}

void stepDown() {
    digitalWrite(9, HIGH);
    digitalWrite(8, HIGH);
    delayMicroseconds(250);          
    digitalWrite(8, LOW); 
    delayMicroseconds(250);
    stepperCount -= 1;
}


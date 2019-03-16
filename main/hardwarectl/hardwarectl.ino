#include <Servo.h>

Servo leftMotor;
Servo rightMotor;

int leftPower;
int rightPower;

// Min 0, Max 28,000
int stepperCount = 0; // Current position
int stepperPosition = 0; // Desired position

#define BUFFER_LENGTH 4
byte serialBuffer[BUFFER_LENGTH] = {0x80, 0x80, 0x00, 0x00}; // Neutral values

void setup() {

    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    // digitalWrite(9, LOW);

    Serial.begin(9600);

    leftMotor.attach(5);
    rightMotor.attach(6);

    /*
    leftMotor.writeMicroseconds(1050);
    rightMotor.writeMicroseconds(1050);

    delay(3000);
    */

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

    // TODO: See if these need to be converted to int (add 0.5 and cast to int to round)
    leftPower = map(serialBuffer[0], 0, 0xff, 0, 180);
    rightPower = map(serialBuffer[1], 0, 0xff, 0, 180);
    stepperPosition = map(serialBuffer[2], 0, 0xff, 0, 28000);

    leftMotor.write(leftPower);
    rightMotor.write(rightPower);

    if ((stepperCount < stepperPosition) && (stepperCount + 1 <= 28000)) {
        stepUp();
    }
    else if ((stepperCount > stepperPosition) && (stepperCount - 1 >= 0) {
        stepDown();
    }

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

/*
digitalWrite(9, LOW);
for (int i = 0; i <= 28000; i++) {
    digitalWrite(8, HIGH);
    delayMicroseconds(250);          
    digitalWrite(8, LOW); 
    delayMicroseconds(250);        
}  
delay(3000);

digitalWrite(9, HIGH);
for (int i = 0; i <= 28000; i++) {
    digitalWrite(8, HIGH);
    delayMicroseconds(250);          
    digitalWrite(8, LOW); 
    delayMicroseconds(250);        
}  
delay(3000);
*/

import serial
import numpy as np

class SerialWriter:
    
    def __init__(self):

        try:
            self.ser = serial.Serial('/dev/ttyACM0', 9600)
            print("Using /dev/ttyACM0")
        except:
            self.ser = serial.Serial('/dev/ttyACM1', 9600)
            print("Fell back to /dev/ttyACM1")
        
        self.byteArr = np.array([0b00000000, 0b01000000, 0b10000000, 0b11000000])

    # --- Setting the values ---

    def setLeftPowerMapped(self, power):
        self.byteArr[0] = 0b00000000 + int(map(power, 0, 1, 0b00000000, 0b00111111))
    
    def setRightPowerMapped(self, power):
        self.byteArr[1] = 0b01000000 + int(map(power, 0, 1, 0b00000000, 0b00111111))

    def setStepperPositionMapped(self, position):
        self.byteArr[2] = 0b10000000 + int(map(position, 0, 1, 0b00000000, 0b00111111))

    def setBit(self, position, bit):
        if bit == 1:
            self.byteArr[3] = self.byteArr[3] | (1 << (position - 1))
        else:
            self.byteArr[3] = self.byteArr[3] & ~(1 << (position - 1))

    # --- Sending values over serial ---

    def writeAllBytes(self):
        for val in self.byteArr:
            self.ser.write(bytes([val]))

    # --- Util Methods ---

    # Convert numpy array of bits (ex. np.array([1, 1, 1, 1, 1, 1, 1, 0])) to int
    @staticmethod
    def encodeToByte(bitArray):
        out = 0
        for i in range(0, bitArray.size):
            out = out | bitArray[i]
            if i < bitArray.size - 1:
                out = out << 1
        return out

def map(val, minIn, maxIn, minOut, maxOut):
    spanIn = maxIn - minIn
    spanOut = maxOut - minOut
    val = float(val - minIn) / float(spanIn)
    val = minOut + (val * spanOut)
    return val

def clamp(val, minVal, maxVal):
    return min(max(val, minVal), maxVal)

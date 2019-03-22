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
        
        self.byteArr = np.array([0x80, 0x80, 0x00, 0])
        # self.byteArr = [0xff, 0xff, 0, 0]
        # self.byteArr = np.array([0.5, 0.5, 0, 0])

    # --- Setting the values, raw ---

    def setLeftPower(self, power):
        self.byteArr[0] = power
        # self.byteArr[0] = int(map(power, 0, 1, 0x00, 0xff))
    
    def setRightPower(self, power):
        self.byteArr[1] = power
        # self.byteArr[1] = int(map(power, 0, 1, 0x00, 0xff))

    def setStepperPosition(self, position):
        self.byteArr[2] = position
        # self.byteArr[2] = int(map(position, 0, 1, 0x00, 0xff))

    def setBit(self, position, bit):
        if bit == 1:
            self.byteArr[3] = self.byteArr[3] | (1 << (position - 1))
        else:
            self.byteArr[3] = self.byteArr[3] & ~(1 << (position - 1))

    # --- Setting the values, mapped ---

    def setLeftPowerMapped(self, power):
        self.byteArr[0] = int(map(power, 0, 1, 0x80, 0xff))
    
    def setRightPowerMapped(self, power):
        self.byteArr[1] = int(map(power, 0, 1, 0x80, 0xff))

    def setStepperPositionMapped(self, position):
        self.byteArr[2] = int(map(position, 0, 1, 0x00, 0xff))

    # --- Sending values over serial ---

    def writeAllBytes(self):
        for val in self.byteArr:
            self.ser.write(bytes([val]))
        # self.ser.write(bytes(self.byteArr))

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

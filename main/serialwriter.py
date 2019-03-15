import serial
import numpy as np

class SerialWriter:

    # Declare class vars for initial values (neutral for motors, off for etc.)
        # Just declare the byteArr up here instead...
    # Keep in mind that reversing is NOT WORKING on one of the ESCs

    # TODO: Should motor powers be sclaed between 0.5 and 1, if a second ESC with functioning reversing is obtained?
    # (0,0.5,1 --> backward,stop,forward)
    # Or, should power be sclaed from 0,1 --> stop,forward
    
    def __init__(self):
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600)
            print("Using /dec/ttyACM0")
        except:
            ser = serial.Serial('/dev/ttyACM1', 9600)
            print("Fell back to /dec/ttyACM1")
        byteArr = np.array([0, 0, 0, 0]) # TODO: Better intial values

    # --- Sending values over serial ---

    def writeByte(val):
        ser.write(bytes([val]))

    def writeAllBytes():
        # Encode the values


        # Send the values
        for byte in byteArr:
            writeByte(byte)

    # --- Setting the values ---

    def setLeftPower():
        pass # TODO
    def setRightPower():
        pass # TODO

    # Takes a numpy array of bits
    # Example: vals = np.array([1, 1, 1, 1, 1, 1, 1, 0])
    def encodeToByte(bitArray):
        out = 0
        for i in range(0, bitArray.size):
            out = out | bitArray[i]
            if i < bitArray.size - 1:
                out = out << 1
        return out

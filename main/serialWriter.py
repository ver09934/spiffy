import serial
import numpy as np

class serialWriter:
    
    def __init__(self):

        try:
            ser = serial.Serial('/dev/ttyACM0', 9600)
            print("Using /dec/ttyACM0")
        except:
            ser = serial.Serial('/dev/ttyACM1', 9600)
            print("Fell back to /dec/ttyACM1")

        byteArr = np.array([0, 0, 0, 0])

    def writeByte(val):
        ser.write(bytes([val]))

    def writeAllBytes():
        for byte in byteArr:
            writeByte(byte)
    
    def setLeftMotor(val):
        byteArr[0] = val

    def setRightMotor(val):
        byteArr[1] = val

    def setStepperMotor(val):
        byteArr[2] = val

    # TODO: Make methods to set the individual bits
    def setDevByte(val):
        byteArr[3] = val


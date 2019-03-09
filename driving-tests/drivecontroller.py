import serial

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print("USING /dec/ttyACM0")
except:
    ser = serial.Serial('/dev/ttyACM1', 9600)
    print("FELL BACK TO /dec/ttyACM1")

def writeByte(val):
    ser.write(bytes([val]))
    
# https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3

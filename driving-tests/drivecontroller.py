import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def writeByte(val):
    ser.write(bytes([val]))
    
# https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
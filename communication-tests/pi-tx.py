import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)

str = bytes("a", 'utf-8')

while True:
    ser.write(str)
    time.sleep(5)

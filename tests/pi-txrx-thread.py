import serial
import threading
import time

def main():

    ser = serial.Serial('/dev/ttyACM0',9600)

    threading.Thread(target=txThread, args=(ser,)).start()
    threading.Thread(target=rxThread, args=(ser,)).start()

def txThread(serialIn):
    while True:
        str = bytes("Hello from Raspberry Pi!", 'utf-8')
        serialIn.write(str)
        time.sleep(1)

def rxThread(serialIn):
    while True:
        read_serial = serialIn.readline()
        print(read_serial)

if __name__ == '__main__':
    main()

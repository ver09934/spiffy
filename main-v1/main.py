import serialwriter
import time
import threading

# TODO: This is inevitably going to need threading... so much fun!
# TODO: Should probably try to document this process for the engineering notebook...

def main():
    serialWriter = serialwriter.SerialWriter()
    time.sleep(3)
    print("Delay over")
    # driveTest(serialWriter)
    # stepperTest(serialWriter)
    # relayTest(serialWriter)
    demo(serialWriter)

def driveTest(writer):
    # writer.setLeftPower(1)
    # writer.setRightPower(1)
    writer.setLeftPower(0xff)
    writer.setRightPower(0xff)
    writer.writeAllBytes()
    time.sleep(3)
    # writer.setLeftPower(0.5)
    # writer.setRightPower(0.5)
    writer.setLeftPower(0x80)
    writer.setRightPower(0x80)
    writer.writeAllBytes()

def stepperTest(writer):
    writer.setStepperPosition(0xff)
    writer.writeAllBytes()
    time.sleep(21)
    writer.setStepperPosition(0x00)
    writer.writeAllBytes()

def relayTest(writer):
    # position, bit
    # relay 1
    writer.setBit(1, 1)
    writer.writeAllBytes()
    time.sleep(1)
    writer.setBit(1, 0)
    writer.writeAllBytes()
    # relay 2
    writer.setBit(2, 1)
    writer.writeAllBytes()
    time.sleep(1)
    writer.setBit(2, 0)
    writer.writeAllBytes()

def demo(writer):
    turnTime = 3

    writer.setLeftPower(0x00)
    writer.setRightPower(0xff)
    writer.setStepperPosition(0xff)
    writer.writeAllBytes()
    time.sleep(turnTime)
    
    writer.setLeftPower(0x80)
    writer.setRightPower(0x80)
    writer.writeAllBytes()
    time.sleep(21 - turnTime)

    time.sleep(0.5)
    writer.setBit(1, 1)
    writer.writeAllBytes()
    time.sleep(1)
    writer.setBit(1, 0)
    writer.writeAllBytes()
    time.sleep(0.5)
    
    writer.setStepperPosition(0x00)
    writer.writeAllBytes()
    time.sleep(21)

'''
def demo(writer):
    threading.Thread(target=demo1, args=(writer,)).start()
    threading.Thread(target=demo1, args=(writer,)).start()

def demo1():
    pass

def demo2():
    pass
'''

if __name__ == "__main__":
    main()


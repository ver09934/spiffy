import serialwriter
import time

# TODO: This is inevitably going to need threading... so much fun!
# TODO: Should probably try to document this process for the engineering notebook...

def main():
    serialWriter = serialwriter.SerialWriter()
    time.sleep(3)
    print("Delay over")
    serialWriter.connect()
    time.sleep(3)
    # driveTest(serialWriter)
    # stepperTest(serialWriter)
    relayTest(serialWriter)

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


if __name__ == "__main__":
    main()


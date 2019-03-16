import serialwriter
import time

# TODO: This is inevitably going to need threading... so much fun!
# TODO: Should probably try to document this process for the engineering notebook...

def main():
    serialWriter = serialwriter.SerialWriter()
    time.sleep(3)
    print("Delay over")
    # driveTest(serialWriter)
    stepperTest(serialWriter)

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
    time.sleep(15)
    writer.setStepperPosition(0x00)
    writer.writeAllBytes()

if __name__ == "__main__":
    main()


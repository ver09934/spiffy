import serialwriter
import time

# TODO: This is inevitably going to need threading... so much fun!
# TODO: Should probably try to document this process for the engineering notebook...

def main():
    serialWriter = SerialWriter()
    driveTest(serialWriter)

def driveTest(writer):
    writer.setLeftPower(1)
    writer.setRightPower(1)
    writer.writeAllBytes()
    time.sleep(3)
    writer.setLeftPower(0.5)
    writer.setRightPower(0.5)
    writer.writeAllBytes()

def lightTest(serialWriter):
    pass

if __name__ == "__main__":
    main()


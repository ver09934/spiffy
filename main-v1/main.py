import serialwriter
import time

relay1 = False

def main():
    
    writer = serialwriter.SerialWriter()
    time.sleep(3)

    turnTime = 6

    writer.setLeftPowerMapped(0)
    writer.setRightPowerMapped(0.4)
    writer.setStepperPositionMapped(1)
    writer.writeAllBytes()
    time.sleep(turnTime)
    
    writer.setLeftPowerMapped(0)
    writer.setRightPowerMapped(0)
    writer.writeAllBytes()
    time.sleep(21 - turnTime)

    time.sleep(0.5)
    writer.setBit(2, 1)
    writer.writeAllBytes()
    time.sleep(1)
    writer.setBit(2, 0)
    writer.writeAllBytes()
    time.sleep(0.5)

    if relay1:
        writer.setBit(1, 1)
        writer.writeAllBytes()
        time.sleep(1)
        writer.setBit(1, 0)
        writer.writeAllBytes()
        time.sleep(0.5)
    
    writer.setStepperPositionMapped(0)
    writer.writeAllBytes()
    time.sleep(21)

if __name__ == "__main__":
    main()


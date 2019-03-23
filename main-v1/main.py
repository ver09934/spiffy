import serialwriter
import time

def main():
    
    writer = serialwriter.SerialWriter()
    time.sleep(3)

    turnTime = 3

    writer.setLeftPowerMapped(0)
    writer.setRightPowerMapped(1)
    writer.setStepperPositionMapped(1)
    writer.writeAllBytes()
    time.sleep(turnTime)
    
    writer.setLeftPowerMapped(0)
    writer.setRightPowerMapped(0)
    writer.writeAllBytes()
    time.sleep(21 - turnTime)

    time.sleep(0.5)
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


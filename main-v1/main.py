import serialwriter
import time

relay1 = False

def main():
    
    writer = serialwriter.SerialWriter()
    time.sleep(3)

    turnTime = 2.5

    writer.setLeftPowerMapped(0)
    writer.setRightPowerMapped(0.3)
    writer.setStepperPositionMapped(1)
    writer.writeAllBytes()
    time.sleep(turnTime)

    slideTime = 23
    
    writer.setLeftPowerMapped(0)
    writer.setRightPowerMapped(0)
    writer.writeAllBytes()
    time.sleep(slideTime - turnTime)

    lightTime = 3

    time.sleep(0.5)
    writer.setBit(2, 1)
    writer.writeAllBytes()
    time.sleep(lightTime)
    writer.setBit(2, 0)
    writer.writeAllBytes()
    time.sleep(0.5)

    pumpTime = 2

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


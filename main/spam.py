import serialwriter
import time

writer = serialwriter.SerialWriter()
time.sleep(3)

while True:
    writer.writeAllBytes()
    time.sleep(0.5)

'''
writer.setLeftPower(0x80)
writer.setRightPower(0x80)
writer.setStepperPosition(0x00)
writer.setBit(1, 0)
writer.setBit(2, 0)
'''

import serialwriter
import time

writer = serialwriter.SerialWriter()
time.sleep(3)

while True:
    # writer.setLeftPowerMapped(0.4)
    # writer.setRightPowerMapped(0.4)
    writer.writeAllBytes()
    time.sleep(0.1)

'''
writer.setLeftPowerMapped(0)
writer.setRightPowerMapped(0)
writer.setStepperPositionMapped(0)
writer.setBit(1, 0)
writer.setBit(2, 0)
'''


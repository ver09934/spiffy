import serialwriter
import time

writer = serialwriter.SerialWriter()
time.sleep(3)
writer.writeAllBytes()

'''
writer.setLeftPowerMapped(0)
writer.setRightPowerMapped(0)
writer.setStepperPositionMapped(0)
writer.setBit(1, 0)
writer.setBit(2, 0)
'''


import serialwriter
import time

writer = serialwriter.SerialWriter()
time.sleep(3)

while True:
    writer.writeAllBytes()
    time.sleep(0.1)

'''
writer.setLeftPower(0)
writer.setRightPower(0)
writer.setStepperPosition(0)
writer.setBit(1, 0)
writer.setBit(2, 0)
'''


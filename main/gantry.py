import serialwriter
import time

serialWriter = serialwriter.SerialWriter()
time.sleep(3.5)

serialWriter.setLeftPowerMapped(0)
serialWriter.setRightPowerMapped(0)
serialWriter.writeAllBytes()
time.sleep(0.5)

serialWriter.setStepperPositionMapped(1)
serialWriter.writeAllBytes()
time.sleep(24)

serialWriter.setBit(2, 1)
serialWriter.writeAllBytes()
time.sleep(5)
serialWriter.setBit(2, 0)
serialWriter.writeAllBytes()
time.sleep(0.5)

serialWriter.setStepperPositionMapped(0)
serialWriter.writeAllBytes()
time.sleep(24)

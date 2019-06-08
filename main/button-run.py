import time
import RPi.GPIO as GPIO
from subprocess import Popen

button_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_lock = False

p = None

while True:
    if GPIO.input(button_pin) and not button_lock:
        button_lock = True

        # Popen(['python3', 'cv-main-robot.py']).wait()

        if p is None: # Never started
            p = Popen(['python3', 'cv-main-robot.py'])
        else:
            if p.poll() is None: # Running
                p.terminate()
            else: # Not running
                p = Popen(['python3', 'cv-main-robot.py'])

    else:
        button_lock = False        
    time.sleep(0.005)

GPIO.cleanup()  

import time
import RPi.GPIO as GPIO

button_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

running = False

button_lock = False

while True:
    if GPIO.input(button_pin) and not button_lock:
        button_lock = True

        # TODO: Actually start and stop the other script
        if not running:
            pass
        else:
            pass

    else:
        button_lock = False        
    time.sleep(0.005)

GPIO.cleanup()  

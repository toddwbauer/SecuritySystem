import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 8
GPIO.setup(PIR_PIN, GPIO.IN)

try:
        print ("PIR Module Test (CTRL+C to exit)")
        time.sleep(.01)
        print ("Ready")
        while True:
                if GPIO.input(PIR_PIN):
	                print ("Motion Detected!")
	                time.sleep(1)
			pirstate='on'
except KeyboardInterrupt:
        print  ("Quit")
        GPIO.cleanup()


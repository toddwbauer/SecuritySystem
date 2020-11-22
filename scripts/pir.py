import RPi.GPIO as GPIO

class Pir:
    
    # On creation, set the PIR pin to input mode.
    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)

    # When motion is detected, return true; otherwise, return false.
    def detect_motion(self):
        if GPIO.input(self.pin):
            self.motion_detected = True
            return True
        else:
            self.motion_detected = False
            return False
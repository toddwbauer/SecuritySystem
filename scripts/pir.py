import RPi.GPIO as GPIO

# The Pir class is a very simple class that controls a PIR sensor. The
# class is instantiated with a pin number which it uses to identify the
# pin the PIR sensor is connected to on the GPIO. A program can then use
# the detect_motion function to read the sensor for input, returning true
# if motion is found and false if not.
#
# Authors: Todd Bauer, Gerardo Ortiz
# November 28, 2020

class Pir:
    
    # On creation, set the PIR pin to input mode.
    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)

    # Detects motion at the moment it is called. When motion is detected,
    # return true; otherwise, return false.
    #
    # Input: void
    # Output: boolean representing if motion is detected.
    def detect_motion(self):
        if GPIO.input(self.pin):
            self.motion_detected = True
            return True
        else:
            self.motion_detected = False
            return False
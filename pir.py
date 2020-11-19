import RPi.GPIO as GPIO
from datetime import datetime
import cv2

class Pir:
    motion_flag = False

    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)

    def pic_on_motion(self, frame):
        if GPIO.input(self.pin):
            if not self.motion_flag:
                cv2.imwrite("snapshot/{}.jpg".format(datetime.now().strftime("%m-%d-%Y--%H:%M:%S")), frame)
                cv2.imwrite("snapshot/latest.jpg", frame)
                print("Motion detected. Picture taken!")
            self.motion_flag = True
        else:
            if self.motion_flag:
                print("Motion stopped.")
            self.motion_flag = False
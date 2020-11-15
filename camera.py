from picamera import PiCamera
from time import sleep
import base64
# output file for image capture from picamera
output = "/home/pi/Downloads/intruder.jpeg"

#heading for b64_string
formatString = "data:image/jpeg;base64,{}"

#picamera 
camera = PiCamaera()
#capture image and write to output
camera.capture(output,format = "jpeg",)


# Function that converts jpeg to DataURL base64 string
# returns formatString + b64_string
def encodeFunction():
    with open(output, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
 
    return(formatString.format(b64_string.decode('utf-8')))

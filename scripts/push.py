from pushsafer import init, Client
import urllib3
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import http.client, urllib
import base64
import cv2

# The PushToPhone class is responsible for contacting the Pushsafer service,
# which pushes a notification to both iOS and Android devices. This allows
# a program to send a notification to a phone device with a picture attachment,
# which is encoded as a base64 string.
#
# Authors: Todd Bauer, Gerardo Ortiz
# November 28, 2020

class PushToPhone:
    
    def __init__(self, key):
        urllib3.disable_warnings()
        
        self.key = key
        self.formatString = "data:image/jpeg;base64,{}"
        init(key)
        
    # Passes info to pushsafer & sends notification to phone
    def sendNot(self, pic):
        url = "https://www.pushsafer.com/api"
        post_fields = {
            "t" : "Alert",                           # Message title
            "m" : "Motion detected pic for details", # Message text
            "s" : "0",                               # Sound number 0-28
            "v" : "1",                               # Vibration number 0-3
            "i" : "1",                               # Icon number 1-98
            "c" : "",                                # Icon color
            "d" : "29780",                           # Device number
            "u" : "https://www.pushsafer.com",       # URL
            "ut" : "Open Pushsafer",                 # URL title
            "k" : self.key,                          # Your private key
            "p" : pic                                # Base64-encoded string
        }
        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()
        print("Push notification sent to registered device.")

    # Encode an image as a base64 string, as this is the format that Pushsafer
    # recognizes when sending images to phones via notification.
    #
    # Input: A frame captured from a webcam using the OpenCV library.
    # Output: The input frame as a base64 string.
    def encodeImage(self, pic):
        retval, buffer = cv2.imencode('.jpg', pic)
        b64_string = base64.b64encode(buffer)

        return(self.formatString.format(b64_string.decode('utf-8')))

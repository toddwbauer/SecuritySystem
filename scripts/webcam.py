from imutils.video import VideoStream
import datetime
import imutils
import cv2

# The WebcamController class acts as a controller for a USB webcam. It uses
# OpenCV, combined with an extension package called imutils which makes
# image processing easier and more flexible.
#
# It creates a VideoStream when initialized, which is then used to capture
# frames from the webcam. It does this each time generate_frame is called,
# and stores the frame in the "frame" class variable. This frame can be used
# for a wide variety of image- and video-related tasks.
#
# To use this class, instantiate a WebcamController object, then run the
# generate_frame function in a loop to perpetually generate the most recent
# frame.
#
# Authors: Todd Bauer, Gerardo Ortiz
# November 28, 2020

class WebcamController:
    frame = None # The last generated frame.
    
    # On creation, set the IP and port number, then start reading camera input.
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.vs = VideoStream(src=0).start()
        
    # Grabs the current camera frame and puts a timestamp on it, then stores
    # it in the class variable "frame".
    #
    # Input: void
    # Output: void
    def generate_frame(self):
        frame = self.vs.read()
        timestamp = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(frame, timestamp, (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, .75, (255, 0, 0), 1)
        self.frame = frame
    
    # Encodes the current frame as a .jpg file for purposes of saving a frame
    # as a permanent file.
    #
    # Input: void
    # Output: flag, a boolean that is true when encoding was successful.
    #         encodedImage, the image resulting from a successful operation.
    def encode_as_jpg(self):
        (flag, encodedImage) = cv2.imencode(".jpg", self.frame)
        return flag, encodedImage
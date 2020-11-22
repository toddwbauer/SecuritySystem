from imutils.video import VideoStream
import datetime
import imutils
import cv2

class WebcamController:
    frame = None # The last generated frame.
    
    # On creation, set the IP and port number, then start reading camera input.
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.vs = VideoStream(src=0).start()
        
    # Grabs the current camera frame and puts a timestamp on it.
    def generate_frame(self):
        frame = self.vs.read()
        timestamp = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(frame, timestamp, (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, .75, (255, 0, 0), 1)
        self.frame = frame
    
    # Encodes the current frame to a .jpg file.
    def to_jpg(self):
        (flag, encodedImage) = cv2.imencode(".jpg", self.frame)
        return flag, encodedImage
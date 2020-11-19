from imutils.video import VideoStream
from flask import Flask, render_template, Response
from pir import Pir
import threading
import datetime
import imutils
import cv2

PIR_PIN = 8
motion_flag = False
outputFrame = None
lock = threading.Lock()

app = Flask(__name__)

vs = VideoStream(src=0).start()
pir = Pir(PIR_PIN)


@app.route("/")
def index():
    return render_template("index.html")

def generate():
    global vs, outputFrame, lock, motion_flag
    
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=630)
        
        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, .75, (255, 0, 0), 1)
        with lock:
            outputFrame = frame.copy()
        with lock:
            pir.pic_on_motion(outputFrame)
        
def stream():
    global outputFrame, lock
    
    while True:
        with lock:
            if outputFrame is None:
                continue
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            if not flag:
                continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encodedImage) + b'\r\n')
    
@app.route("/video_feed")
def video_feed():
    return Response(stream(),
        mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':    
    t = threading.Thread(target=generate)
    t.daemon = True
    t.start()
    
    app.run(host="192.168.0.108", port=8081, debug=True,
            threaded=True, use_reloader=False)
    
vs.stop()
    
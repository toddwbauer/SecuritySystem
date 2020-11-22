import json
import cv2
import datetime

class DataLogger:
    video_recording = False
    video_log_enabled = False
    motion_log_enabled = False
    
    # On creation, set the path to the settings file,
    # then store the settings from that file.
    def __init__(self, path):
        self.path = path
        self.refresh_settings()
            
    def refresh_settings(self):
        try:
            with open(self.path) as file:
                data = json.load(file)
                if data["videolog"]["enabled"] == "on":
                    self.video_log_enabled = True
                else:
                    self.video_log_enabled = False
                    
                if data["motionlog"]["enabled"] == "on":
                    self.motion_log_enabled = True
                else:
                    self.motion_log_enabled = False
                    
                self.video_path = data["videolog"]["path"]
                self.motion_path = data["motionlog"]["path"]
        
        # The file could not be found or loaded.
        except OSError as e:
            print("Error: Could not load " + file.name
                  + ". Videos and motion will not be saved.\n"
                  + "Please verify that settings.txt exists "
                  + "in the software's root directory. If it "
                  + "does not, create this file as an empty "
                  + "text file, then set desired settings in "
                  + "the General Settings web page.\n"
                  + "Error message:", e)
            
        # The file was found and read but not decoded by JSON.
        except ValueError as e:
            print("JSON Decode error. This can occur when changing "
                  + "settings during program operation and is non-fatal "
                  + "unless perpetually recurring.")
        
    # Saves an image to a file.
    def motion_to_file(self, image):
        filename = "/{}.jpg".format(datetime.datetime.now()
                        .strftime("%m-%d-%Y--%H:%M:%S"))
        cv2.imwrite(self.motion_path + filename, image)
        cv2.imwrite(self.motion_path + "/latest.jpg", image)
        print("Image saved to", self.motion_path + filename)
        
    # Initializes the recording of a video by setting the codec and filename.
    def start_recording(self):
        self.fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        self.videoWriter = cv2.VideoWriter(self.video_path + "/{}.avi"
                                          .format(datetime.datetime.now()
                                          .strftime("%m-%d-%Y--%H:%M:%S")),
                                      self.fourcc, 30.0, (640,480))
        self.video_recording = True
        
    # Stops the current recording.
    def stop_recording(self):
        if self.video_recording is True:
            self.videoWriter.release()
            self.video_recording = False
    
    # Provided the video is recording, write a frame to that video.
    def video_to_file(self, frame):
        if self.video_recording is True:
            self.videoWriter.write(frame)
    
    # TO-DO
    def activity_to_file(self):
        return False
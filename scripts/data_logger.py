import json
import cv2
import datetime

# The DataLogger class exists to manage data in the Security System program.
# It serves two primary and essential functions: it manages the settings that
# the user chooses from settings.php, and using these settings, decides which
# data logging functions to perform.
#
# Video recording is a complicated process due to the way OpenCV works. First,
# a video file must be set, and then frames must be continually added to this
# file. start_recording sets the filename, and video_to_file writes the frame.
# The former function must be called once to set up the video, and the latter
# must be called in a loop to write frames continuously.
#
# Authors: Todd Bauer, Gerardo Ortiz
# November 28, 2020

class DataLogger:
    video_recording = False    # Flag to mark video as currently recording.
    video_log_enabled = False  # Marks whether video recording is enabled
    motion_log_enabled = False # Marks whether motion logging is enabled
    # video_path marks the path to save video if recording is enabled
    # motion_path marks the path to save motion if motion is enabled
    
    # On creation, set the path to the settings file,
    # then store the settings from that file.
    #
    # Input: path - the path of the settings file.
    # Output: void
    def __init__(self, path):
        self.path = path
        self.refresh_settings()
            
    # Loads the settings file and reads settings.
    #
    # Input: void
    # Output: void
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
    #
    # Input: A frame from the webcam.
    # Output: The input frame, converted to an image, saved on the hard disk.
    def motion_to_file(self, image):
        filename = "/{}.jpg".format(datetime.datetime.now()
                        .strftime("%m-%d-%Y--%H:%M:%S"))
        cv2.imwrite(self.motion_path + filename, image)
        cv2.imwrite(self.motion_path + "/latest.jpg", image)
        print("Image saved to", self.motion_path + filename)
        
    # Initializes the recording of a video by setting the codec and filename.
    # Sets video_recording to true to tell video_to_file that it can write
    # video when it is called.
    #
    # Input: void
    # Output: void
    def start_recording(self):
        self.fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        self.videoWriter = cv2.VideoWriter(self.video_path + "/{}.avi"
                                          .format(datetime.datetime.now()
                                          .strftime("%m-%d-%Y--%H:%M:%S")),
                                      self.fourcc, 30.0, (640,480))
        self.video_recording = True
        
    # Stops the current recording.
    #
    # Input: void
    # Output: void
    def stop_recording(self):
        if self.video_recording is True:
            self.videoWriter.release()
            self.video_recording = False
    
    # Provided the video is recording, write a frame to that video.
    #
    # Input: A frame from the webcam.
    # Output: The input frame, inserted into a recording as the specified path.
    def video_to_file(self, frame):
        if self.video_recording is True:
            self.videoWriter.write(frame)
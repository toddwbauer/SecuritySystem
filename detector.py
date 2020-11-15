from gpiozero import MotionSensor
import push
import camera
pir = MotionSensor(14)

#starting up sensor
pir.wait_for_no_motion()
print("Sensor Online")
#forever loop to keep PIR sensor online.
while True:
    
    pir.wait_for_motion()
    print("Motion Detected")
    #push.sendNot(camera.encodeFunction())
    pir.wait_for_no_motion()
    print("No Motion")
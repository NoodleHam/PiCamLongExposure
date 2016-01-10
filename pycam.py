import time
import picamera
import fractions
import os

def capture(prefix, suffix, exposure_max, numOfFrames):
    numOfFrames += 1 #the first frame is wasted
    cam = picamera.PiCamera()
    cam.resolution = (1920, 1080)

    #auto exposure time, up to 1/exp_time s
    cam.framerate = fractions.Fraction(exposure_max, 1)

    cam.start_preview()
    time.sleep(0.7)
    
    for i in range(0, numOfFrames):
        cam.capture(prefix + str(i) + suffix)

    #remove the first frame since it's usually bad
    os.remove(prefix + "0" + suffix)
    cam.close()

prefx = "picam_"
sufx = ".jpg"
exp_max = 12 #exposure time, x/1 sec
num = 10

capture(prefx, sufx, exp_max, num)



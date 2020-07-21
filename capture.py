from grovepi import *
import time, os

port = 3
pinMode(port, "INPUT")

def onClick():
    os.system("raspistill -t 1 -o image.jpg")
    os.system("pkill gpicview")
    os.system("gpicview image.jpg &")
    print("image saved")

pressed = False
begin_time = None
while 1:
    if digitalRead(port):
        pressed = True
        if begin_time is None:
            begin_time = time.time()

    elif pressed:
        pressed = False 
        if time.time() - begin_time < 1:
            onClick()
        begin_time = None

    time.sleep(0.05)

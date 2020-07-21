from grovepi import *
import time

port = 3

pinMode(port, "INPUT")

pressed = False
n = 0
while 1:
    if digitalRead(port):
        pressed = True
        print("{}: button pressed".format(n))

    elif pressed:
        pressed = False 
        print("{}: button released".format(n))

    n += 1
    time.sleep(0.02)

from grovepi import *
import time

port = 3

pinMode(port, "INPUT")

n = 0
while 1:
    if digitalRead(port):
        print("{}: button pressed".format(n))
        n += 1
    time.sleep(0.02)

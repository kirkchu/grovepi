from grovepi import *
import time

port = 8

pinMode(port, "OUTPUT")

try:
    while 1:
        digitalWrite(port, 1)
        time.sleep(1)
        digitalWrite(port, 0)
        time.sleep(1)
except:
    digitalWrite(port, 0)

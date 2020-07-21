import grovepi
import time

port = 2

grovepi.pinMode(2, "INPUT")

while 1:
    value = grovepi.analogRead(port)
    print(value)
    time.sleep(0.5)

import grovepi
import time, math

port = 4
dht11 = 0
dht22 = 1
 
while True:
    (t, h) = grovepi.dht(port, dht11)  
    if not(math.isnan(t) and math.isnan(h)):
        print("temp={}C humidity={}%".format(t, h))
    time.sleep(5)

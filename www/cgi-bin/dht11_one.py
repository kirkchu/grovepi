#!/usr/bin/python3
import grovepi
import time, json, math

port = 4
dht11 = 0
 
while 1:
    (t, h) = grovepi.dht(port, dht11)  
    if not(math.isnan(t) and math.isnan(h)):
        value = {"temperature": t, "humidity": h}
        print("content-type: text/json\n")
        print(json.dumps(value))
        break
    time.sleep(5)
    

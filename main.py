import grovepi
import grove_rgb_lcd as lcd
import time, math

port = 4
dht11 = 0
dht22 = 1
 
lcd.setRGB(0, 128, 64)
while True:
    (t, h) = grovepi.dht(port, dht11)  
    if not(math.isnan(t) and math.isnan(h)):
        lcd.setText('T:{}, H:{}'.format(t, h))
        print("temp={}C humidity={}%".format(t, h))
    time.sleep(5)

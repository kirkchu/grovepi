from grove_rgb_lcd import *
import time

setText("Hello World\nHi Everyone")
setRGB(0, 128, 64)

for c in range(0, 255):
    setRGB(255 - c, c, 0)
    time.sleep(0.01)

setText("")
setRGB(0, 0, 0)

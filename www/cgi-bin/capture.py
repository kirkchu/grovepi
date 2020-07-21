#!/usr/bin/python3

import os

os.system("raspistill -t 1 -dt -o image.jpg")

print("content-type:text/html")
print("")

print("image.jpg")

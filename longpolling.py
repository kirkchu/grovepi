import urllib.request as urllib
import time, json

url = "http://humpback.local:8000/cgi-bin/dht11_one.py"

while 1:
    response = urllib.urlopen(url)
    value = json.load(response)
    print("溫度: {temperature}, 濕度: {humidity}".format(**value))
    time.sleep(10)


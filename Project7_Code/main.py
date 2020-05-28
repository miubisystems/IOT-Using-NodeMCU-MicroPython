from machine import Pin
import network
import urequests
from dht import DHT11
from MQ135 import MQ135
import time
import ujson
THRESHOLD = 15
data2send = {
            "type": "note",
            "title": "WARNING : Gas Leakage",
            "body": "",
            }

API_KEY = 'o.OA64hJxGGNDVeUxwmxlehGm4na8wsfys'

pb_headers = {
'Access-Token': API_KEY,
'Content-Type': 'application/json',
'Host': 'api.pushbullet.com'
}

def notify(ppmlevel):
    data2send["body"] = "Gas Level : " + str(ppmlevel)
    r = urequests.post('https://api.pushbullet.com/v2/pushes',data=ujson.dumps(data2send),headers=pb_headers)
    global flag
    time.sleep(5)
    flag = 0

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('AccessPoint', '9652721286')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def main():
    mq135 = MQ135(0)  # analog PIN 0
    dht11 = DHT11(Pin(2))  #
    do_connect()
    while True:
        dht11.measure()
        temperature = dht11.temperature()
        humidity = dht11.humidity()
        corrected_ppm = mq135.get_corrected_ppm( temperature, humidity)
        if ( corrected_ppm > THRESHOLD):
            notify(corrected_ppm)
        print("Corrected Resistance :",corrected_ppm)

if __name__ == '__main__':
    main()
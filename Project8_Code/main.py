from machine import Pin
import network
import urequests
from dht import DHT11
import time
import ujson
data2send = {
            "value1": "",
            "value2": "",
            }

API_KEY = 'kAmC64uwDj5duxVjEMOw-qSB2wDIoQevrXe5x7zoovo'

pb_headers = {
'Content-Type': 'application/json',
}

def notify(temperature, humidity):
    data2send["value1"] = str(temperature)
    data2send["value2"] = str(humidity)
    r = urequests.post('https://maker.ifttt.com/trigger/dht11/with/key/'+ API_KEY,
                       data=ujson.dumps(data2send),headers=pb_headers)
    time.sleep(5)
    flag = 0

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Access Point', 'Password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def main():
    dht11 = DHT11(Pin(4))
    do_connect()
    while True:
        dht11.measure()
        temperature = dht11.temperature()
        humidity = dht11.humidity()
        print('temperature : ',temperature, 'humidity :', humidity)
        notify(temperature,humidity)

if __name__ == '__main__':
    main()
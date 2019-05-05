from machine import Pin
import network
from umqtt.robust import MQTTClient
import sys
import os

# the following function is the callback which is
# called when subscribed data is received
# dshyam91/feeds/gpio2
def call_back_routine(feed, msg):
    print('Received Data:  feed = {}, Msg = {}'.format(feed, msg))
    if ADAFRUIT_IO_FEEDNAME1 in feed:
        action = str(msg, 'utf-8')
        if action == 'ON':
            pin16.value(0)
        else:
            pin16.value(1)
        print('action = {} '.format(action))
    if ADAFRUIT_IO_FEEDNAME2 in feed :
        action = str(msg, 'utf-8')
        if action == 'ON':
            pin2.value(0)
        else:
            pin2.value(1)
        print('action = {} '.format(action))

ADAFRUIT_IO_URL = b'io.adafruit.com'
ADAFRUIT_USERNAME = b'dshyam91'
ADAFRUIT_IO_KEY = b'0df3c623101b4dc48de1d66d82d1d66d'
ADAFRUIT_IO_FEEDNAME1 = b'gpio16'
ADAFRUIT_IO_FEEDNAME2 = b'gpio2'
# create a random MQTT clientID
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')


client = MQTTClient(client_id=mqtt_client_id,
                    server=ADAFRUIT_IO_URL,
                    user=ADAFRUIT_USERNAME,
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)



def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('shyam', '9652721286')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    try:
        client.connect()
    except Exception as e:
        print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
        sys.exit()


pin16 = Pin(16, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin2.value(1)
pin16.value(1)
def main():
    do_connect()
    # ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME1
    mqtt_feedname1 = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME1), 'utf-8')
    mqtt_feedname2 = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME2), 'utf-8')
    client.set_callback(call_back_routine)
    client.subscribe(mqtt_feedname1)
    client.subscribe(mqtt_feedname2)
    while True:
        try:
            client.wait_msg()
        except KeyboardInterrupt:
            print('Ctrl-C pressed...exiting')
            client.disconnect()
            sys.exit()

if __name__ == '__main__':
    main()
from machine import Pin
import network
import time
from umqtt.robust import MQTTClient
import sys
import dht
import os

ADAFRUIT_IO_URL = b'io.adafruit.com'
ADAFRUIT_USERNAME = b'dshyam91'
ADAFRUIT_IO_KEY = b'0df3c623101b4dc48de1d66d82d1d66d'
ADAFRUIT_IO_FEEDNAME1 = b'temperature'
ADAFRUIT_IO_FEEDNAME2 = b'humidity'
ADAFRUIT_IO_FEEDNAME3 = b'vibration'
MESUREMENT_INTERVAL = 7

# create a random MQTT clientID
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')


client = MQTTClient(client_id=mqtt_client_id,
                    server=ADAFRUIT_IO_URL,
                    user=ADAFRUIT_USERNAME,
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)

#ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME1
mqtt_feedname1 = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME1), 'utf-8')
mqtt_feedname2 = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME2), 'utf-8')
mqtt_feedname3 = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME3), 'utf-8')



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


def Send_Data(tVstat,tTemp,tHumid) :
    client.publish(mqtt_feedname1,bytes(str(tTemp), 'utf-8'), qos=0)
    client.publish(mqtt_feedname2,bytes(str(tHumid), 'utf-8'),qos=0)
    client.publish(mqtt_feedname3,bytes(str(tVstat), 'utf-8'),qos=0)

def main():
    do_connect()
    p5 = Pin(5, Pin.IN) # Vibration Data
    d = dht.DHT11(Pin(4)) # Temp and Humidity
    last_mesurement_time = 0
    Vstat =0
    while True:
        if p5.value() == 1:
            Vstat += 1
        current_time = time.time()
        d.measure()
        temp = d.temperature()  # eg. 23 (°C)
        humid = d.humidity()  # eg. 41 (% RH)

        if current_time - last_mesurement_time > MESUREMENT_INTERVAL:
            print('Temperature:',temp,'Humidity',humid,'Vib Stat',Vstat)
            Send_Data(Vstat,temp,humid)
            last_mesurement_time = current_time
            Vstat = 0


if __name__ == '__main__':
    main()
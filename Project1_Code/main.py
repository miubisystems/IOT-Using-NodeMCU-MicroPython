import network
import socket
import ussl
import time
import dht
from machine import Pin

API_KEY = "3PUNCXS9S3GOW2BF"
HOST = "api.thingspeak.com"
MESUREMENT_INTERVAL = 5

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('shyam', '9652721286')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def Send_Data(tVstat,tTemp,tHumid) :
    data = "api_key=" + API_KEY + "&field1=" + str(tTemp)+ "&field2=" + str(tHumid) +"&field3=" + str(tVstat)
    s = socket.socket()
    ai = socket.getaddrinfo(HOST, 443)
    addr = ai[0][-1]
    s.connect(addr)
    s = ussl.wrap_socket(s)

    s.write("POST /update HTTP/1.0\r\n")
    s.write("Host: " + HOST + "\r\n")
    s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
    s.write(data)
    print(s.read(10)) #Response packet
    s.close()
    # time.sleep(1)


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
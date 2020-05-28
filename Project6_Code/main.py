#import network and socket libraries to connect with AP and receive data
import network
import socket
import urequests
import utime
#This library must be downloaded from
#https://github.com/mcauser/micropython-pcd8544/blob/master/pcd8544_fb.py
import pcd8544_fb
from machine import Pin, SPI
# Hardware Map of Connections between Nokia Display(PCD8544) and NodeMCU
# Read on SPI at : https://docs.micropython.org/en/latest/esp8266/quickref.html#hardware-spi-bus
# InCode|	ESP	|	Disp|	Name|	Description
#-------|-------|-------|-------|----------------
# 15	|	D0	|	1	|	RST	|	External reset input, active low
# 5		|	D1	|	2	|	CE	|	Chip enable, active low
# 4		|	D2	|	3	|	D/C	|	Data high / Command low
# Lib	|	D7	|	4	|	DIN	|	Serial data input
# Lib	|	D5	|	5	|	CLK	|	Serial clock, up to 4 Mbits/s
# 		|	3.3V|	6	|	VCC	|	Supply voltage 2.7-3.3V
# 		|	GND	|	7	|	BL	|	Backlight
# 		|	GND	|	8	|	GND	|	Ground

spi = SPI(1) # Create SPI Device Object, Use 1 Only, 0 is reserved for other purposes
spi.init(baudrate=2000000, polarity=0, phase=0) #20Mhz Speed, POL and PHA being default 0, 0
# Create Pin Objects
ce = Pin(5) #Chip Enable
dc = Pin(4) # Data High / Command low
rst = Pin(16)# Reset Pin
#Create LCD Object with hardware pinout information
lcd = pcd8544_fb.PCD8544_FB(spi, ce, dc, rst)


def connect_to_ap():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('Shyam', '9652721286')
        while not wlan.isconnected():
            pass
    print('network config', wlan.ifconfig())

def print_climate_data(data):
    for i in range(6):
        lcd.fill(0)
        place = data["title"]
        #Get Todays Data First
        weather = data["consolidated_weather"][i]
        date_today = weather["applicable_date"]
        weather_today = weather["weather_state_name"]
        temperature = weather["the_temp"]
        Humidity = weather["humidity"]
        #print Today Data
        lcd.text(place, 0, 0, 1)
        lcd.text(date_today, 0, 8, 1)
        lcd.text(str(temperature), 0, 16, 1)
        lcd.text("dC", 52, 16, 1)
        lcd.text("Humid:", 0, 24, 1)
        lcd.text(str(Humidity), 52, 24, 1)
        lcd.text(weather_today, 0, 32, 1)
        lcd.show()
        utime.sleep(1)
def main():
    connect_to_ap()
    response = urequests.get("https://www.metaweather.com/api/location/2383660/")
    data = response.json()
    while True:
        print_climate_data(data)

if __name__ == '__main__':
    main()
#import network and socket libraries to connect with AP and receive data
import network
import socket
#For Parsing Json data and Getting response from URLs
import urequests

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
        place = data["title"]
        #Get Todays Data First
        weather = data["consolidated_weather"][i]
        date_today = weather["applicable_date"]
        weather_today = weather["weather_state_name"]
        temperature = weather["the_temp"]
        Humidity = weather["humidity"]
        #print
        print("Place:",place)
        print("Date :", date_today)
        print("Weather :",weather_today )
        print("Temperature :",temperature )
        print("Humidity :", Humidity)

def main():
    connect_to_ap()
    response = urequests.get("https://www.metaweather.com/api/location/2383660/")
    data = response.json()
    print_climate_data(data)

if __name__ == '__main__':
    main()
import network
import urequests
import time
import ujson

data2send = {
            "type": "note",
            "title": "Msg From NodeMCU",
            "body": "",
            }
API_KEY = 'o.RqA4kXld3nW9f2smlj2RFTxOfOQhIl9z'

pb_headers = {
'Access-Token': API_KEY,
'Content-Type': 'application/json',
'Host': 'api.pushbullet.com'
}

def notify(custom_msg):
    data2send["body"] = custom_msg
    r = urequests.post('https://api.pushbullet.com/v2/pushes', 
						data=ujson.dumps(data2send), headers=pb_headers)
    time.sleep(5)

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
    do_connect()
    #while True:
    notify("Dummy Notification")

if __name__ == '__main__':
    main()
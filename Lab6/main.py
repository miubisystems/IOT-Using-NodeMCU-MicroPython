import network
import socket

def connect_to_ap():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('dummy','956856')
        while not wlan.isconnected():
            pass
    print('network config',wlan.cofig())

def watch_starwars():
    addr_info = socket.getaddrinfo("towel.blinkenlights.ln",23)
    addr = add_info[0][-1]
    s = socket.socket()
    s.connect(addr)
    while True:
        data = s.recv(500)
        print(str(data,'utf8'),end='')

def main():
    connect_to_ap()
    watch_starwars()


if __name__ == '__main__':
    main()
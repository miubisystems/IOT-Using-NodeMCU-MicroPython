import machine

status_pin = machine.Pin(4,machine.Pin.IN)
print('Vibration Sensing')
while True :
    if(status_pin.value() == True):
        print('Vibration')

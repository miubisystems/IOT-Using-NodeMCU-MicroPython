import machine
import utime

pin1 = machine.Pin(16, machine.Pin.OUT)
pin2 = machine.Pin(2, machine.Pin.OUT)

while True:
    pin1.value(0)
    pin2.value(1)
    utime.sleep_ms(500)
    pin1.value(1)
    pin2.value(0)
    utime.sleep_ms(500)



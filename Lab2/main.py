import machine
import time
import math
def pulse(l, t):
    for i in range(20):
        print('dutycycle :',int(math.sin(i / 10 * math.pi) * 500 + 500), ( i / 10 * math.pi),math.sin(i / 10 * math.pi))
        l.duty(int(math.sin(i/10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

def main():
    ledR = machine.PWM(machine.Pin(0))
    ledG = machine.PWM(machine.Pin(4))
    ledB = machine.PWM(machine.Pin(5))
    for i in range(10):
        pulse(ledR, 500)
        pulse(ledG, 500)
        pulse(ledB, 500)


if __name__ == '__main__':
    main()


import machine

def main():
    while True:
        adc = machine.ADC(0)
        print(adc.read())


if __name__ == '__main__':
    main()

import time
from machine import I2C, Pin
from vl6180 import Sensor
import ssd1306

i2c_lidar = I2C(sda=Pin(4), scl=Pin(5))
i2c_display = I2C(-1, Pin(5), Pin(4))
lidar = Sensor(i2c_lidar)
display = ssd1306.SSD1306_I2C(128, 64, i2c_display)
display.fill(0)
prev = lidar.range()
while True:
    display.fill(0)
    display.text("Range-Milli Mts : ", 0, 0)
    display.text(str(lidar.range()), 0, 10)
    display.text("Gesture : ", 0, 20)
    cur = lidar.range()
    if prev > cur:
        if prev is 255:
            display.text("Glitch", 21, 40)
        else:
            display.text("Approaching", 21, 40)
    elif prev < cur:
        display.text("Moving Away", 21, 40)
    elif cur is 255:
        display.text("No Gesture", 21, 40)

    prev = cur
    display.show()

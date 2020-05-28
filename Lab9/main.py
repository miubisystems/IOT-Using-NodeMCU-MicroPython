# For Math Functions like sin and cos
import math
import utime
#This library must be downloaded from
#https://github.com/mcauser/micropython-pcd8544/blob/master/pcd8544_fb.py
import pcd8544_fb
from machine import Pin, SPI
# Hardware Map of Connections between Nokia Display(PCD8544) and NodeMCU
# Read on SPI at : https://docs.micropython.org/en/latest/esp8266/quickref.html#hardware-spi-bus
# InCode|	ESP	|	Disp|	Name|	Description
#-------|-------|-------|-------|----------------
# 16	|	D0	|	1	|	RST	|	External reset input, active low
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
ce = Pin(5) # Enable
dc = Pin(4) # Data High / Command low
rst = Pin(16)# Reset Pin
#Create LCD Object with hardware pinout information
lcd = pcd8544_fb.PCD8544_FB(spi, ce, dc, rst)

#Note : 1 Degree = 0.017453 Radians
#Note : Math Functions require the value in radians, so they follow above conversion
def draw_sin(amplitude, freq, phase, yoffset=24): # 24 is midpoint of Display as height is 48 pixels
	for i in range(freq):
		y = int((math.sin((i + phase) * 0.017453) * amplitude) + yoffset)
		x = int((84 / freq) * i) #84 being the maximum width of the display pixels, so we normalize.
		lcd.pixel(x, y, 1)# Highlight that pixel / lit the pixel by writing 1 to it
	lcd.show()

def draw_cos(amplitude, freq, phase, yoffset=24):
	for i in range(freq):
		y = int((math.cos((i + phase) * 0.017453) * amplitude) + yoffset)
		x = int((84 / freq) * i)
		lcd.pixel(x, y, 1)# Highlight that pixel / lit the pixel by writing 1 to it
	lcd.show()

#lets enable few pixels
lcd.fill(0)# Clear the display means filling with 0
lcd.pixel(0,0,1)# a pixel is enabled at (0,0)
lcd.pixel(42,24,1)# a pixel is enabled at (42,24) this is a diagonal midpoint of display
lcd.pixel(83,47,1)# a right most corner of display
lcd.show()# show diplay with above changes
utime.sleep(5)
#big wave
lcd.fill(0)# clear display
draw_sin(20, 360, 0)# (Height,Repetetion, Phase) # no need to use show(), as the function already uses

#little wave
lcd.fill(0)
draw_sin(10, 5*360, 0)

#tiny wave
draw_sin(5, 10*360, 0)

#two waves
lcd.fill(0)
draw_sin(10, 4*360, 0, 12*1)
draw_cos(10, 4*360, 0, 12*3)


# Lets Write Something Now
lcd.fill(0) # Clears the display
lcd.text("  MiUbi  ", 0, 0, 1) # Start Writing from pixel (0,0)
lcd.text("Mon 12:30 PM", 0, 8, 1) # Start Writing from pixel (0,8)
lcd.text("Temp:30dC", 0, 16, 1)# Start Writing from pixel (16,1)
lcd.text("Humid:60 ", 0, 24, 1)# Start Writing from pixel (24,1)
lcd.text("Light Rain,", 0, 32, 1)# Start Writing from pixel (32,1)
lcd.text("29 Oct 19", 0, 40, 1)# Start Writing from pixel (0,40)
lcd.show()


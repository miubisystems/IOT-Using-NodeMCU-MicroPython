# Necessary Libraries to be Imported
import machine
import ssd1306

#Creation of I2C Bus Object Using I2C Library
#Specifiy Desired Pins For CLK and DATA respectively
i2c = machine.I2C(-1, machine.Pin(2), machine.Pin(0))

#Creation of Display Object using SSD1306 Library and binding it to I2C bus
# 128 is X direction pixels and 32 is y direction pixels
display = ssd1306.SSD1306_I2C(128, 64, i2c)
# Fill the Display with 0's
display.fill(0)
# Set a pixel in the origin 0,0 position.
display.text("Hello", 0, 0)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the end 127, 31 position.
display.pixel(127, 31, 1)
# Drawing a Horizontal Line,
# hline(x,y, length, color)
display.hline(0, 20, 20, 1)
# Drawing a Vertical Line
# hline(x,y, length, color)
display.vline(15, 20, 25, 1)
# Drawing a Joining Line
# line(x1,y1,x2,y2, color)
display.line(100, 25, 128, 0, 1)
# Scroll Contents x,y
#display.scroll(1,10)

#Display the above on to display
display.show()
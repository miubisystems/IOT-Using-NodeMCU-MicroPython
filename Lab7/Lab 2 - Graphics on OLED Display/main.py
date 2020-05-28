# Necessary Libraries to be Imported
from machine import I2C, Pin
import time
import ssd1306
import framebuf

#Creation of I2C Bus Object Using I2C Library
#Specifiy Desired Pins For CLK and DATA respectively
i2c = I2C(-1, Pin(5), Pin(4))

#Creation of Display Object using SSD1306 Library and binding it to I2C bus
# 128 is X direction pixels and 32 is y direction pixels
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Dynamic Buffer
images = []
with open('0.pbm', 'rb') as f:#limits of number of binary images
    # Open File in binary mode, the input is 1bit binary image "*.pbm"
    f.readline() # Read 1st line , which may be Creator comment
    f.readline() # Read 2nd line, which is Dimensions
    # Reads Complete File till end of file , in to 'data' buffer
    data = bytearray(f.read())
# Create a two dimensional Frame Buffer using framebuf Library
# framebuf helps during displaying graphics over any display
# Note that the buffer should be same as your display dimension for full resolution
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

# This will display 1's of the buffer
display.invert(0)
# blit routine in display library helps for faster updates of images
display.blit(fbuf, 0, 0)
# shows the buffer loaded on ssd1306
display.show()
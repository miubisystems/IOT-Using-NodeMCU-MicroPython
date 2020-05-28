# Necessary Libraries to be Imported
from machine import I2C, Pin
import ssd1306
import time
import framebuf

#Creation of I2C Bus Object Using I2C Library
#Specifiy Desired Pins For CLK and DATA respectively
i2c = I2C(-1, Pin(5), Pin(4))
#Creation of Display Object using SSD1306 Library and binding it to I2C bus
# 128 is X direction pixels and 32 is y direction pixels
display = ssd1306.SSD1306_I2C(128, 64, i2c)

images = [] # Dynamic Buffer
for n in range(0,19):#limits of number of binary images
    # Open File in binary mode, the input is 1bit binary image "*.pbm"
    with open('out_%s.pbm' % n, 'rb') as f:
        #here f is the object to access the file
        f.readline() # Read 1st line , which may be Creator comment
        f.readline() # Read 2nd line, which is Dimensions
        #Reads Complete File till end of file , in to 'data' buffer
        data = bytearray(f.read())
    # Create a two dimensional Frame Buffer using framebuf Library
    # framebuf helps during displaying graphics over any display
    # Note that the buffer should be same as your display dimension for full resolution
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
    #Append the Frames to 'images' Buffer
    images.append(fbuf)

# This will display 0's of the buffer
display.invert(1)
while True:
    # This helps to loop the images one after the other
    for i in images:
        # images hold the all binary images
        # 'i' shall contain the image buffer for every iteration
        # blit routine in display library helps for faster updates of images
        display.blit(i, 0, 0)
        # shows the buffer loaded on ssd1306
        display.show()
        # delay Routine
        time.sleep(0.02)

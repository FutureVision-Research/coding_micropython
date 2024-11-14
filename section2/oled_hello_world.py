#This script uses an OLED display to write "Hello World!".
#You must installed the ssd1306 package before running this script.

from machine import Pin, I2C #Loads support for digital pins and for I2C communications
from ssd1306 import SSD1306_I2C #Loads support for ssd1306 displays using I2C communication

#Set the resolution of the OLED display
WIDTH = 128
HEIGHT = 64

#Create an object called i2c which contains all communication parameters. 200KHz for I2C communication.
i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=200000) 

#Create an object called oled which contains the parameters for the display.
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) 

oled.fill(0) #Clears the OLED

#Create the text we want to display. The two numbers is the start coordinates in pixels. 0,0 is the top left corner.
oled.text("Hello World!",0, 0) 

oled.show() #Tells the OLED to display the text we just sent.


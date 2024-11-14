#This script asks a person for their name in the Shell and the OLED display.
#It then outputs a message using the person's name onto the OLED display.

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# Initialize I2C for OLED display
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# Set up OLED display
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

#Displays the question on the OLED
oled.fill(0) #Clear the display
oled.text("Enter name:", 0,0)
oled.show() #Update the display

# Ask for user input in the Shell
name = input("What is your name? ")

# Display greeting on the OLED
oled.fill(0)  # Clear the display
oled.text("Hello,", 0, 20)  # Display "Hello,"
oled.text(name, 0, 40)  # Display the name on the next line
oled.show()  # Update the display

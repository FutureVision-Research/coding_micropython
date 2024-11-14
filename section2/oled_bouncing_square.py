#This script outputs an animation onto an OLED display.
#This animate shows a square bouncing around the display and changing size.

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# Initialize I2C interface for OLED
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# Create OLED display object
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Variables for square animation
x, y = 0, 0          # Starting position of the square
size = 10            # Initial size of the square
dx, dy = 2, 2        # Movement increments
ds = 1               # Size increment
min_size, max_size = 10, 20  # Minimum and maximum square size

# Animation loop
while True:
    # Clear the display
    oled.fill(0)

    # Draw the square at (x, y) with the current size. The final number is color. (1=on, 0=off)
    oled.fill_rect(x, y, size, size, 1)

    # Update the display
    oled.show()

    # Move the square
    x += dx 
    y += dy 

    # Change the size of the square
    size += ds

    # Bounce off the edges for position
    if x + size > WIDTH or x < 0:
        dx = -dx
    if y + size > HEIGHT or y < 0:
        dy = -dy

    # Bounce off limits for size
    if size >= max_size or size <= min_size:
        ds = -ds

    # Delay for animation effect
    utime.sleep(0.05)

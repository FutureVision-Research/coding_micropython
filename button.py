# This script causes an external LED to glow when a button is pressed.

from machine import Pin
import time

# Define GPIO pins
button_pin = 16  # Button connected to GPIO 15
led_pin = 14     # LED connected to GPIO 25 (built-in LED on some boards)

# Set up the button as an input with an external pull-up resistor
button = Pin(button_pin, Pin.IN, pull=Pin.NONE)

# Set up the LED as an output
led = Pin(led_pin, Pin.OUT)

while True: #Using "while" in this way allows the program to run in a loop, untill the loop is broken
    # Check if the button is pressed (active high due to pull-down resistor)
    if button.value() == 1:
        led.on()  # Turn on the LED when button is pressed
    else:
        led.off()  # Turn off the LED when button is released
    
    # Small delay to debounce
    time.sleep(0.01)

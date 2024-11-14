# This script causes an external LED to glow when a button is pressed.

from machine import Pin #By loading only the class called "Pin", we don't have to use machine.Pin in our code, we just use Pin
import utime

# Define GPIO pins
button_pin = 16  # Button connected to GPIO 16
led_pin = 14     # Connection for external LED

# Set up the button as an input with an external pull-up resistor
button = Pin(button_pin, Pin.IN, None)

# Set up the LED as an output
led = Pin(led_pin, Pin.OUT)

while True: #Using "while" in this way allows the program to run in a loop, untill the loop is broken
    # Check if the button is pressed (active high due to pull-down resistor)
    if button.value() == 1:
        led.on()  # Turn on the LED when button is pressed
    else:
        led.off()  # Turn off the LED when button is released
    
    # Small delay to debounce
    utime.sleep(0.01)

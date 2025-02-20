# This script is intended to demonstrate the use of a relay.
# When GP17 is pull low by a button, it toggles the state of a boolean variable.
# When the boolean variable is true, GP16 is set to high, which can be used to trigger a relay via a NPN transistor.
# Use a 2N2222 transistor to drive the relay. Be sure to place a diode across the coil.

from machine import Pin #By loading only the class called "Pin", we don't have to use machine.Pin in our code, we just use Pin
import utime

# Define the boolean variable
toggle_state = False

# Define GPIO pins
button_pin = 17  # Button connected to GPIO 16
relay_pin = 16     # Connection for external LED

# Set up the button as an input with an external pull-up resistor
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Set up the LED as an output
relay = Pin(relay_pin, Pin.OUT)

while True: #Using "while" in this way allows the program to run in a loop, until the loop is broken
    # Check if the button is pressed (Pin is held high due to pull-up resitor. Low indicates button press.)
    if button.value() == 0:
        toggle_state = not toggle_state # Flips the boolean variable to the opposite state.
        
    # The following conditional engages the relay if the toggle_state boolean is true.
    if toggle_state == True:    
        relay.on()  # Turn on the LED when button is pressed
        print ("Relay is on")
    else:
        relay.off()  # Turn off the LED when button is released
        print ("Relay is off")
    
    # Small delay to help debounce
    # If this delay is not used, the relay will turn off and on very quickly
    # There are more advanced ways to debounce, but we'll start with this method
    utime.sleep(0.2)
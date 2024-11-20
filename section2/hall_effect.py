#This script powers an LED when the input pin goes low.
#We will use it with a US1881 latching Hall Effect sensor

from machine import Pin
import utime

# Initialize Pin 14 as input with pull-up resistor
pin_14 = Pin(14, Pin.IN, Pin.PULL_UP) #Sets 14 as an input with a built in pull up resistor

# Initialize Pin 15 as output
pin_15 = Pin(15, Pin.OUT)

while True:
    # Read the state of Pin 14
    if pin_14.value() == 0:  # Pin 14 is low
        pin_15.value(1)     # Set Pin 15 high
    else:
        pin_15.value(0)     # Set Pin 15 low
    
    # Small delay to debounce the input
    utime.sleep(0.01)


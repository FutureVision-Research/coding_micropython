# This script is intended for use with a PIR motion sensor.
# When the input is high, it sets the output pin high, and vice versa
from machine import Pin
from utime import sleep

# Define GPIO pins
input_pin = Pin(16, Pin.IN, None)  # GPIO 16 as input. The PIR sensor will hold its output low until an event is triggered so we don't want to use internal pull down. 
output_pin = Pin(17, Pin.OUT) # GPIO 17 as output

# Main loop
while True:
    if input_pin.value()==1:  # Check if GPIO 16 is high
        output_pin.value(1)  # Set GPIO 17 high
    else:
        output_pin.value(0)  # Set GPIO 17 low
        
sleep(.01) #Adds a small delay to ensure stability

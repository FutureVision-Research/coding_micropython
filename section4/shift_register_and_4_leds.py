# This script demonstrates how to communicate with a 74HC595 shift register
# It will sequence four LEDs connected to the first four outputs

from machine import Pin       # Import Pin class for controlling GPIO pins
import time                   # Import time module for delays

# Define GPIO pins connected to the 74HC595 shift register
data_pin = Pin(15, Pin.OUT)   # DS (serial data input) connected to GPIO15
clock_pin = Pin(14, Pin.OUT)  # SH_CP (shift register clock) connected to GPIO14
latch_pin = Pin(13, Pin.OUT)  # ST_CP (storage register clock / latch) connected to GPIO13

def pulse(pin):
    """
    Send a quick HIGH-LOW pulse on the given pin.
    Used to clock data into or latch the register.
    """
    pin.high()                # Set pin HIGH
    time.sleep_us(1)          # Wait a microsecond (tiny delay)
    pin.low()                 # Set pin LOW
    time.sleep_us(1)          # Wait again to finish the pulse

def shift_out(value):
    """
    Shift out 8 bits (MSB first) to the 74HC595 shift register.
    """
    for i in range(7, -1, -1):             # Loop from bit 7 to 0 (MSB to LSB)
        bit = (value >> i) & 1             # Get the current bit value
        data_pin.value(bit)                # Set the data pin to this bit (0 or 1)
        pulse(clock_pin)                   # Pulse the clock pin to shift in the bit
    pulse(latch_pin)                       # After 8 bits, pulse the latch to update output

# Define a list of LED patterns (only using Q0–Q3 for 4 LEDs). The prefix 0b indicates a binary number
led_sequence = [
    0b00000001,  # Turn on LED connected to Q0
    0b00000010,  # Turn on LED connected to Q1
    0b00000100,  # Turn on LED connected to Q2
    0b00001000   # Turn on LED connected to Q3
]

# Main loop: cycle through the LED patterns forever
while True:
    for pattern in led_sequence:      # Loop through each LED pattern
        shift_out(pattern)            # Send pattern to the shift register
        time.sleep(0.3)               # Wait 300ms before the next step

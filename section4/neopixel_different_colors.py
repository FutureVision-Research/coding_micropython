# This script uses the neopixel library to control a strand of five WS2812 LEDS.
# Keep in mind: We are using the neopixel library included with MicroPython, which is a minimal, low-level library developed by the MicroPython team.
# Adafruit provides a more feature-rich NeoPixel library for their own fork of MicroPython, called CircuitPython.
# There is no loop in the script. It will set each LED to a different color and then wait for the user to press Enter
# Once Enter is pressed, the script will clear all LEDs and then end

# Yellow = 255, 255, 0
# Cyan = 0, 255, 255
# Orange = 255, 165, 0
# Purple = 128, 0, 128
# Magenta = 255, 0, 255


import machine            # Allows us to communicate with GPIO pins
import neopixel           # Library to control WS2812 LEDs (built into microPython
from time import sleep    # Allows us to introduce delays into the script
import sys                # Allows us to interact with the Python interpreter

# Setup constants (variables that stay the same through our script.)
NUM_LEDS = 5              # Number of WS2812 LEDs
LED_PIN = 15              # GPIO pin connected to the LED data line

communication_pin = machine.Pin(LED_PIN) #Setup to GPIO pin to communicate with the LED strand
np = neopixel.NeoPixel(communication_pin, NUM_LEDS) #Configure the Neopixel object

def clear_leds_and_exit(): #This function clears all LEDs so they will be "off" when the program exits
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0) #Sets each LED to "no color"
    np.write() # Sends color setting to LEDs
    print("All LEDs are off. Exiting program.")
    # MicroPython script will end at this point

try:
    np[0] = (255, 255, 0)   # set LED 0 to yellow
    np.write()
    
    np[1] = (0, 255, 255)   # set LED 1 to cyan
    np.write()
    
    np[2] = (255, 64, 0)   # set LED 2 to orange
    np.write()
    
    np[3] = (128, 0, 128)   # set LED 3 to purple
    np.write()
    
    np[4] = (255, 0, 255)   # set LED 4 to magenta
    np.write()
    
    # The following waits for the user to press enter and then calls the function to clear the LEDs
    # This is an example of "housekeeping"...cleaning up before
    input("Click inside the Shell, and press Enter to clear all LEDs and exit the program.")   
    clear_leds_and_exit()

except KeyboardInterrupt: #executes the following code block if user breaks out of the program
    clear_leds_and_exit()

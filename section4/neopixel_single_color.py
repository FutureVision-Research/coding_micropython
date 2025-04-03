# This script uses neopixel library to control a strand of five WS2812 LEDS. The Neopixel library was created by Adafruit
# Yellow = 255, 255, 0
# Cyan = 0, 255, 255
# Orange = 255, 165, 0
# Purple = 128, 0, 128
# Magenta = 255, 0, 255


import machine            # Allows us to communicate with GPIO pins
import neopixel           # Library to control WS2812 LEDs (built into microPython
from time import sleep    # Allows us to introduce delays into the script

# Setup constants (variables that stay the same through our script.)
NUM_LEDS = 5              # Number of WS2812 LEDs
LED_PIN = 15              # GPIO pin connected to the LED data line
DELAY = 1                 # Delay between color changes (in seconds)

communication_pin = machine.Pin(LED_PIN) #Setup to GPIO pin to communicate with the LED strand
np = neopixel.NeoPixel(communication_pin, NUM_LEDS) #Configure the Neopixel object

# === Main Loop ===
try:
    while True:
        np[0] = (255, 255, 0)   # set led to yellow
        np.write()
        
except KeyboardInterrupt: #executes the following code block if user breaks out of the program
    for i in range(NUM_LEDS):
            np[i] = (0, 0, 0) #Sets each LED to "no color"
    np.write() # Sends color setting to LEDs
    print("All LEDs are off. Exiting program.")
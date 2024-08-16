#This script blinks an external LED (not built onto the board) connected to a Raspberry Pi Pico RP2040.
#Be sure to place a 51Ω (or higher) resistor in series with the LED.

import machine #Loads machine library, which allows us to control GPIO pins
import utime   #Loads the microtime library, which allows us to keep track of time

# Define the GPIO pin number where the external LED is connected
led_pin = 15  

led = Pin(led_pin, Pin.OUT) #Sets GPIO pin 15 as an output and assigns it to an object called "led"

# Infinite loop to blink the LED
while True:
    led.on()          # Turn the LED on
    time.sleep(1)     # Wait for 1 second (LED stays on)
    led.off()         # Turn the LED off
    time.sleep(1)     # Wait for 1 second (LED stays off)

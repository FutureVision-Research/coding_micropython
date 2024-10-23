#This script blinks three external LEDs (not built onto the board) connected to a Raspberry Pi Pico RP2040.
#Be sure to place a 51Ω (or higher) resistor in series with each LED.

import machine #Loads machine library, which allows us to control GPIO pins
import utime   #Loads the microtime library, which allows us to keep track of time

# Define the GPIO pin numbers where the external LEDs will be connected
led1_pin = 15
led2_pin = 16
led3_pin = 17

led1 = machine.Pin(led1_pin, machine.Pin.OUT) #Sets GPIO pin 15 as an output and assigns it to an object called "led1"
led2 = machine.Pin(led2_pin, machine.Pin.OUT) #Sets GPIO pin 16 as an output and assigns it to an object called "led2"
led3 = machine.Pin(led3_pin, machine.Pin.OUT) #Sets GPIO pin 17 as an output and assigns it to an object called "led3"

# Infinite loop to blink the three LEDs one at a time in sequence
while True:
    led1.on()          # Starts the sequence to turn the first LED on for one second, then turn it off
    utime.sleep(1)     # 
    led1.off()         # 
    utime.sleep(1)     # 
    led2.on()          # Starts the sequence to turn the second LED on for one second, then turn it off
    utime.sleep(1)     # 
    led2.off()         # 
    utime.sleep(1)     # 
    led3.on()          # Starts the sequence to turn the third LED on for one second, then turn it off
    utime.sleep(1)     # 
    led3.off()         # 
    utime.sleep(1)     # 

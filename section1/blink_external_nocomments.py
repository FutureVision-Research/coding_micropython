#This script blinks an external LED (not built onto the board) connected to a Raspberry Pi Pico RP2040.

import machine 
import utime   

led_pin = 15  

led = machine.Pin(led_pin, machine.Pin.OUT) 

while True:
    led.on()          
    utime.sleep(1)     
    led.off()         
    utime.sleep(1)    

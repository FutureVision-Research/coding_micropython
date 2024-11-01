# This script causes an LED to fade off and on in a loop
# Regarding the "Fade up" range: The upper limit 65536 is set because the range function in Python (and MicroPython) is non-inclusive of the upper limit. 
# This means the loop will iterate up to, but not including, 65536.

from machine import Pin, PWM
import time

# Set up the LED pin with PWM on pin 15
led = PWM(Pin(15))
led.freq(1000)  # Set the PWM frequency to 1kHz

while True:
    # Fade up
    for duty in range(0, 65536, 256):  # Increment duty cycle by 256. 
        led.duty_u16(duty)  # Set PWM duty cycle (16-bit)
        time.sleep(0.01)    # Small delay for smooth fading

    # Fade down
    for duty in range(65535, -1, -256):  # Decrement duty cycle by 256
        led.duty_u16(duty)
        time.sleep(0.01)

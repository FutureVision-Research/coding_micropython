# Import the necessary modules
from machine import Pin
from utime import sleep

# Define the LED pins (GPIO 0 through GPIO 9)
# Note: the number for range in the following statement is not correct. We will fix it during class.
led_pins = [Pin(i, Pin.OUT) for i in range(11)]

# Main loop
try:
    while True:
        # Turn on LEDs one by one in sequence
        for i in range(11):
            # Turn off all LEDs
            for led in led_pins:
                led.value(0)
            # Turn on the current LED
            led_pins[i].value(1)
            # Wait for 0.2 seconds
            sleep(0.2)     

except KeyboardInterrupt:
    # Turn off all LEDs when interrupted
    for led in led_pins:
        led.value(0)
    print("Program stopped. All LEDs are now off.")

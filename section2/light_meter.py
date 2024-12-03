# Import necessary modules
from machine import Pin, ADC
from utime import sleep

# Define the LED pins (GPIO 0 through GPIO 9)
led_pins = [Pin(i, Pin.OUT) for i in range(10)]

# Configure ADC (analog input) on GP26 (ADC0)
analog_input = ADC(26)

# Main loop
while True:
    # Read the analog value (range: 0-65535)
    analog_value = analog_input.read_u16()

    # Calculate the number of LEDs to light up (range: 0-10)
    leds_to_light = int((analog_value / 65535) * 10)

    # Light up the calculated number of LEDs
    for i in range(10):
        if i < leds_to_light:
            led_pins[i].value(1)  # Turn on the LED
        else:
            led_pins[i].value(0)  # Turn off the LED

    # Optional: Small delay to stabilize reading
    sleep(0.1)

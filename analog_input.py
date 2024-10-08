from machine import ADC, Pin
import time

# Initialize ADC on GPIO 26 (ADC0)
adc_pin = ADC(Pin(26))

while True:
    # Read raw ADC value (16-bit: 0-65535)
    raw_value = adc_pin.read_u16()  # Returns a value between 0 and 65535 in MicroPython

    # Display the raw ADC value
    print("Raw ADC Value: {}".format(raw_value))
    
    # Small delay before the next reading
    time.sleep(1)

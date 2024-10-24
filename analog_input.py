#Reads the analog input from a potentiomter connected to an analog input and outputs the result to the shell

from machine import ADC, Pin #Loads the classes ADC and Pin from the library module.
import utime

# Initialize ADC on GPIO 26 (ADC0)
adc_pin = ADC(Pin(26))

while True:
    # Read raw ADC value (16-bit: 0-65535)
    raw_value = adc_pin.read_u16()  # Returns a value between 0 and 65535 in MicroPython

    # Display the raw ADC value
    print("Raw ADC Value: {}".format(raw_value))
    
    # Small delay before the next reading
    utime.sleep(1)

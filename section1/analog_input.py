# Reads the analog input from a potentiomter connected to an analog input and outputs the result to the shell
# Keep in mind:
# The ADC in your Pico has a resolution of 12 bits, meaning that it can transform an analog signal into a digital signal as a number ranging from 0 to 4095.
# However, this is transformed inside MicroPython to a 16-bit range, which is 0 to 65535. This is because other MicroPython controllers have a 16 bit ADC.
# Therefore, when we read an analog value, we'll receive a number between 0 and 65535.

from machine import ADC, Pin #Loads the classes ADC and Pin from the library module.
import utime

# Initialize ADC on GPIO 26 (ADC0)
adc_pin = ADC(Pin(26))

while True:
    # Read raw ADC value
    
    raw_value = adc_pin.read_u16()  # Returns a value between 0 and 65535 in MicroPython

    # Display the raw ADC value
    print("Raw ADC Value: {}".format(raw_value))
    
    # Small delay before the next reading
    utime.sleep(1)

# Reads the analog input of a potentiometer connected to GP26 and converts that value to a voltage
# Keep in mind:
# The ADC in your Pico has a resolution of 12 bits, meaning that it can transform an analog signal into a digital signal as a number ranging from 0 to 4095.
# However, this is transformed inside MicroPython to a 16-bit range, which is 0 to 65535. This is because other MicroPython controllers have a 16 bit ADC.
# That means when we read an analog value, we'll receive a number between 0 and 65535.

from machine import ADC, Pin
import utime

# Initialize ADC on GPIO 26 (ADC0)
adc_pin = ADC(Pin(26))

# Define the reference voltage of the RP2040 (usually 3.3V)
VREF = 3.3

while True:
    # Read raw ADC value
    raw_value = adc_pin.read_u16()  # Returns a value between 0 and 65535 in MicroPython (16-bit)

    # Convert raw value to voltage
    voltage = (raw_value / 65535) * VREF

    # Display the voltage reading
    print("Voltage: {:.2f} V".format(voltage))
    
    # Small delay before the next reading
    utime.sleep(1)

# This script reads the temperature from a TMP36 connected to ADC0 (GP26)
# and outputs the result to the console and a SSD1306 OLED display

# Import necessary libraries

# Import ADC (Analog to Digital Converter) for reading analog input, Pin to support GPIO assignments, and I2C to support communication
from machine import ADC, Pin, I2C 
from utime import sleep   # Import sleep for delay
from ssd1306 import SSD1306_I2C # Import support for the SSD1306 OLED display using I2

# Define constants
TEMP_SENSOR_PIN = 26  # Pin where TMP36 is connected (ADC0 = GPIO26)
VOLTAGE_REFERENCE = 3.3  # Reference voltage of the RP2040
ADC_RESOLUTION = 65535  # ADC resolution for RP2040 (16-bit)

# Creat an anlag input object to read the TMP36
temp_sensor = ADC(TEMP_SENSOR_PIN)

# Initialize I2C for OLED display
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# Set up OLED display
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Main loop
while True:
    # Read raw analog value from the sensor
    raw_value = temp_sensor.read_u16()
    
    # Convert raw value to voltage
    voltage = (raw_value / ADC_RESOLUTION) * VOLTAGE_REFERENCE
    
    # Convert voltage to temperature in Celsius
    # TMP36 outputs 0.5V at 0°C, with a scale of 10mV/°C
    celsius = (voltage - 0.5) * 100
    
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    
    # Print the temperature readings to the console
    # A floating point variable must be formatted so it can be displayed.
    # Therefore, we use the f-string feature available in print() to format the floating point variables.
    # :.2f specifies that two places should be shown after the decimal point
    print(f"Temperature: {celsius:.2f} °C | {fahrenheit:.2f} °F") #The f stands for f-string and allows us to include variables inside curly braces.
    
    # Print the temperature readings to the OLD
    
    oled.fill(0) #Clear the display
    oled.text("Temperature:",0,0)
    # oled.text() does not support f-strings, therefore, we must format the floating point variables as shown below.
    # {:.2f} specifies that two places should be shown after the decimal point
    oled.text("{:.2f} C".format(celsius), 0, 20)
    oled.text("{:.2f} F".format(fahrenheit), 0, 40)
    oled.show() #Update the display
    
    # Wait for 1 second before taking the next reading
    sleep(1)

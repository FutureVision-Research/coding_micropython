# Import necessary libraries
from machine import ADC  # Import ADC (Analog to Digital Converter) for reading analog input
from utime import sleep   # Import sleep for delay

# Define constants
TEMP_SENSOR_PIN = 26  # Pin where TMP36 is connected (ADC0 = GPIO26)
VOLTAGE_REFERENCE = 3.3  # Reference voltage of the RP2040
ADC_RESOLUTION = 65535  # ADC resolution for RP2040 (16-bit)

# Creat an anlag input object to read the TMP36
temp_sensor = ADC(TEMP_SENSOR_PIN)

# Main loop
while True:
    # Read raw analog value from the sensor
    raw_value = temp_sensor.read_u16() #Create the variable raw_value and assign it an unsigned 16 bit integer based on a read of the temperature sensor

    # The following lines print a data type and variable contents to the Shell
    print() # Make a blank line
    print("The data type for raw_value is:")
    print(type(raw_value))  # Display the type of raw_value
    print() # Make a blank line
    print("The value of raw_value is:")
    print(raw_value) # Display the information contained in the variable raw_value
    input("Press Enter to continue...")  # Wait for the user to press Enter before proceeding
    print() # Make a blank line
    
    # Convert raw value to voltage
    voltage = (raw_value / ADC_RESOLUTION) * VOLTAGE_REFERENCE
    
    # The following lines print a data type and variable contents to the Shell
    print("The data type for voltage is:")  
    print(type(voltage)) # Display the type of voltage
    print()
    print("The value of voltage is:")
    print (voltage) # Display the information contained in the variable voltage
    input("Press Enter to continue...")  # Wait for the user to press Enter before proceeding
    print() # Make a blank line
    
    # Convert voltage to temperature in Celsius
    # TMP36 outputs 0.5V at 0°C, with a scale of 10mV/°C
    celsius = (voltage - 0.5) * 100
    
    # The following lines print a data type and variable contents to the Shell
    print("The data type of celsius is:")
    print(type(celsius)) # Display the type of celsius
    print() # Make a blank line
    print("The value of celsius is: ")
    print (celsius) # Display the information contained in the variable celsius
    input("Press Enter to continue...")  # Wait for the user to press Enter before proceeding
    
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    
    # Print the temperature readings to the console
    print(f"Temperature: {celsius:.2f} °C | {fahrenheit:.2f} °F") #The f stands for f-string and allows us to include variables inside curly braces.
    
    # Wait for 1 second before taking the next reading
    sleep(1)

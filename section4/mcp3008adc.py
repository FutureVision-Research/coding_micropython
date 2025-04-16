# This script uses SPI (Serial Peripheral Interface) to communicate with a MCP3008 ADC
# It reads the input from ADC 0 on the MCP3008 and changes the brightness of an LED based on that input
# Use a 3V3 voltage divider as the input for the MCP3008
# LED is connected via a current limiting resistor to GP15

from machine import Pin, PWM, SPI  # Import classes for GPIO, PWM, and SPI
import time  # Import time module for delays

# ----- SPI Setup -----
# Configure SPI0 on the Pico using the default pins:
# SCK  -> GP18 (Serial Clock)
# MOSI -> GP19 (Master Out Slave In)
# MISO -> GP16 (Master In Slave Out)
spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

# Chip Select (CS) pin for the MCP3008
cs = Pin(17, Pin.OUT)

# ----- PWM Setup -----
# Set up PWM on GP15 for the LED
led = PWM(Pin(15))    # Use GP15 as a PWM pin to control LED brightness
led.freq(1000)        # Set PWM frequency to 1 kHz (fast enough to avoid flicker)

# ----- MCP3008 Read Function -----
def read_mcp3008(channel):
    """
    Reads a 10-bit analog value (0 to 1023) from the MCP3008 ADC chip.
    'channel' must be between 0 and 7 (CH0 to CH7).
    """
    if not 0 <= channel <= 7:
        raise ValueError("Channel must be between 0 and 7")

    # Build the command to send to MCP3008
    # Byte 1: 0x01 = 00000001 -> Start bit
    # Byte 2: (0x08 | channel) << 4
    #   - 0x08 = 00001000: tells MCP3008 we're doing a single-ended read
    #   - channel is shifted into the correct position
    # Byte 3: 0x00 = dummy byte, required to clock out the result
    buf = bytearray([0x01, (0x08 | channel) << 4, 0x00])

    # Begin SPI transaction
    cs.value(0)  # Set CS low to start communication
    spi.write_readinto(buf, buf)  # Send command and read the response into the same buffer
    cs.value(1)  # Set CS high to end communication

    # Response:
    # buf[1] (after SPI): xxxx abcd -> we want the lower 4 bits only (abcd)
    # buf[2]           : efgh ijkl -> this holds the lower 8 bits of result
    #
    # Combine to get full 10-bit result: abcdefghij
    #
    # Step-by-step breakdown:
    # buf[1] & 0x0F   -> Masks the upper 4 bits, keeping only the lower 4 (00001111)
    # << 8            -> Shifts those 4 bits to the left to become the top of our 10-bit result
    # | buf[2]        -> Adds in the lower 8 bits from the third byte using bitwise OR
    result = ((buf[1] & 0x0F) << 8) | buf[2]

    return result  # Final result is a number from 0 to 1023

# ----- Main Loop -----
while True:
    adc_value = read_mcp3008(0)  # Read analog value from CH0 (voltage divider input)

    # Convert 10-bit ADC value (0–1023) to actual voltage (based on 3.3V reference)
    voltage = adc_value * 3.3 / 1023

    # Scale 10-bit ADC to 16-bit PWM range (0–65535)
    pwm_value = int(adc_value * 65535 / 1023)

    # Apply PWM duty cycle to the LED — this changes its brightness
    led.duty_u16(pwm_value)

    # Print values for debugging/monitoring
    print("ADC:", adc_value, "Voltage:", round(voltage, 2), "V", "PWM:", pwm_value)

    time.sleep(0.1)  # Small delay to slow down output and avoid flicker

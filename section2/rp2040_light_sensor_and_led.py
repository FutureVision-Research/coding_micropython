# MicroPython script for the Raspberry Pi Pico (RP2040)
# This script reads an analog input from GPIO 26 (ADC0) and outputs
# a proportional PWM signal on GPIO 15. The analog input is read 
# using the onboard ADC (Analog-to-Digital Converter), which returns
# a 16-bit value (0-65535). This value is then scaled to set the 
# PWM duty cycle on GPIO 15, allowing for an analog-like output based 
# on the input.

# Components:
# 1. Analog sensor or potentiometer connected to GPIO 26 (ADC input)
# 2. PWM-controlled device (LED, motor, etc.) connected to GPIO 15

# The map_value function is used to map the ADC value (0-65535) to a 
# corresponding PWM duty cycle (0-65535). The PWM frequency is set 
# to 1kHz.

from machine import Pin, ADC, PWM
import time

# Setup ADC on GPIO 26 (ADC0)
adc = ADC(Pin(26))

# Setup PWM on GPIO 15
pwm_pin = Pin(15)
pwm = PWM(pwm_pin)
pwm.freq(1000)  # Set PWM frequency to 1kHz

# Function to map analog value (0-65535) to PWM duty (0-65535)
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    # Read analog value from GPIO 26
    analog_value = adc.read_u16()
    
    # Map analog value to PWM duty cycle
    duty_cycle = map_value(analog_value, 0, 65535, 0, 65535)
    
    # Set PWM duty cycle (0-65535)
    pwm.duty_u16(duty_cycle)
    
    # Delay for stability
    time.sleep(0.01)

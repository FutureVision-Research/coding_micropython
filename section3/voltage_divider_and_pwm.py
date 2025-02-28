# This script reads an analog input from GPIO 26 (ADC0) and outputs
# a PWM signal on GPIO 15.


from machine import Pin, ADC, PWM
from utime import sleep

# Setup ADC on GPIO 26 (ADC0)
adc = ADC(Pin(26))

# Setup PWM on GPIO 15
pwm_pin = Pin(15)
pwm = PWM(pwm_pin)
pwm.freq(1000)  # Set PWM frequency to 1kHz

while True:
    # Read analog value from GPIO 26
    analog_value = adc.read_u16()
    
    #Since the analog input will be 0 to 65535, and the duty cycle range is 0 65635, we can use the analog value as the duty cycle
    pwm.duty_u16(analog_value)
    
    # Delay for stability
    sleep(0.01)

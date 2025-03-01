from machine import Pin, PWM, ADC
import time

# Servo PWM setup
servo = PWM(Pin(19)) # Create PWM object to control the servo on GP19
servo.freq(50)  # Standard servo PWM frequency (50 Hz)

# ADC setup
adc = ADC(Pin(26)) #Create ADC input on ADC0 (GP26)

# Function to convert ADC value to servo duty cycle
def set_servo_position(adc_value):
    # Map ADC value (0-65535) to servo angle (0-180)
    angle = (adc_value / 65535) * 180  # Convert ADC value to an angle
    duty = int(2500 + (angle / 180) * 5000)  # Convert angle to duty cycle (500-7500 range)
    
    # Apply duty cycle to the servo
    servo.duty_u16(duty)

# Main loop
while True:
    adc_value = adc.read_u16()  # Read ADC value (0-65535)
    set_servo_position(adc_value) #calls the function to set the servo position
    time.sleep(0.05)  # Small delay to prevent excessive updates

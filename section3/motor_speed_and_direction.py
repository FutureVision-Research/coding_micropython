# This script controls a DC motor using the L293 H-bridge IC.
# A voltage divider on ADC0 controls the speed of the motor.
# A pushbutton on GP4 toggles the motor's direction.

from machine import Pin, PWM, ADC
import utime

# Define L293D H-Bridge pins
motor_in1 = Pin(14, Pin.OUT) # Connects to L293 pin 2
motor_in2 = Pin(15, Pin.OUT) # Connects to L293 pin 7
motor_pwm = PWM(Pin(13))  # Enable pin for PWM speed control. Connects to L293 pin 1
motor_pwm.freq(1000)  # Set PWM frequency

# Define analog input (voltage divider)
potentiometer = ADC(26)  # GP26 (ADC0)

# Define pushbutton (with external pull-up resistor)
button = Pin(16, Pin.IN, Pin.PULL_UP) 

# Initial motor direction
motor_direction = True  # True = Forward, False = Reverse

def set_motor(speed, direction): # Set motor speed and direction
    
    if direction: # This if statement executes if the boolean direction is True
        motor_in1.value(1)
        motor_in2.value(0)
    else:
        motor_in1.value(0)
        motor_in2.value(1)
        
    motor_pwm.duty_u16(speed) #Sets PWM based on duty cycle determined by potentiometer

try:
    while True:
        # Read potentiometer value (0-65535)
        speed = potentiometer.read_u16()
        
        # Check if button is pressed to toggle direction
        if button.value() == 0: 
            motor_direction = not motor_direction
            utime.sleep(0.3)  # Debounce delay
        
        # Call the function to set the motor's speed and direction
        set_motor(speed, motor_direction)

        utime.sleep(0.1)  # Short delay
        
except KeyboardInterrupt: #Disable PMW before breaking out of the program
    motor_pwm.duty_u16(0) #Sets PWM to zero which turns off the L293
    print("Motor is disabled")


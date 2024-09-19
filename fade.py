from machine import Pin, PWM
import time

# Initialize PWM on GPIO 15 for the LED
led_pwm = PWM(Pin(15))

# Set PWM frequency (in Hz)
led_pwm.freq(1000)  # 1 kHz frequency

# Total fade time in seconds
fade_time = 5

# The PWM duty cycle is 16-bit, so it ranges from 0 to 65535
max_duty = 65535

# Calculate the time between each step
step_time = fade_time / max_duty

# Gradually increase the duty cycle to fade the LED in
for duty in range(0, max_duty + 1):
    led_pwm.duty_u16(duty)  # Set duty cycle (brightness)
    time.sleep(step_time)    # Wait before increasing the brightness further

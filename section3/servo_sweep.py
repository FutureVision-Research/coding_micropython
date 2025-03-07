# This script demonstrates sweeping a servo back and forth
# Written by Benjamin Book

from machine import Pin, PWM
from utime import sleep

servo = PWM(Pin(19))
servo.freq(50)
servo.duty_u16(1500)
try:
    while True:
       for duty in range(1500, 7850, 10):
           servo.duty_u16(duty)
           print(f'The PWM duty cycle is {duty}')
           sleep(0.01)
       for duty in range(7850, 1500, -10):
           servo.duty_u16(duty)
           print(f'The PWM dutycycle is {duty}')
           sleep(0.01)
except KeyboardInterrupt:
    servo.deinit()
    print('Servo is disabled')

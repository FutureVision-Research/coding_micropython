# This demonstrates playing notes without using a function

from machine import Pin, PWM
from time import sleep

# Set up the speaker pin connected to GP15 as PWM
speaker = PWM(Pin(15))

# Frequncies for C major scale = 261, 294, 329, 349, 392, 440, 494, 523

try:
    speaker.freq(261) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(294) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(329) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(349) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(392) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(440) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(494) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.freq(523) # Sends a specific frequency as PWM
    speaker.duty_u16(30000)  # Adjust volume (0-65535). 
    sleep(.5) # Rests between notes. 
    speaker.duty_u16(0)  # Turn off sound. 
    sleep(0.1)  # Short pause between notes

    speaker.deinit()  # Turn off PWM after playing. 

except KeyboardInterrupt:
    speaker.deinit()
    print("Speaker is off")

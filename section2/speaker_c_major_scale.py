# This script uses PWM to play tones over a speaker connected to GP15.
# Best practice when using one PWM pin to drive a speaker (which is DC) is to use a diode to protect from kickback.

from machine import Pin, PWM
from time import sleep

# Set up the speaker pin connected to GP15 as PWM
speaker = PWM(Pin(15))

# Create a data type called a "list" which stores the frequencies for the C Major scale (Middle C to High C)
# List of notes and their frequencies rounded to the nearest integer: C4:261, D4:294, E4:329, F4:349, G4:392, A4:440, B4:494, C5:523
C_MAJOR_SCALE = [261, 294, 329, 349, 392, 440, 494, 523]

# Create a variable to hold the duration for each note (milliseconds)
NOTE_DURATION = 500

# Function to play a tone
def play_tone(frequency, duration): # Creates a function called "play_tone" and receives two variables
    if frequency > 0: # Will only send a PWM signal to the speaker if a frequency is specified
        speaker.freq(frequency) # Sends a specific frequency as PWM
        speaker.duty_u16(30000)  # Adjust volume (0-65535). Values higher than 30000 may cause distortion
        sleep(duration / 1000) # Rests between notes. By dividing by 1,000, we convert milliseconds to seconds
        speaker.duty_u16(0)  # Turn off sound. It is important to turn off PWM so no voltage is sent to speaker
    sleep(0.1)  # Short pause between notes

# Play the C Major scale
for frequency in C_MAJOR_SCALE: #Example of a for-each loop that iterates through each freq. in our list
    play_tone(frequency, NOTE_DURATION) #Calls the function "play_tone" and provides a freq. and note duration

speaker.deinit()  # Turn off PWM after playing. Never leave PWM on when connected to a speaker.

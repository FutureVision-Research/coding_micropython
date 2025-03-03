# This script demonstrates how to drive a bipolar stepper motor using a L293 Hbridge.

from machine import Pin
import time

# Define motor control pins and set them as output
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# Step sequence for a bipolar stepper motor
# Each tuple represents the state of the four control pins
step_sequence = [
    (1, 0, 1, 0),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (1, 0, 0, 1)
]

# Function to set motor pins according to a given state
def set_pins(state):
    IN1.value(state[0])
    IN2.value(state[1])
    IN3.value(state[2])
    IN4.value(state[3])

# Function to rotate the stepper motor a given number of steps
def rotate_stepper(steps, delay=0.005):
    step_count = len(step_sequence)  # Number of steps in the sequence
    direction = 1 if steps > 0 else -1  # Determine direction based on sign of steps
    
    # Loop through the steps in the specified direction
    for _ in range(abs(steps)):
        for step in range(step_count)[::direction]:
            set_pins(step_sequence[step])  # Set the pins for current step
            time.sleep(delay)  # Delay between steps to control speed
    
    # Turn off all pins after movement to save power
    set_pins((0, 0, 0, 0))

# Main loop to take user input and control the motor
while True:
    try:
        # Prompt user for number of steps to move the motor
        steps = int(input("Enter steps (negative for reverse): "))
        rotate_stepper(steps)  # Call function to rotate motor
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

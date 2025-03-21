# This script demonstrates how to drive a bipolar stepper motor using the l293 Hbridge.
# When you run the script, you'll be prompted to enter the number of steps. 

from machine import Pin  # Import Pin class to control GPIO pins
import time  # Import time module for delays

# Define motor control pins and set them as output using the Pin class
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# Step sequence for a bipolar stepper motor
# This is a list of tuples, where each tuple contains 4 integers (0 or 1)
# Each tuple represents the ON/OFF state for the four control pins
step_sequence = [
    (1, 0, 1, 0),  # Tuple: Pin1 and Pin3 ON
    (0, 1, 1, 0),  # Tuple: Pin2 and Pin3 ON
    (0, 1, 0, 1),  # Tuple: Pin2 and Pin4 ON
    (1, 0, 0, 1)   # Tuple: Pin1 and Pin4 ON
]

# Function to set motor pins according to a given tuple state
def set_pins(state):
    IN1.value(state[0])  # Access tuple index 0
    IN2.value(state[1])  # Access tuple index 1
    IN3.value(state[2])  # Access tuple index 2
    IN4.value(state[3])  # Access tuple index 3

# Function to rotate the stepper motor a given number of steps
# The smaller the delay value, the faster the rotation speed. The minimum delay is approximately 0.002
def rotate_stepper(steps, delay=0.005):
    step_count = len(step_sequence)  # Get the length of the list (number of steps in the sequence)
    
    # Ternary operation: determines direction (1 for forward, -1 for reverse)
    direction = 1 if steps > 0 else -1
    
    # Loop through the number of steps in the specified direction
    for _ in range(abs(steps)):
        # Use slicing with step to reverse sequence if needed (step_count)[::direction] is a list slice
        for step in range(step_count)[::direction]:
            set_pins(step_sequence[step])  # Call function with the current tuple from the list
            time.sleep(delay)  # Delay between steps to control speed
    
    # Turn off all pins after movement to save power
    set_pins((0, 0, 0, 0))  # A tuple of all 0s turns off the motor

# Main loop to take user input and control the motor
while True:
    try:
        # Prompt user for number of steps to move the motor
        # input() returns a string, which we convert to an integer with int()
        steps = int(input("Enter steps (negative for reverse): "))
        rotate_stepper(steps)  # Call function to rotate motor
    except ValueError:
        print("Please enter a valid integer.")  # Handle non-integer input errors


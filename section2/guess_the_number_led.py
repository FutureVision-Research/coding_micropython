# This script generates a random number and asks the user to guess the number
# Connect a bi-color red/green LED to GP16 and GP17. Long lead of LED should be connected to GP16
# Be sure to put at least a 150Ω resistor in series with the LED
# LED starts off red, but turns green when the user guesses the correct number
# LED returns to red if the user wants to play again
# If the user chooses not to play again, or breaks out of the script, the LED is turned off

import random # Allows us to generate random numbers
from machine import Pin # Allows communication with GPIO pins

# Setup the two GPIO pins to control the LED
# Reminder, once a GPIO pin is set as output, it is grounded (off) until turned on
led_pin0 = Pin(16, Pin.OUT)
led_pin1 = Pin(17, Pin.OUT)

# Use variables to store the number range to be guessed by the user.
min_number = 1
max_number = 100

try:
    while True:
        # Set LED as red. This sets pin0 at 3V# and pin1 is grounded
        led_pin0.on()
        led_pin1.off()
        
        number_to_guess = random.randint(min_number, max_number) # Generates a random integer within the number range specified.
        attempts = 0 # Sets the counter to keep track of how many guesses by the user.
        
        print(f"I have chosen a number between {min_number} and {max_number}. Try to guess it!")
        
        while True:
            # This line prints a message on the screen and accepts an input from the user. The value saved to user_guess will be a string.
            user_guess = input("Enter your guess as an integer: ")        
            
            user_guess = int(user_guess) #Converts the input from a string into an integer
            attempts += 1 # Adds one to the attempts counter.
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                # Set LED as green. This grounds pin0 and sets pin1 to 3V3
                led_pin0.off()
                led_pin1.on()
                
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break # This breaks out of the inner most "while true:" loop, this means it will drop down to the statement asking if the user wants to play again.

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes':
            # Turn LED off. This grounds both pin0 and pin1
            led_pin0.off()
            led_pin1.off()
            
            print("Thanks for playing! LED is now off. Goodbye.")
            break # This breaks out of the main "while true" loop, which ends the program.

except KeyboardInterrupt:
    # Turn LED off. This grounds both pin0 and pin1
    led_pin0.off()
    led_pin1.off()
    print("Program stopped. LED is now off.")
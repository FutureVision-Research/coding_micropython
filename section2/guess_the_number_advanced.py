import random # Allows us to generate random numbers

# Use variables to store the number range to be guessed by the user.
min_number = 1
max_number = 100

while True:
    number_to_guess = random.randint(min_number, max_number) # Generates a random integer within the number range specified.
    attempts = 0 # Sets the counter to keep track of how many guesses by the user.
    
    print(f"I have chosen a number between {min_number} and {max_number}. Try to guess it!")
    
    while True:
        # This line prints a message on the screen and accepts an input from the user. The value saved to user_guess will be a string.
        # .strip() removes any any spaces entered by the user.
        user_guess = input("Enter your guess as an integer: ").strip()
        
        if not user_guess.isdigit(): # Checks to see if the user entered digits only
            print("I don't think you entered an integer. Please try again.")
            continue  # Skips the rest of the inner most while true: loop and starts the loop over by asking for input again
        
        user_guess = int(user_guess) #Converts the input from a string into an integer
        
        
        attempts += 1 # Adds one to the attempts counter.
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break # This breaks out of the inner most "while true:" loop, this means it will drop down to the statement asking if the user wants to play again.

    # .strip() removes any extra spaces entered by the user. While, .lower() converts the input to lower case. 
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break # This breaks out of the main "while true" loop, which ends the program.

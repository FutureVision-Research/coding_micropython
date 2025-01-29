import random # Allows us to generate random numbers

# Use variables to store the number range to be guessed by the user.
min_number = 1
max_number = 100

while True:
    number_to_guess = random.randint(min_number, max_number) #Generates a random integer within the number range specified.
    attempts = 0 #Sets the counter to keep track of how many guesses by the user.
    
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
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
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    # .strip removes any accidental spaces and .lower() converts the input to lower case
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break

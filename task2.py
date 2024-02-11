import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        # Get user input for the guess
        user_input = input("Guess the number (between 1 and 100): ")
        
        # Validate user input
        if not user_input.isdigit():
            print("Please enter a valid integer.")
            continue
        
        user_guess = int(user_input)
        attempts += 1

        # Compare the user's guess with the secret number
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
guess_the_number()

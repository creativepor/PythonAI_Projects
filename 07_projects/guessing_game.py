# Lesson 7: Mini Project - Number Guessing Game

import random

def run_guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game! 🎯")
    print(f"I am thinking of a number between 1 and 20. You have {max_attempts} attempts.")
    
    # Simulated run logic for demonstration
    test_guesses = [10, 15, secret_number]
    for guess in test_guesses:
        attempts += 1
        print(f"\nAttempt {attempts}: Guessed {guess}")
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts! 🎉")
            break

if __name__ == "__main__":
    run_guessing_game()

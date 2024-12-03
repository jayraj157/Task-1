
import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed_correctly:
        # Prompt the user for their guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare the guess to the generated number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
            print(f"It took you {attempts} attempts to guess the number.")

if __name__=="__main__":
    guessing_game()
    
    
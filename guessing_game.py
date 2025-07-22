# Guessing Game - Jasir Muhammad
import random

def generate_random_number(): ## Generates a random number between 1 and 100
    return random.randint(1, 100)

def get_user_guess(): ## Prompts the user to guess the number and gives hints
    number_to_guess = generate_random_number()
    while True:
        try:
            get_user_guesser = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if get_user_guesser == number_to_guess: ## User guessed the number correctly
            print("Congratulations! You guessed the number!")
            break
        elif get_user_guesser < number_to_guess: ## User guessed too low
            print("Too low! Try again.")
            user_exit = input("Enter 'exit' to quit or continue entering guesses: ")
            if user_exit.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break
            else:
                continue
        elif get_user_guesser > number_to_guess: ## User guessed too high
            print("Too high! Try again.")
            user_exit = input("Enter 'exit' to quit or continue entering guesses: ")
            if user_exit.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break
            else:
                continue
        else: ## User entered an invalid guess
            print("Wrong guess, try again!")
            user_exit = input("Enter 'exit' to quit or continue entering guesses: ")
            if user_exit.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break
            else:
                continue

def play_guessing_game(): ## Main function to play the guessing game
   while True:
      print("Welcome to the Guessing Game!")
      get_user_guess()
      print("Thanks for playing!")
      break

def game_loop(): ## Calls the main function to start the game
   play_guessing_game()

game_loop()
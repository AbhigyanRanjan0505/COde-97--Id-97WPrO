# importing random library
import random

# setting values of chances and the number
number = random.randint(1, 9)
chances = 0

# printing the name of the game
print("Number guessing game")
print("")

# repeating until chances are not over
while chances < 5:
    # player enters a number guess
    guess = int(input("Guess a number between 1 to 9: "))
    print("")

    # checking if guess exists and its in expected range
    if guess and guess > 1 and guess < 10:
        # checking if the number is correct
        if guess == number:
            # telling player that the number is correct
            print(f"Your guess is correct. The number was {number}.")
            print("")

            # congratulating the player
            print("You won")
            print("")

            # discontinuing the while loop and ending the game
            break

        # checking if the number is lesser
        elif guess < number:
            # telling player that the number is lesser
            print(f"Your guess is too low. Guess a number higher that {guess}")
            print("")

            # decreasing the chances
            chances += 1

        # checking if the number is greater
        elif guess > number:
            # telling player that the number is greater
            print(f"Your guess is too high. Guess a number lower that {guess}")
            print("")

            # decreasing the chances
            chances += 1

# ending the game if chances are over
if not chances < 5:
    # showing player a lose message
    print(f"You lost. The correct answer was - {number}. Try again")

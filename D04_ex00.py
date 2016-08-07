#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random as random

# Body
# generates random interger 1 - 25
secret_number = (random.randint(1,25))

#Set up guess counter
count_guess = 5

#Main game loop
while count_guess > 0:
    guess = ''
    while guess == '':
        try:
            guess = int(input('Enter a # ')) # prompts user for guess, fails != int
            if  guess > 25 or guess < 1:     # validates int is between 1 - 25
                print('Please guess a number between 1 - 25')
                guess = ''
        except:
            print('Please enter an integer.')

    #tell user if correct, high, low
    if guess == secret_number:              # correct case, exits program
        print("You guessed it! Goodbye.")
        break
    elif guess <= secret_number:            # guess low
        count_guess -= 1
        print("Higher.\nYou have " + str(count_guess) + " guesses left." )
        guess = ''
    elif guess >= secret_number:            # guess high
        count_guess -= 1
        print("Lower.\nYou have " + str(count_guess) + " guesses left." )
        guess = ''
else:                                       # game over msg if out of guesses
    print("Too many guesses. Try again.")
#print("Too many guesses. Try again")




################################################################################
def main():

    if __name__ == '__main__':
        main()

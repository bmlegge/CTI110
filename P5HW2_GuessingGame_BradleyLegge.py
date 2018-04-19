#Create a random number and ask the user to guess.  Then display if they got it right or not.  If not ask them to play again.
#4/18/2018
#CTI-110 P5HW2 - Random Number Guessing Game
#Bradley Legge

import random

MIN = 1
MAX = 100

def main():
    again = 'y'

    while again == 'y' or again == 'Y':
        guess = int(input('Guess the secret number: '))
        play_game(guess)
        again = input('Play again? (y = yes): ')

def play_game(guess):
    rand = random.randint(MIN, MAX)
    tries = 1
    while guess != rand:
        if guess == rand:
            print('You guess the secret number!!')
        elif guess > rand:
            print('Too high, try again!')
        elif guess < rand:
            print('Too low, try again!')
        guess = int(input('Guess the secret number: '))        
        tries = tries + 1
    print('It took you ' , tries, ' tries to guess the secret number!')
main()


"""
## Number Guessing Game

Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low

## Optional Enhancements 

- Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level. 
- Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed. 
- Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game. 
"""

import random

while True:
    try:
        min: int = int(input('Enter a minimum number: '))
        max: int = int(input('Enter a maximum number: '))
        rand_num: int = random.randint(min, max)
        attempts: int = 0
        break
    except ValueError:
        print('Please enter a valid number! ')

while True:
    guess: int = int(input(f'Guess the number (between {min} and {max}): '))
    attempts += 1
    
    if guess == rand_num:
        print(f'Congratulations! You guesses the number in {attempts} attempts')
        break
    
    if guess > rand_num:
        print('Too high! Try again.')
    
    if guess < rand_num:
        print('Too low! Try again.')


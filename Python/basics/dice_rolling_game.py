"""
Source: https://codewithmosh.com/ -> Python Projects for Beginners
## Dice Rolling Game
A program that simulates rolling a pair of dice. Each time the program runs, it
randomly generate two numbers between 1 and 6 (inclusive), representing the
result of each die. The program should then display the results and ask if the
user would like to roll again.
"""
import random

while True:
    choice: str = input('Roll the dice? (y/n): ')
    if choice.casefold() == 'y':
        die_1: int = random.randint(1, 6)
        die_2: int = random.randint(1, 6)
        print(f'({die_1}, {die_2})')
    elif choice.casefold() == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid Choice!')
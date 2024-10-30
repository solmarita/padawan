"""
Source: https://codewithmosh.com/ -> Python Projects for Beginners
## Rock, Paper, Scissors Game

Write a program to simulate a game of Rock, Paper, Scissors.
The game will prompt the player to choose rock, paper, or scissors by
typing 'r', 'p', or 's'. The computer will randomly select its choice.
The game will then display both choices using emojis and determine the winner
based on the rules.

## Optional Enhancements
- Modify the game so that the first player (or computer) to win two out of
three rounds is declared the overall winner. This adds a competitive aspect
to the game.
- Keep a tally of how many times the player wins, loses, or ties with the
computer. Display these statistics at the end of the game.
- Add an option for two players to play against each other, taking turns
to input their choices. The program should then determine the winner based
on their inputs.
"""
from typing import Any

def get_user_input(prompt: str, data_type: type) -> Any:
    while True:
        user_input: str = input(prompt)

        try:
            return data_type(user_input)
        except ValueError:
            print(f'Invalid input. Please provide a value of type {data_type.__name__}')
        except Exception as e: # Gracefully handle other unforseen errors
            print(f'Input Error: {e}')

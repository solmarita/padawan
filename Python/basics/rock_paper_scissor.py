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
from typing import Any, Optional
import random

def get_user_input(
        prompt: str,
        data_type: type,
        choices: Optional[list[Any]] = None
        ) -> Any:
    """
    Continuously prompt for user input until a valid value is given.

    Parameters:
        prompt (str): Message displayed when asking for input.
        data_type (type): Expected type of input (e.g., int, float, str).
        choices (Optional[list[Any]]): List of acceptable values for the input. 
        If provided, the input must match one of these choices.

    Raises:
        ValueError: If input cannot be cast to the specified type.
        Exception: If any unforeseen errors occur during input processing.
    
    Example:
        >>> user_input = get_user_input(
        ...     "Enter an integer: ",
        ...     choices=[1, 2, 3],
        ...     data_type=int
        ... )
        Enter an integer: abc
        Invalid input. Please provide a value of type int.
        Enter an integer: 4
        Invalid choice. Please choose from: [1, 2, 3]
        Enter an integer: 2
        >>> print(user_input)
        2

        >>> user_choice = get_user_input(
        ...     "Choose rock, paper, or scissors (r/p/s): ",
        ...     choices=['r', 'p', 's'],
        ...     data_type=str
        ... )
        Choose rock, paper, or scissors (r/p/s): x
        Invalid choice. Please choose from: ['r', 'p', 's']
        Choose rock, paper, or scissors (r/p/s): p
        >>> print(user_choice)
        'p'
    """
    while True:
        prompt_with_choices: str = f"{prompt}, choices: {choices}" if choices \
            else f"{prompt}"
        user_input: str = input(prompt_with_choices)
        try:
            value = data_type(user_input)

            if choices is not None and value not in choices:
                print(f'Invalid choice. Please choose from: {choices}')
                continue

            return value
        except ValueError:
            print(f'Invalid input. Please provide a value of type '
                  f'{data_type.__name__}')
        except Exception as e: # Gracefully handle other unforseen errors
            print(f'Input Error: {e}')

def main():
    """
    Wraps the game logic to ensure it runs only when the script is executed directly.

    This function contains the main flow of the Rock, Paper, Scissors game, preventing 
    accidental execution when the file is imported as a module.
    """
    #choices: list[str] = ['r', 'p', 's']
    choices: dict[str, str] = {
        'r': '🪨',
        'p': '📃',
        's': '✂️'
    }

    player_1_wins: int = 0
    ties: int = 0
    player_2_wins: int = 0
    win_threshold: int = 2

    # Choosing Opponent
    opponent: str = get_user_input(
        'Play against computer of human? (c/h)',
        str,
        ['c', 'h'])

    player_1_name: str = get_user_input(
        'Player 1, enter your name: ',
        str)

    if opponent == 'h':
        player_2_name: str = get_user_input(
            'Player 2, enter your name: ',
            str)
    else:
        player_2_name: str = 'Computer'


    while True:
        # Making Choices
        player_1_choice: str = get_user_input(
            f'{player_1_name} > Rock, Paper, or Scissors? (r/p/s): ',
            str,
            ['r', 'p', 's'])
        
        if player_2_name == 'Computer':
            player_2_choice: str = random.choice(list(choices.keys()))
        else:
            player_2_choice: str = get_user_input(
                f'{player_2_name} > Rock, Paper, or Scissors? (r/p/s): ',
                str,
                ['r', 'p', 's'])

        match [player_1_choice, player_2_choice]:
            case ['s', 's']:
                result = 'tie'
                ties += 1
            case ['s', 'p']:
                result = 'win'
                player_1_wins += 1
            case ['s', 'r']:
                result = 'lose'
                player_2_wins += 1
            case ['p', 's']:
                result = 'lose'
                player_2_wins += 1
            case ['p', 'p']:
                result = 'tie'
                ties += 1
            case ['p', 'r']:
                result = 'win'
                player_1_wins += 1
            case ['r', 's']:
                result = 'win'
                player_1_wins += 1
            case ['r', 'p']:
                result = 'lose'
                player_2_wins += 1
            case ['r', 'r']:
                result = 'tie'
                ties += 1
            case _:
                result = 'have an error! (Hint: You entered an invalid choice)'
                break

        print(f'{player_1_name} chose '
            f'{choices.get(player_1_choice, 'an invalid choice!')}')
        print(f'{player_2_name} chose '
            f'{choices.get(player_2_choice, 'an invalid choice!')}')
        print(f'{player_1_name}, you {result}')

        if player_1_wins == win_threshold or player_2_wins == win_threshold:
            if player_1_wins > player_2_wins:
                print(f'{player_1_name} won the game!')
            elif player_2_wins > player_1_wins:
                print(f'{player_2_name} won the game!')
            
            print('Game Statistics:')

            # player 1
            print(f'{player_1_name}')
            print('='*len(player_1_name))
            print(f'Won: {player_1_wins} times')
            print(f'Lost: {player_2_wins} times')
            print(f'Tied {ties} times')

            # player 2
            print(f'{player_2_name}')
            print('='*len(player_2_name))
            print(f'Won: {player_2_wins} times')
            print(f'Lost: {player_1_wins} times')
            print(f'Tied {ties} times')

            # reset stats
            player_1_wins = 0
            ties = 0
            player_2_wins = 0

        keep_playing: str = get_user_input('Continue? (y/n): ', str, ['y', 'n'])
        if keep_playing == 'n':
            break

if __name__=="__main__":
    main()








from ast import get_source_segment
import random
from typing import AsyncIterable
import math

display_greeting = print("Welcome to Rock, Paper, Scissors, Lizard, Spock!!!")


question = input("Would you like to play a game of RPSLS?")
while question != "yes":
    question = input("Please select yes or exit the game. Enter yes to continue: ")
if question == "yes":
    print("Here are the rules for this best 2 out of 3 game:", "\n" "1. Paper beats Rock", "\n" "2. Rock beats Scissors", "\n" "3. Paper covers Rock", "\n" "4. Rock crushes Lizard", "\n" "5. Lizard poisons Spock", "\n" "6. Spock smashes Scissors", "\n" "7. Scissors decapitates Lizard", "\n" "8. Lizard eats Paper", "\n" "9. Paper disproves Spock", "\n" "10. Spock vaporizes Rock", "\n" "Whichever player wins 2 out of 3 games first, wins!")
        

player_mode = input("If you would like to play against the computer please press 1, if you would like to play with another player please select 2!")
while player_mode != "1" and player_mode != "2":
    player_mode = input("Please make a selection from the list...")
if player_mode == "1":
    print("You have selected to play against the computer!")
elif player_mode == "2":
    print("You have choosen to play against another player!")


player_name = input("Player please enter your name: ")
print(f"Let's get ready to rumble {player_name}!!")


def play():
    user =  input("What's your choice? 'ro' for rock, 'pa' for paper, 'sc' for scissors, 'sp' for spock, or 'li' for lizard?" '\n')
    user = user.lower()

    computer = random.choice(['ro', 'pa', 'sc', 'sp', 'li'])

    if user == computer:
        return (0, user, computer)

    if is_win (user, computer):
        return (1, user, computer)

    return (-1, user, computer)


def is_win(player, opponent):
    if (player == 'ro' and opponent == 'sc') or (player == 'sc' and opponent == 'pa') or (player == 'pa' and opponent == 'ro') or (player == 'li' and opponent == 'pa') or (player == 'li' and opponent == 'sp') or (player == 'ro' and opponent == 'li') or (player == 'sp' and opponent == 'sc') or (player == 'sp' and opponent == 'ro'):
        return True
    return False    


def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.cell(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary
        result, user, copmuter = play()

        if result == 0:
            print("It is a tie. You and the computer have both chosen {}. \n.format{user}")

        elif result == 1:    
            print("Great job, you won! You chose {} and the computer chose {}. \n.format{user}{computer}")

        elif result == -1:
            print("You lost, what a shame! You chose {} and the computer trumped you with {}! \n.format{user}{computer}")




# 9. declare winner and give them 1 point
# 10. check scores to see if someone has 2 pts (best 2 of 3)
# 11. if no winner, loop back to step 6 and go again
# 12. if there is a winner, congrats!end game


# Classes:
#    Player-human
#         AI
# Game (game logic here)   
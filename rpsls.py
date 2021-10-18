from ast import get_source_segment
import random
from typing import AsyncIterable


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


player1_gesture = 
# player1_gesture = input("Player, please select your gesture:" , "\n" "Press 1 for Rock", "\n" "Press 2 for Paper", "\n" "Press 3 for Scissors", "\n" "Press 4 for Lizard", "\n" "Press 5 for Spock")
# print("Thank you for your selection!")


# player2_gesture = input("Player, please select your gesture:" , "\n" "Press 1 for Rock", "\n" "Press 2 for Paper", "\n" "Press 3 for Scissors", "\n" "Press 4 for Lizard", "\n" "Press 5 for Spock")
#     print("Thank you for your selection!")




# 8. compare our two gestures
# Rock crushes Scissors 
# Scissors cuts Paper 
# Paper covers Rock 
# Rock crushes Lizard 
# Lizard poisons Spock 
# Spock smashes Scissors 
# Scissors decapitates Lizard
# Lizard eats Paper 
# Paper disproves Spock 
# Spock vaporizes Rock
#    -same thing? no points!
# 

# 9. declare winner and give them 1 point
# 10. check scores to see if someone has 2 pts (best 2 of 3)
# 11. if no winner, loop back to step 6 and go again
# 12. if there is a winner, congrats!end game


# Classes:
#    Player-human
#         AI
# Game (game logic here)   
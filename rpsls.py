import random
import math

display_greeting = print("****!!!Welcome to Rock, Paper, Scissors, Lizard, Spock!!!****")
player_name = input("Hello player! Please enter your name: ")


question = input(f"Would you like to play a game of 'RPSLS' {player_name}? Please enter yes or no: ")
question = question.lower()
while question != "yes":
    question = input("Please select yes or exit the game. Enter 'yes' to continue: ")
if question == "yes":
    print("Here are the rules for this best 2 out of 3 game:", "\n" "1. Paper beats Rock", "\n" "2. Rock beats Scissors", "\n" "3. Paper covers Rock", "\n" "4. Rock crushes Lizard", "\n" "5. Lizard poisons Spock", "\n" "6. Spock smashes Scissors", "\n" "7. Scissors decapitates Lizard", "\n" "8. Lizard eats Paper", "\n" "9. Paper disproves Spock", "\n" "10. Spock vaporizes Rock", "\n" "Whichever player wins 2 out of 3 games first, wins!")
        


def choose_mode():
    player_mode = input("If you would like to play against the computer please enter 1, if you would like to play with another player please enter 2! ")
    while player_mode != "1" and player_mode != "2":
        player_mode = input("Please make a selection from the list by entering 1 or 2...")
    if player_mode == "1":
        print("You have selected to play against the computer!")
        return 1
    elif player_mode == "2":
        print("You have choosen to play against another player!")
        return 2

print(f"Let's get ready to rumble {player_name}!!")




# game mode 1 :user vs computer:
def play():
    user = input("What's your choice? Please enter 'ro' for rock, 'pa' for paper, 'sc' for scissors, 'sp' for spock, or 'li' for lizard?" '\n')
    user = user.lower()

    computer = random.choice(['ro', 'pa', 'sc', 'sp', 'li'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)



def is_win(player, opponent):
    if (player == 'ro' and opponent == 'sc') or (player == 'sc' and opponent == 'pa') or (player == 'pa' and opponent == 'ro') or (player == 'li' and opponent == 'pa') or (player == 'li' and opponent == 'sp') or (player == 'ro' and opponent == 'li') or (player == 'sp' and opponent == 'sc') or (player == 'sp' and opponent == 'ro'):
        return True
    return False    



def play_best_of(z):
    
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(z/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:
            print("It is a tie. You and the computer have both chosen {}.\n".format(user))

        elif result == 1:
            player_wins += 1    
            print("Great job, you won! You chose {} and the computer chose {}.\n".format(user, computer))

        else:
            computer_wins += 1
            print("You lost, what a shame! You chose {} and the computer trumped you with {}!\n".format(user, computer))

    if player_wins > computer_wins:
        print("You have won the best of {} games! Congratulations!".format(z))

    else:
        print("You have lost the best of {} games, how embarrasing! Game over.".format(z))



# game mode 2: user vs user:
class Players:
    def __init__(self, fname):
        self.name = fname



def play_user(p1, p2):

    user1 = input("{} what is your choice? Please enter 'ro' for rock, 'pa' for paper, 'sc' for scissors, 'sp' for spock, or 'li' for lizard?" '\n'.format(p1.name))
    user1 = user1.lower()
    while user1 != 'ro' and user1 != 'sc' and user1 != 'sp' and user1 != 'li' and user1 != 'pa':
        user1 = input("{} please choose from the following options: ''ro' for rock, 'pa' for paper, 'sc' for scissors, 'sp' or spock, or 'li' for lizard" '\n'.format(p1.name))
        user1 = user1.lower()

    user2 = input("{} what is your choice? 'ro' for rock, 'pa' for paper, 'sc' for scissors, 'sp' for spock, 'li' for lizard\n".format(p2.name))
    user2 = user2.lower()
    while user2 != 'ro' and user2 != 'sc' and user2 != 'sp' and user2 != 'li' and user2 != 'pa':
        user2 = input("{} please choose from the following options: 'ro' for rock, 'pa' for paper, 'sc' for scissors, 'sp' for spock, 'li' for lizard\n".format(p2.name))
        user2 = user2.lower()

    if user1 == user2:
        return (0, user1, user2)

    if is_win_user(user1, user2):
        return (1, user1, user2)

    return (-1, user1, user2)



def is_win_user(user1, user2):
    if (user1 == 'ro' and user2 == 'sc') or (user1 == 'sc' and user2  == 'pa') or (user1  == 'pa' and user2  == 'ro') or (user1  == 'li' and user2  == 'pa') or (user1  == 'li' and user2  == 'sp') or (user1  == 'ro' and user2  == 'li') or (user1 == 'sp' and user2  == 'sc') or (user1  == 'sp' and user2  == 'ro') or (user1  == 'pa' and user2 == 'sp'):
        return True
    return False



def play_best_of_three(z, user1_name, user2_name):

    user1_wins = 0
    user2_wins =0
    wins_necessary = math.ceil(z/2)
    while user1_wins < wins_necessary and user2_wins < wins_necessary:
        result, user1, user2 = play_user(user1_name, user2_name)

        if result == 0:
            print("It is a tie. {} and {} have both chosen {}.\n".format(user1_name.name, user2_name.name, user1))

        elif result ==1:
            user1_wins += 1
            print("{} chose {} and {} chose {}. {} wins!!\n".format(user1_name.name, user1, user2_name.name, user2, user1_name.name))

        else:
            user2_wins += 1
            print("{} chose {} and {} chose {}. {} wins!\n".format(user2_name.name, user2, user1_name.name, user1, user2_name.name))


    if user1_wins > user2_wins:
        print("{} has won the best of {} game!! Great job!!\n".format(user1_name.name, z))
    else:
        print("{} has won the best of {} game!! Way to go!!\n".format(user2_name.name, z))


if __name__ == '__main__':
    game_mode = choose_mode()
    if game_mode == 1:
        play_best_of(3)
    elif game_mode ==2:
        player1 = input("Player one please enter your first name: ")
        player2 = input("Player two please enter your first name: ")
        user1 = Players(player1)
        user2 = Players(player2)
        play_best_of_three(3, user1, user2)  
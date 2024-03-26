import random

def welcome_mr_schultze():
    print("Hello Mr. Teacher, welcome to the extremely convoluted and complicated amazing, super game of Rock, Paper, Scissors!")
    print("I am not sorry for your inconvenience")

def get_player_choice():
    while True:
        print("\nChoose your attack:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        try:
            ur_move = int(input("Enter your choice, 1, 2, or 3: "))
            if ur_move not in [1, 2, 3]:
                raise ValueError
            return ur_move
        except ValueError:
            print("Come on, enter something valid, aka, 1, 2, 3")

def get_computer_choice():
    return random.randint(1, 3)

def print_moves(player_move, computer_move):
    moves = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print("Your move:", moves[player_move])
    print("Computer move:", moves[computer_move])

def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (player_move == 1 and computer_move == 3) or \
         (player_move == 2 and computer_move == 1) or \
         (player_move == 3 and computer_move == 2):
        return "player"
    else:
        return "computer"

def print_result(winner):
    if winner == "tie":
        print("It's a tie!!! Now you have to waste your time on another round.")
    elif winner == "player":
        print("You win, wowowowow")
    else:
        print("Computer wins, take the L")


def play_again():
    while True:
        choice = input("You wanna waste your time on another round? (yes or no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def rock_paper_scissors():
    welcome_mr_schultze()
    
    player_wins = 0
    computer_wins = 0
    
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print_moves(player_choice, computer_choice)
        winner = get_winner(player_choice, computer_choice)
        print_result(winner)
        
        if winner == "player":
            player_wins += 1
        elif winner == "computer":
            computer_wins += 1
        print("Scoreboard - You:", player_wins, "Computer:", computer_wins)
        
        if not play_again():
            print("You're done, get wrecked")
            break

rock_paper_scissors()

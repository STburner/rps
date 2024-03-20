import random
def rock_paper_scissors():
    print("Hello Mr. Teacher, welcome to the extremly convoluted and complicated amazing, super game of Rock, Paper, Scissors!")
    print("I am not sorry for your inconvienince")
    while True:
        print("\nChoose your attack:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        ur_move = input("Enter your choice, 1, 2, or 3")
        if ur_move not in ['1', '2', '3']:
            print("Come on, enter something valid, aka, 1, 2, 3")

        ur_move = int(ur_move)
        computer_move = random.randint(1, 3)
        
        print("Ur move:", end=" ")
        if ur_move == 1:
            print("Rock")
        elif ur_move == 2:
            print("Paper")
        else:
            print("Scissors")
        
        print("Computer move:", end=" ")
        if computer_move == 1:
            print("Rock")
        elif computer_move == 2:
            print("Paper")
        else:
            print("Scissors")
        
        if ur_move == computer_move:
            print("It's a tie!!! Now you have to waste your time on another round.")
        elif (ur_move == 1 and computer_move == 3) or \
             (ur_move == 2 and computer_move == 1) or \
             (ur_move == 3 and computer_move == 2):
            print("You win, wowowowow")
        else:
            print("Computer wins, take the L")
        play_again = input("Do you want to play again, yes or no? (please say no)")
        if (play_again.lower()!="yes"):
            print("You're not done yet")
            break

rock_paper_scissors()

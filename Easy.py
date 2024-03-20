import random
choices = ["rock", "paper", "scissors"]
ur_move = input("Enter rock, paper, or scissors: ").lower()
computer_move = random.choice(choices)
if ur_move == computer_move:
    print("All tied up")
elif (ur_move == "rock" and computer_move == "scissors") or (ur_move == "paper" and computer_move == "rock") or (ur_move == "scissors" and computer_move == "paper"):
    print("We have a winner here")
else:
    print("Take the L")
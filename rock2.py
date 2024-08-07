import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True
while play_again:
    
    player_choice = input("\nEnter...\n 1 for Rock,\n 2 for paper, or\n 3 for scissors:\n\n")

    player = int(player_choice) 

    if player < 1 or player > 3:
        sys.exit("press between 1 and 3")

    computer_choice = random.choice("123")


    computer = int(computer_choice)  
    

    print("\nYou chose " + str(RPS(player)).replace('RPS.','' +"."))
    print("\nPython chose " + str(RPS(computer)).replace('RPS.','') + ".")
    

    if player == 1 and computer == 3:
        print("🎉You win!") 
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("🎉You win!")
    elif player == computer:
        print(" 👌. its a draw")     
    else:
        print("🐍Python wins!")  
    play_again = input("\nPlay again? \nY for Yes or\nQ to quit\n\n")

    if play_again.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        play_again = False

sys.exit("Bye! 👋")
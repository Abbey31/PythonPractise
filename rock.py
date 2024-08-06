import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
player_choice = input("Enter...\n 1 for Rock,\n 2 for paper, or\n 3 for scissors:\n\n")

player = int(player_choice) 

if player < 1 or player > 3:
    sys.exit("press between 1 and 3")

computer_choice = random.choice("123")

computer = int(computer_choice)  

print("")
print("You chose " + str(RPS(player)).replace('RPS.','' +"."))
print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

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
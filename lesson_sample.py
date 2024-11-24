import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerchoice = input("Enter...\n1for rock:\n2 for paper: \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1,2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You Chose " + str(RPS(player)).replace('RPS.','') + ".")
print("Python Chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

if player == 1 and computerchoice == 3:
    print("🎉🎉You win!")
elif player == 2 and computerchoice == 1:
    print("🎉🎉You win!")
elif player == 3 and computerchoice == 2:
    print("You win!🎉🎉")
elif player == computer:
    print("😲😲Tie Game!")
else:
    print("🐍 Python wins!") 

    

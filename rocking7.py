import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_game():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        
            
        player_choice = input("\nEnter...\n 1 for Rock,\n 2 for paper, or\n 3 for scissors:\n\n")

        if player_choice not in["1","2","3"]:
            print("You must enter 1,2, or 3.")
            return play_game()

        player = int(player_choice) 

        computer_choice = random.choice("123")


        computer = int(computer_choice)  
        

        print(f"\nYou chose  {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"\nPython chose  {str(RPS(computer)).replace('RPS.','').title()}.")
        
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1 
                return "You win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win"
            elif player == computer:
                return" 👌. its a draw"     
            else:
                python_wins += 1
                return"🐍Python wins!" 
            
        game_result = decide_winner(player,computer)

        print(game_result)
                
        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins:  {str(python_wins)}")

        print("\n Play again?")
        while True:
            play_again = input("\nY for Yes or\nQ to quit\n")
            if play_again.lower() not in ["y","q"]:
                continue 
            else:
                break
        if play_again.lower() == "y":
            return play_game() 
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_game

    
rock_paper_scissors = rps()

if __name__ == "__main__": 
    rock_paper_scissors()



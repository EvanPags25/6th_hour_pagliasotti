#Name:Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def RPS():
    playerNum = int(input("1 for rock 2 for paper 3 for scissors"))
    opponentNum = random.randint(1,3)

    print("Opponent got ", opponentNum)

    if playerNum==1 and opponentNum==3:
        print("you win")
    elif playerNum==1 and opponentNum==2:
        print ("you lost")
    elif playerNum==1 and opponentNum==1:
        print (" you tied")
    elif playerNum == 2 and opponentNum == 1:
        print("you win")
    elif playerNum == 2 and opponentNum == 3:
        print("you lost")
    elif playerNum ==2  and opponentNum == 2:
        print(" you tied")
    elif playerNum==3 and opponentNum==2:
        print("you win")
    elif playerNum==3 and opponentNum==1:
        print ("you lost")
    elif playerNum==3 and opponentNum==3:
        print (" you tied")
    repeat()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def repeat():
    replayInput = input("Would like to play again? Y/N")

    # Note here how you can call the function inside of itself to repeat the code.
    if replayInput == "y":
        RPS()
    else:
        exit()
RPS()

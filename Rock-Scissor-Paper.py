import random
import time
rock = 1
paper = 2
scissors = 3
names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}
player_score = 0
computer_score = 0
def start():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    if play_again() == "y":
        start()
    else: scores()
def move():
    while True:
        print
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 1, 2 or 3.")
def result(player, computer):
    print( "1....")
    time.sleep(1)
    print( "2...")
    time.sleep(1)
    print ("3!")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie game: ")
    else:
        if rules[player] == computer:
            print("Your victory assured")
            player_score += 1
        else:
            print("The computer laughs as you realises you have been defeated.")
            computer_score += 1
def play_again():
    answer = input("Would you like to play again? y/n:")
    if answer in ("y", "n"):
        return answer
    else :
        print("Thank you:")
def scores() :
    global player_score, computer_score
    print()
    print("---*---"*3,"High scores","---*---"*3)
    print("Player Score: ",player_score)
    print("Computer Score ",computer_score)
    if(player_score == computer_score):
        print("Tie! Good luck for next time")
    else :
        if player_score > computer_score:
            print("Hurrah! You won! Congo.")
        else:
            print("You Lose! :) ")
    print()
if __name__ == "__main__":
    start()
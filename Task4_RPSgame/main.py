# .......... STONE PAPER SCISSSORS ...........
import random


user_score = 0
computer_score = 0
rounds = 0


def select_choice():
    global user_score, computer_score, rounds 
    
    print("\nComputer's Turn : Rock(r) , Paper(p) , Scissors(s) ")
    randChoice = random.randint(1,3)
    if randChoice==1:
        comp='r'
    elif randChoice==2:
        comp='p'
    elif randChoice==3:
        comp='s'

    your = input("Your turn : Rock(r) , Paper(p) , Scissors(s) : ")

    if your not in ['r' , 'p' , 's']:
        print("Invalid input ! please enter r, p, or s.")
        return

    choice_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"\nComputer Chose {choice_map[comp]}")
    print(f"You Chose {choice_map[your]}")


    res = game(comp, your)
    rounds += 1

    if res==None:
        print("The Game is Tied!\n")
    elif res:
        print("You Won!\n")
        user_score += 1
    else:
        print("You Lose!\n")
        computer_score +=1

    print(f"Scores after round {rounds} :")
    print(f"You -> {user_score}")
    print(f"Computer -> {computer_score}")

def game(comp,your):
    if comp==your:
        return None
    
    if comp=='r':
        if your == 's':
            return False
        elif your == 'p':
            return True

    if comp=='p':
        if your == 'r':
            return False
        elif your == 's':
            return True

    if comp=='s':
        if your == 'p':
            return False
        elif your == 'r':
            return True
            

print("****** Welcome to Stone Paper Scissors Game! ******")
print("")
print("Instructions: Enter 'r' for Rock, 'p' for Paper, 's' for Scissors.")

while True:
    select_choice()
    play_more = input("\nDo you want to play again? (y/n): ").lower()
    if play_more != 'y':
        print("\nThanks for playing!\n")
        print(f"Final Scores after total {rounds} rounds : ")
        print(f"You -> {user_score}")
        print(f"Computer -> {computer_score}\n")
        break


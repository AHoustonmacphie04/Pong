import random

score = 0

def roll():
    global score  
    dice = random.choice([1, 2, 3, 4, 5, 6])
    if dice == 1:
        print("You Rolled a 1, you lose!")
        score = 0 
    else:
        score += dice
        roll_again = input(f"You rolled a {dice}. Would you like to roll again? (yes/no): ")
        if roll_again.lower() == "yes":
            roll()
        else:
            print(f"Your score is: {score}") 

choice = input("Would you like to roll your dice? (yes/no): ")

if choice.lower() == "yes":
    roll()
    
else:
    print(f"Your  final score is: {score}") 
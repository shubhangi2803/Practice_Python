# Make a two-player Rock-Paper-Scissors game.
# Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game

# Remember the rules:
#  Rock beats scissors
#  Scissors beats paper
#  Paper beats rock

import random

name=input("Enter your name : \n")
p1=0
p2=0
while True:
    P1=input("Rock / Paper / Scissors : ")
    P2=random.choice(['rock','paper','scissors'])
    print("Computer : {}".format(P2))
    if (P1=='rock' and P2=='scissors') or (P1=='scissors' and P2=='paper') or (P1=='paper' and P2=='rock'):
        Win=P1
        p1+=1
    elif (P2=='rock' and P1=='scissors') or (P2=='scissors' and P1=='paper') or (P2=='paper' and P1=='rock'):
        Win=P2
        p2+=1
    else:
        print("No point")
    if p1==3 or p2==3:
        if Win==P1:
            print("----- Congratulations ! You WON !! -----\n")
        else:
            print("----- Oh No ! You loose ! Computer WON !! -----\n")
        choice=None
        while True:
            choice=input("Do you want to start a new game ?  y/n ")
            if choice=='n':
                break
            elif choice=='y':
                name=input("Enter your name : \n")
                p1=0
                p2=0
                break
            else:
                print("Enter valid choice !!")
        if choice=='y':
            continue
        if choice=='n':
            break
    else:
        print("\nPOINTS : ")
        print("{} : {}  ||  Computer : {}\n".format(name,p1,p2))
        continue

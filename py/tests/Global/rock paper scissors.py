import random
tools = ["","rock","paper","scissors"]
round = 0
print("\n\n\n\n")
score = 0
computer_score = 0
usrchoice=""
usr_choice_valid = None
comchoice = ""

while True:
    rounds = input("Recommended to play odd rounds to avoid draws\nEnter number of rounds(max 9): ")
    if rounds.isnumeric():

        if int(rounds)>0 and int(rounds)<=9:
            rounds = int(rounds)
            print("Best of "+str(rounds))
            break
        else:
            print("\nNumber should be from 1 to 9")

    else:
        print("\nThat's not a number!!!")


def declare(u, n):
    dif = u-n
    global computer_score, score
    if dif == -2 or dif==1:
        print(f"\n---You won! (+1) ---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n")
        score = score+1
        return 1,f"\n---You won! (+1) ---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n"
    elif dif == 2 or dif==-1:
        print(f"\n---You lost! (-1) ---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n")
        computer_score = computer_score+1
        return 0,f"\n---You lost! (-1) ---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n"
    elif dif == 0:
        print(f"\n---It's a draw! (+0) ---\nBoth you and computer chose: {usrchoice.capitalize()}\n")
        return 0,f"\n---It's a draw! (+0) ---\nBoth you and computer chose: {usrchoice.capitalize()}\n"
    else:
        print("\n---Good job, you found a bug 👏👏👏, restart the program and report the bug---\n")
        return 0.1,"\n---Good job, you found a bug 👏👏👏, restart program and report it---\n"


def take_choice():
    global comchoice
    global usrchoice
    global usr_choice_valid
    usr_choice_valid = None #Clear the value of a variable 
    u=0
    n=0
    n = random.randint(1,3)
    print(f"---Round: {round+1}---")
    comchoice = tools[n].capitalize()
    print('\nOptions(Enter number letter or word):\n1. Rock(r,R)\n2. Paper(p,P)\n3. Scissors(s,S)')
    usrinp = input("\nInput your choice: ").lower()
    if usrinp == "1" or usrinp =="rock" or usrinp =="r" or usrinp =="R":
        u = 1
    elif usrinp == "2" or usrinp =="paper" or usrinp =="p" or usrinp =="P":
        u = 2
    elif usrinp == "3" or usrinp =="scissor" or usrinp=="scissors" or usrinp =="s" or usrinp =="S":
        u = 3
    else:
        print("Enter a valid input(Enter number letter or word):\n1. Rock(r,R)\n2. Paper(p,P)\n3. Scissors(s,S)")
        usr_choice_valid = False


    if usr_choice_valid!=False:
        usrchoice = tools[u].capitalize()
        declare(u,n)
        print(f"Your score: {score}         Computer score: {computer_score}\n")

    usrchoice = tools[u].capitalize()

    while True:
        conf=input("Enter 'y' to proceed to next round/result: ")
        if conf=="y":
            break
        else:
            print("")



for round in range(int(rounds)):
    ""

if score > computer_score:
    print(f"---You won! ({score}:{computer_score})---")
elif score < computer_score:
    print(f"---You lost! ({score}:{computer_score})---")
elif score == computer_score:
    print(f"---It's a draw! ({score}:{computer_score})---(Play odd rounds to avoid draws)\n")
else:
    print("🙏 No idea what just happened")



#def show_scorecard(rounds=0,u=0,n=0):
#
#    #add_score=declare(u,n)[0]
#    #print (add_score)
#    print("\n\n\n\n\n\n\n\n\n")
#    print(f'''----------------------------------------------------------------
#          
#                    You are playing best of []
#
#                          ---Round: {round}---
#You: {score}                                               Computer: {computer_score}
#
#
#''')
#    if usr_choice_valid != False:
#        take_choice()
#    else:
#        print('''                        Make your choice:
#                         -Rock (1,R,r)
#                         -Paper (2,P,p)
#                         -Scissors (3,S,s)''')
#    
#    print (f'''
#
#You: {usrchoice.capitalize()}                                         Computer: {comchoice.capitalize()}
#''')
#
#
#show_scorecard()
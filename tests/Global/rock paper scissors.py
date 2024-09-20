import random
tools = ["","rock","paper","scissors"]
usr_has_entered = True
round = 0
print("\n\n\n\n")
score = 0
computer_score = 0

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
    det = u-n
    global computer_score, score
    if det == -2 or det==1:
        print(f"\n---You won! (+1) ---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n")
        score = score+1
        return 1
    elif det == 2 or det==-1:
        print(f"\n---You lost! (-1) ---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n")
        computer_score = computer_score+1
        return 0
    elif det == 0:
        print(f"\n---It's a draw! (+0) ---\nBoth you and computer chose: {usrchoice.capitalize()}\n")
        return 0
    else:
        print("\n---Good job, you found a bug 👏👏👏, restart program and report it---\n")
        return 0.1


for round in range(int(rounds)):
    inp_valid = None
    u=0
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
        inp_valid = False


    if inp_valid!=False:
        usrchoice = tools[u].capitalize()
        declare(u,n)
        print(f"Your score: {score}         Computer score: {computer_score}\n")

    usrchoice = tools[u].capitalize

    while True:
        conf=input("Enter 'y' to proceed to next round/result: ")
        if conf=="y":
            break
        else:
            print("")

if score > computer_score:
    print(f"---You won! ({score}:{computer_score})---")
elif score < computer_score:
    print(f"---You lost! ({score}:{computer_score})---")
elif score == computer_score:
    print(f"---It's a draw! ({score}:{computer_score})---(Play odd rounds to avoid draws)\n")
else:
    print("🙏 No idea what just happened")


import random
tools = ["","rock","paper","scissors"]
usr_has_entered = True
round = 0
print("\n\n\n\n")
score = 0

while True:
    rounds = input("Recommended to enter an odd number to avoid draws\nEnter number of rounds(max 9): ")
    if rounds.isnumeric():

        if int(rounds)>0 and int(rounds)<9:
            rounds = int(rounds)
            print("Best of "+str(rounds))
            break
        else:
            print("\nNumber should be from 1 to 9")

    else:
        print("\nThat's not a number!!!")


def declare(u, n):
    det = u-n
    if det == -2 or det==1:
        print(f"\n---You won!---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n")
        return 1
    elif det == 2 or det==-1:
        print(f"\n---You lost!---\nYour choice: {usrchoice.capitalize()}\nComputer's choice: {comchoice.capitalize()}\n")
        return -1
    elif det == 0:
        print(f"\n---It's a draw!---\nBoth you and computer chose: {usrchoice.capitalize()}\n")
        return 1
    else:
        print("\n---Good job, you found a bug 👏👏👏, restart program and report it---\n")
        return 0.1


for round in range(int(rounds)):
    u=0
    n = random.randint(1,3)
    print(f"---Round: {round+1}---")
    comchoice = tools[n]
    print('\nOptions(Enter number letter or word):\n1. Rock(r,R)\n2. Paper(p,P)\n3. Scissors(s,S)')
    usrinp = input("\nInput your choice: ").lower()
    if usrinp == "1" or usrinp =="rock" or usrinp =="r" or usrinp =="R":
        u = 1
        usrchoice = tools[u]
        score = score+declare(u,n)
    elif usrinp == "2" or usrinp =="paper" or usrinp =="p" or usrinp =="P":
        u = 2
        usrchoice = tools[u]
        score = score+declare(u,n)
    elif usrinp == "3" or usrinp =="scissor" or usrinp=="scissors" or usrinp =="s" or usrinp =="S":
        u = 3
        usrchoice = tools[u]
        score = score+declare(u,n)
    else:
        print("Enter a valid input(Enter number letter or word):\n1. Rock(r,R)\n2. Paper(p,P)\n3. Scissors(s,S)")

    usrchoice = tools[u]

    while True:
        conf=input("Enter 'y' to proceed to next round/result: ")
        if conf=="y":
            break
        else:
            print("")

if score > 0:
    print(f"---You won! ({score}/{rounds})---")
elif score < 0:
    print(f"---You lost! ({score}/{rounds})---")
elif score == 0:
    print(f"---It's a draw! ({score}/{rounds})---(Play odd rounds to avoid draws)\n")
else:
    print("🙏 No idea what just happened")


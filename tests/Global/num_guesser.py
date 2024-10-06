import random


print("\n\n\n")
print("Guess a random integer from -10 to 10")


ans = random.randint(-10,10)
#print (ans) #remove first hash only to get the right answer printed at the beginning for debug


def getinput():
    guess = input("Enter guess: ")
    return guess


def checkvalid(guess):
    if guess.isnumeric() or (guess[0]=="-" and guess[1:].isnumeric()): #first condition to check for positive and second for negative
        if int(guess) in range(-10,11):
            valid = True
        else:
            print("-------------------------------------\nOnly enter an integer from -10 to 10\n-------------------------------------")
            valid = False
    else:
        print("-------------------------------------\nOnly enter an integer from -10 to 10\n-------------------------------------")
        valid = False
    return valid


def checkans(valid, guess, ans):
    if valid == True:
        if int(guess) > ans:
            print("---------------------------\nYour guess was higher than the answer, try again\n---------------------------")
            ansisright = False
        elif int(guess) < ans:
            print("---------------------------\nYour guess was lower than the answer, try again\n---------------------------")
            ansisright = False
        elif int(guess)==ans:
            ansisright = True
        else:
            ansisright = False
    else:
        ansisright = False
    return ansisright


valid = False
ansisright = False


while valid == False or ansisright == False:
    guess = getinput()
    valid = checkvalid(guess)
    ansisright = checkans(valid, guess, ans)


print(f"\n---------------------------\nYou guessed it! It was {ans}\n---------------------------\n")



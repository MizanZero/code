import random

inp_is_valid = False
inp_is_correct = False

print("\n\n\n")


print("Guess a random integer from -10 to 10")

guess = ""
ans = random.randint(-10,10)
#print (ans) #remove first hash only to get the right answer printed at the beginning for debug

while inp_is_valid == False or inp_is_correct == False:
    guess = input("Enter guess: ")
    if guess.isnumeric() or guess.replace("-","").isnumeric():
        inp_is_valid = True

        if int(guess) in range(-10,11):

            if int(guess)>ans:
                print("Your guess was higher than the answer, try again")
            elif int(guess)<ans:
                print("Your guess was lower than the answer, try again")
            else:
                print(f"You guessed it. It was {ans}")
                inp_is_correct = True
        else:
            print("Only enter an integer from -10 to 10")

    else:
        print("Only enter an integer from -10 to 10")


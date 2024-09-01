import random

c_set = ["Spades", "Clubs", "Hearts", "Diamonds"]
c_type = [2,3,4,5,6,7,8,9,10,"A","K","Q","J"]


def r_card():
    type = input("String or Tuple?")
    r1 = int(random.randint(0,12))
    r2 = int(random.randint(0,3))
    if type.lower() == "string":
        return str(c_type[random.randint(0,12)]) + " of " + str(c_set[random.randint(0,3)])
    else:
        return [r1, r2, c_type[r1], c_set[r2]]
    
print(r_card())
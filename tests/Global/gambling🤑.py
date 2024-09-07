import random


def roll_dice():
    return random.radint(1,6)


class player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

nplayers_is_valid = False

while True:
    nplayers = input("Enter the number of players(Maximum 10): ")
    if nplayers.isdigit():
        if int(nplayers) <= 10:
            nplayers = int(nplayers)
            nplayers_is_valid = True
            break
        else:
            ""
    else:
        ""

ent_score = ""

while ent_score<50:
    should_roll = input("Do you want to roll(Enter 'y' for yes): ")
    if should_roll.lower() != "y":
        break
    dice = roll_dice()
    
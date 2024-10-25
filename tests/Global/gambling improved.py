import random


def roll_dice():
    return random.randint(1,6)


nplayers_is_valid = False

while True: #hint: checkhow break has been used here in this loop
    nplayers = input("\nEnter the number of players(Maximum 10): ")
    if nplayers.isdigit():
        if int(nplayers) <= 10:
            nplayers = int(nplayers)
            nplayers_is_valid = True
            break


scores = [0 for _ in range(nplayers)]
print (nplayers)

current_player = 1


while scores[(current_player-1)]<50 and current_player <= nplayers:
    
    dice = 0
    should_roll = input("Do you want to roll(Enter 'y' to roll): ")

    if should_roll.lower()!='y': #hint: good usage of break
        #print(current_player)
        if current_player < nplayers:
            current_player+=1
            print (f"\nYou ended your turn--- You scored: {scores[current_player-1]}\nPlease pass to the next player")
        else:
            print(f"\nYou ended your turn--- You scored: {scores[current_player-1]}\nPlease pass to the next player")
            break
        
        dice = 0
    else:
        dice = roll_dice()
        print(f"You rolled {dice}")
        scores[current_player-1] +=dice
    if dice == 1:
        scores[current_player-1]=0
        current_player = current_player + 1
        #print(current_player)
        print(f"\nEliminated ---You rolled a One. Your score is 0\nPlease pass to the next player\n"+"")

    elif dice == 0:
        ""
    else:
        scores[current_player-1]+=dice
        #print(current_player)
        
    #print(scores)


for _ in range(len(scores)):
    print(f"\nPlayer {_+1} scored {scores[_]}")

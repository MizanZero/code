

import random

comp_role=0
player_role=0
oddstr = ["o","od","odd","oddd","d"]
evestr = ["e","even","ven","en","v","n"]

while True:
 oddoreve= input("Odd or even: ")
 if (oddoreve in oddstr):
  usrodd = True
  break

 elif oddoreve in evestr:
  usrodd = False
  break
 
 else:
  print ("Congrats for breaking the program, you won NOTHING 😂")
  exit(code=0)
 
  


while True:
 oddeve = ("Enter natural number for odd or even (max 10): ")
 
#oddoreve.lower() in oddstr) or #(oddoreve.lower() in evestr)

 if oddeve.isnumeric():
  if int(oddeve)<=10:
   break
   

com_oddeve=random.randint(1,10)
print(f"Computer chose: {com_oddeve}")
isEven = (com_oddeve+oddeve).isEven()










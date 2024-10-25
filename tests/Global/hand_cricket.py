

def input(inpmsg):
 inp = input(inpmsg)
 return inp.isnumeric(),inp
 

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
  print ("Congrats for breaking the program, your reward is 🎉NOTHING🎉 😂")
  exit(code=0)




while True:
 oddeve = input("Enter natural number for odd or even (max 10): ")
 
#oddoreve.lower() in oddstr) or #(oddoreve.lower() in evestr)

 if oddeve.isnumeric():
  if int(oddeve)<=10:
   oddeve = int(oddeve)
   break
   

com_oddeve=random.randint(1,10)
print(f"Computer chose: {com_oddeve}")


if oddeve%2 == 0:
 iseven = True
else:
 iseven = False


if usrodd and iseven:
 print(f"{com_oddeve}+{oddeve} = {com_oddeve+oddeve}. Computer will chose.")
 bias_list = [0,0,0,0,1]
 comp_role = bias_list[random.randint(len(bias_list))]
 print (comp_role)
 exit(code=0)
 player_role = 1-comp_role
 
 if comp_role==0:
  print("Computer chose to bat")
elif comp_role==1:
 print("Computer chose to bowl")


usrthrow = 0, compthrow = 0
usrlist=[0,0,0,0,0,0]

while usrthrow != compthrow:
 compthrow = random.randint(1,10)
 while 


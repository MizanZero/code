
import random

def getInput(inpmsg):
 inp = input(inpmsg)
 return inp.isnumeric(),inp
 



def updateScores(out="notout",u=0,c=0):

 if out == "out":
  if comRole==0:
    usrScore += u
  else:
    comScore += c
 
 else:
  if comRole==0:
    compScore += c
  else:
    usrScore += u

  return usrScore,comScore



usrScore,comScore = 0,0
comRole=0
usrRole=0
oddList = ["o","od","odd","oddd","d","1","11"]
eveList = ["e","even","ven","en","v","n","2","22"]
bias_list = [0,0,0,0,1]
outMsg = {
  0:"You lost a wicket!",
  1:"You took a wicket!"
}


while True:
 oddoreve= input("Odd or even: ") 
 if (oddoreve in oddList):
  usrOdd = True 
  break

 elif oddoreve in eveList:
  usrOdd = False
  break
 
 else:
  print ("Please enter odd or even")





while True:
 oddeve = input("Enter natural number for odd or even (max 10): ")
 
#oddoreve.lower() in oddstr) or #(oddoreve.lower() in evestr)

 if oddeve.isnumeric():
  if int(oddeve)<=10:
   oddeve = int(oddeve)
   break
   

com_oddeve=random.randint(1,10)
print(f"Computer chose: {com_oddeve}")


if (com_oddeve+oddeve)%2 == 0:
 iseven = True
else:
 iseven = False




if usrOdd and iseven:
 print(f"{com_oddeve}+{oddeve} = {com_oddeve+oddeve}. Computer will chose.")
 comRole = bias_list[random.randint(0, len(bias_list)-1)]
 print (comRole)
 #exit(code=0)
 usrRole = 1-comRole
 
 if comRole==0:
  print("Computer chose to bat")
 elif comRole==1:
  print("Computer chose to bowl")

else:
  print(f"{com_oddeve}+{oddeve} = {com_oddeve+oddeve}")
  while True:
   batorbowl = input("Enter Bat or Bowl: ")
 
   if batorbowl.lower() in ["bat","ba","at"]:
    usrRole = 0
    comRole = 1
    print ("You chose to bat")
    print()
    break
 
   elif batorbowl.lower() in ["bowl", "bo", "ow", "owl", "wl"]:
    usrRole=1
    comRole=0
    print("You chose to bowl")
    print()
    break



usrThrow = 0
compThrow = 0
usrlist=[0,0,0,0,0,0]


def match():
 compThrow = random.randint(1,10)
 usrThrow = input("Throw your number: ")
 
 while not usrThrow.isnumeric():
  usrThrow = input("Throw your number: ")
  if int(usrThrow) <= 10:
   usrThrow = int(usrThrow)
   if usrThrow == compThrow:
     print(outMsg[usrRole])
     usrScore+=updateScores("out",usrThrow,compThrow)[0]
   else:
     comScore+=updateScores("notout",usrThrow,compThrow)[1]



match() 


if usrScore>comScore:
 bat = "computer"
else:
 bat = "player"


usrRole, comRole = comRole, usrRole


match() 
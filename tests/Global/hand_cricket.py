
import random

def getInput(inpmsg):
 inp = getInput(inpmsg)
 return inp.isnumeric(),inp
 



def updateScores(out="notout",u=0,c=0):

 if out == "out":
  if comp_role==0:
    usrScore += u
  else:
    comScore += c
 
 else:
  if comp_role==0:
    compScore += c
  else:
    usrScore += u

  return usrScore,comScore



usrScore,comScore = 0,0
comp_role=0
player_role=0
oddList = ["o","od","odd","oddd","d","1","11"]
eveList = ["e","even","ven","en","v","n","2","22"]
bias_list = [0,0,0,0,1]
outMsg = {
  0:"You lost a wicket!",
  1:"You took a wicket!"
}


while True:
 oddoreve= getInput("Odd or even: ") 
 if (oddoreve in oddList):
  usrOdd = True 
  break

 elif oddoreve in eveList:
  usrOdd = False
  break
 
 else:
  print ("Congrats for breaking the program, your reward is 🎉NOTHING🎉")
  exit(code=0) 





while True:
 oddeve = getInput("Enter natural number for odd or even (max 10): ")
 
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




if usrOdd and iseven:
 print(f"{com_oddeve}+{oddeve} = {com_oddeve+oddeve}. Computer will chose.")
 comp_role = bias_list[random.randint(len(bias_list))]
 print (comp_role)
 exit(code=0)
 player_role = 1-comp_role
 
 if comp_role==0:
  print("Computer chose to bat")
 elif comp_role==1:
  print("Computer chose to bowl")



usrThrow = 0, compThrow = 0
usrlist=[0,0,0,0,0,0]



compThrow = random.randint(1,10)
usrThrow = getInput("Throw your number: ")

while not getInput("Throw your number: ")[0]:
 usrThrow = getInput("Throw your number: ")
 if usrThrow[0]:
  if int(usrThrow) <= 10:
   usrThrow = int(usrThrow)
   if usrThrow == compThrow:
     print(outMsg[player_role])
     updateScores("out",usrThrow,compThrow)
   else:
     updateScores("notout",usrThrow,compThrow)

  
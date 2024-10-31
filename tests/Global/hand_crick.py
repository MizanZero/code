import random 

oddList = ["odd","od","dd","do","o","d"] 
eveList = ["even","eve","ven","eve",'ev','ve','e'] 
batList=['batting','bat']
bowlList=['bowl','ball','bal']
biasList=[0,0,0,0,1] 


def inp(inpMsg):
    inp=input(inpMsg) 
    return inp,inp.isnumeric() #return user enter and bool for numeric


def isOut(p,c):
    return False if p==c else True 


def controlledInp(l1,l2,r1,r2,takeInt,inpMsg,warning=""):
    if takeInt:
        inp = inp(inpMsg) 
        while True:
            inp=inp(inpMsg) 
            if inp[1]:
                inp = int(inp) 
            else:
                print(warning)
    while True:
        inp=input(inpMsg).lower() 
        if inp in l1:
            return r1,inp.isnumeric() #return desired return val,bool for numeric
        elif inp in l2:
            return r2,inp.isnumeric() #same 
        else:
            print(warning)





def throw():
    [usrThrow,usrNum]=inp("Throw a number: ")[0:2] 
    return usrThrow,usrNum,random.randint(1,10) #return usr value, boolean for numeric, and a random from 1 to 10


oddOrEve = controlledInp(eveList,oddList,'eve','odd',False,"Enter Odd or Eve: ") 
if oddOrEve == 'eve':
    oddOrEve='eve'
else:
    oddOrEve='odd'



oddEve=controlledInp(oddList,eveList,'odd','eve',True,"Enter a number for Odd or Eve(max: 10): ",'Only enter odd or eve(max: 10)')
print (oddEve) #debug statement 

if oddEve[1]:
    if int(oddEve[1]) in range(1,11):
        oddEve = int(oddEve[0])
        com_oddOrEve=random.randint(1,10)
        print (com_oddOrEve,oddEve)
        if (com_oddOrEve+oddEve)%2==0 and oddEve=='eve':
            batOrBowl=inp('You won, enter Bat or Ball: ')
        elif (com_oddOrEve+oddEve)%2==1 and oddEve=='odd':
            batOrBowl=inp('You won, enter Bat or Ball: ')



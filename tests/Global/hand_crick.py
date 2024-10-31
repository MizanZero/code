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


def controlledInp(l1,l2,r1,r2,dataType,inpMsg,warning=""):
    
    if dataType=='int':
        while True:
            takeInp=inp(inpMsg)
            takeInp=list(takeInp) #takes input
            if takeInp[1]: 
                takeInp[0] = int(takeInp[0]) 
                break 
            else:
                print(warning,"first loop in contrInp") 
    else:
        takeInp=inp(inpMsg)
        takeInp=list(takeInp) #takes input
    while True:
        if takeInp[0] in l1:
            return r1,takeInp[1] #return desired return val,bool for numeric
        elif takeInp[0] in l2:
            return r2,takeInp[1] #same 
        else:
            print(warning,"second loop in contrInp")




def throw():
    [usrThrow,usrNum]=inp("Throw a number: ")[0:2] 
    return usrThrow,usrNum,random.randint(1,10) #return usr value, boolean for numeric, and a random from 1 to 10


oddOrEve = controlledInp(eveList,oddList,'eve','odd',False,"Enter Odd or Eve: ") 


oddEve=controlledInp(range(1,10,2),range(2,10,2),'odd','eve','int',"Enter a number for Odd or Eve(max: 10): ",'Only enter odd or eve(max: 10)')
# tf does the above do?
print (oddEve) #debug statement 


#change the below blocks they are double checking 
if oddEve[1]:
    if int(oddEve[0]) in range(1,11):
        oddEve = int(oddEve[0]) 
        com_oddOrEve=random.randint(1,10) 
        print (com_oddOrEve,oddEve) 
        if (com_oddOrEve+oddEve)%2==0 and oddEve=='eve':
            batOrBowl=inp('You won, enter Bat or Ball: ') 
        elif (com_oddOrEve+oddEve)%2==1 and oddEve=='odd':
            batOrBowl=inp('You won, enter Bat or Ball: ') 














import random 

oddList = ["odd","od","dd","do","o","d"] 
eveList = ["even","eve","ven","eve",'ev','ve','e'] 
batList=['batting','bat']
bowlList=['bowl','ball','bal']
biasList=['bat','bat','bat','bat','bowl'] 
batScore=0
comScore=0
usrScore=0
score = {'usrScore':0, 'comScore':0}



def inp(inpMsg):
    inp=input(inpMsg) 
    return inp,inp.isnumeric() #return user enter and bool for numeric


def outOrNot(p,c):
    return True if p==c else False 


def controlledInp(l1,l2,r1,r2,dataType,inpMsg,warning=""):
    
    if dataType=='int':
        while True:
            takeInp=inp(inpMsg)
            takeInp=list(takeInp) #takes input
            if takeInp[1]: 
                takeInp[0] = int(takeInp[0]) 
                return takeInp[0]
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




def throw(roleMsg):
    print(roleMsg)
    usrNum=controlledInp(range(1,11),range(1,11),'','','int',"Throw a number: ") 
    return usrNum,random.randint(1,10) #return usr value, boolean for numeric, and a random from 1 to 10



def switch():
    if batting=='usr':
        batting='com'
    else:
        batting='usr'


oddOrEve = controlledInp(eveList,oddList,'eve','odd',False,"Enter Odd or Eve: ") 


oddEveVal=controlledInp(range(1,10,2),range(2,10,2),'odd','eve','int',"Enter a number for Odd or Eve(max: 10): ",'Only enter odd or eve(max: 10)')
print (oddEveVal) #debug statement 

#check if odd or eve
checkOddEveVal=oddEveVal+random.randint(1,10) #sum to check for oddeve
if (checkOddEveVal%2==0 and oddOrEve=='eve') or (checkOddEveVal%2==1 and oddOrEve=='odd'):
    usrWillChoose = True
else:
    usrWillChoose=False


#if usr won oddEve ask for bat or ball
if usrWillChoose:
    batting=controlledInp(batList,bowlList,'usr','com','notInt',"Batting or Bowling: ","Enter a valid choice!\n")
else:
    batting=random.choice(biasList)


isNotOut=True
teamsBowled = 0




def easyMatch():
    if batting == 'usr':
        roleMsg = "You are batting"
    else:
        roleMsg="You are bowling"
    global batScore
    global isNotOut
    global teamsBowled
    while isNotOut and batScore<=50 and teamsBowled!=2:
        [batThrow,bowlThrow]=throw(roleMsg) 
        isNotOut=outOrNot(batThrow,bowlThrow)
        batScore+=batThrow 
    score[batting+'Score'] = batScore
    teamsBowled = teamsBowled+1
    return batScore if teamsBowled==2 else easyMatch()

easyMatch()


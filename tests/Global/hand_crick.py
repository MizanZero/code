import random

print()

oddList = ["odd","od","dd","do","o","d"] 
eveList = ["even","eve","ven","eve",'ev','ve','e'] 
batList = ['batting','bat','at','att','atting','ting','tting']
bowlList= ['bowl','ball','bal','owl','all','al']
biasList= [0,0,0,0,1] 
batScore=0
comScore=0
usrScore=0
score = {'usrScore':0, 'comScore':0}



def inp(inpMsg,dataType='',warning=""): #return integer if required else return input as it is
    inp=input(inpMsg) 
    if dataType!='int':
        return inp
    elif dataType=='int' and not inp.isnumeric():
        print()
        print(warning)
        inp = input(inpMsg)
    elif dataType=='int' and inp.isnumeric():
        return int(inp)


def outOrNot(p,c): #invalid for -1 invalid2 for any other invalid, True for out, False for not out
    if -1 in [p,c]:
        return 'invalid'
    elif p!=c: 
        return True 
    elif p==c:
        declareOut(batting)
        return False 
    else:
        return 'invalid2'

def decide(l1,l2,r1,r2,dataType,inpMsg,warning=""): #return input, r1 
    while True:
        takeInp=inp(inpMsg,dataType,warning)
        if takeInp in l1:
            return takeInp, r1
        elif takeInp in l2:
            return takeInp, r2
        else:
            print()
            print(warning)



def throw(roleMsg):
    usrThrow=decide(range(1,11),range(1,11),'','','int',"Throw a number: ")[0] #take an integer input from 1 to 10
    return usrThrow,random.randint(1,10) #return usr value, and a random from 1 to 10



def switchRole(batting):
    global usrRole
    global comRole
    if batting=='usr':
        batting='com' 
        usrRole='bowl' 
        comRole='bat' 
    else:
        batting='usr' 
        usrRole='bat' 
        comRole='bowl' 




oddOrEve = decide(eveList,oddList,'eve','odd','',"Enter Odd or Eve: ","Only enter Odd or Eve!")[1]  #stores odd or eve 
#print (oddOrEve) #debug statement


oddEveVal=decide(range(1,10,2),range(2,10,2),'odd','eve','int',"Enter a number for Odd or Eve(max: 10): ","Only enter a natural number(max: 10)")
oddEveVal=oddEveVal[0] 
#print (oddEveVal) #debug statement 

#check if odd or eve 
comOddEveVal = random.randint(1,10)
checkOddEveVal=oddEveVal+comOddEveVal #sum to check for oddeve 
if (checkOddEveVal%2==0 and oddOrEve=='eve') or (checkOddEveVal%2==1 and oddOrEve=='odd'):
    usrWillChoose = True
else:
    usrWillChoose=False


#if usr won oddEve ask for bat or ball 
if usrWillChoose:
    print(oddEveVal,'+',comOddEveVal,'=',oddEveVal+comOddEveVal,"\nYou can choose") 
    batting=decide(batList,bowlList,'usr','com','notInt',"Batting or Bowling: ","Enter a valid choice!\n")[1] #batting takes usr or com
else:
    batting=random.choice(['com' for x in biasList if x==0]+['usr']) #computer chooses
    print(oddEveVal,'+',comOddEveVal,'=',oddEveVal+comOddEveVal,"\nComputer's choice") 


if batting == 'com':
    comRole='bat'
    usrRole = 'bowl'
else:
    comRole='bowl'
    usrRole='bat'
print("Coumputer chose to",comRole)


#defining user and computer roles 
if usrRole=='bat':
    roleMsg="You are batting"
else:
    roleMsg="You are bowling"

isNotOut=True
inning = 1



def declareOut(batting):
    return "You took a wicket!" if batting == 'com' else "You lost a  wicket!"

thrown={'usr':0,'com':0}  #stores number thrown 

totalInnings = 2

def easyMatch():
    isNotOut=True 
    for inning in range(1,totalInnings+1): 
        while isNotOut:
            print('Inning:',inning,'|','Total innnigs:',totalInnings) 
            print(roleMsg) 
            score[batting+'Score']+=thrown[batting] 
            thrown['usr'],thrown['com']=throw(roleMsg) 
            isNotOut=outOrNot(thrown['usr'],thrown['com']) 

        switchRole(batting) 


easyMatch() 

def declareResult():
    if score['usrScore'] > score['comScore']:
        print("You won!\n",score['usrScore'],":",score['comScore']) 
    elif score['usrScore'] < score['comScore']:
        print("You lost!\n",score['usrScore'],":",score['comScore']) 

    else:
        print("Close Game! It was a tie!",score['comScore']) 

declareResult() 
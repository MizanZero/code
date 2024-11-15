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
finalScore={'com':-1,'usr':-1}


def checkInp(inpMsg,dataType='',warning=""): #return integer if required else return input as it is
    while True:
        inp=input(inpMsg) 
        if dataType != 'int':
            return inp
        elif dataType=='int' and inp.isnumeric():
            return int(inp) 
        else:
            print(warning+'\n')


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
        inp=checkInp(inpMsg,dataType,warning)
        if inp in l1:
            return inp,r1
        elif inp in l2:
            return inp,r2
        else:
            print(warning)




def throw(roleMsg):
    usrThrow=decide(range(1,11),range(1,11),'','','int',"Throw a number: ")[0] #take an integer input from 1 to 10
    return usrThrow,random.randint(1,10) #return usr value, and a random from 1 to 10


def switchRole(inning): 
    global usrRole
    global comRole
    global roleMsg
    global batting

    if batting=='usr': 
        batting='com' 
        usrRole='bowl' 
        comRole='bat' 
        if score[batting+'Score']<100 and inning<totalInnings: 
            print("\n\n=====YOU got BOWLED. You are now bowling=====") 
        roleMsg = "You are bowling" 
    else:
        batting='usr' 
        usrRole='bat' 
        comRole='bowl' 
        if score[batting+'Score']<100 and inning<totalInnings: 
            print("\n\n=====You BOWLED the computer. You are now batting=====") 
        roleMsg = "You are batting" 
        



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
    batting=decide(batList,bowlList,'usr','com','notInt',"Batting or Bowling: ","Enter a valid choice!\n")[1] #batting stores usr or com
else:
    batting=random.choice(['com' for x in biasList if x==0]+['usr']) #computer chooses
    print(oddEveVal,'+',comOddEveVal,'=',oddEveVal+comOddEveVal,"\n\nYou lost")


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
    global score
    global thrown
    isNotOut=True 
    for inning in range(1,totalInnings+1): 
        while isNotOut: 
            if score[batting+'Score']>=100:
                print("CENTURY!") 
                break
            else: 
                print() 
                print('Inning:',inning,'|','Total innnigs:',totalInnings) 
                print(roleMsg) 
                score[batting+'Score']+=thrown[batting] 
                print("Batsman score(total):",score[batting+'Score']) 
                [thrown['usr'],thrown['com']]=throw(roleMsg) 
                print("Computer:",thrown['com']) 
                isNotOut=outOrNot(thrown['usr'],thrown['com']) 
        finalScore[batting]=score[batting+'Score']
        score={x:0 for x in score.keys()} 
        isNotOut=True 
        inning+=1 
        thrown={x:0 for x in thrown.keys()} 
        switchRole(inning-1) 
        print() 



easyMatch() 

def declareResult():
    if finalScore['usr'] > finalScore['com']: 
        print("You won!\n",finalScore['usr'],":",finalScore['com']) 
    elif finalScore['usr'] < finalScore['com']:
        print("You lost!\n",finalScore['usr'],":",finalScore['com']) 

    else:
        print("Close Game! It was a tie!",finalScore['com']) 

declareResult()



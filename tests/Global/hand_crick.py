import random 

oddList = ["odd","od","dd","do","o","d"] 
eveList = ["even","ven","eve",'ev','ve','e'] 
battingList=[0,0,0,0,1] 


def inp(inpMsg):
    inp=input(inpMsg) 
    return inp,inp.isnumeric() 


def outOrNot(p,c):
    return False if p==c else True 


def oddOrEve():
    while True:
        oddOrEve=inp("Enter Odd or Even: ")[0].lower() 
        if oddOrEve in eveList:
            return 'eve'
        elif oddOrEve in oddList:
            return 'odd'


def throw():
    [usrThrow,usrNum]=inp("Throw a number: ")[0:2] 
    return usrThrow,usrNum,random.randint(1,10) 



if oddOrEve() == 'eve':
    oddOrEve='eve'
else:
    oddOrEve='odd'


oddEve=inp("Enter a number for Odd or Eve: ")
if oddEve[1]:
    oddEve = int(oddEve[0])
    if (throw(2)+oddEve)%2 == 0 and :
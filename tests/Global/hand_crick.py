import random

oddList = ["odd","od","dd","do","o","d"]
eveList = ["eve",'ev','ve','e']

def inp(inpMsg):
    inp=input(inpMsg)
    return inp,inp.isnumeric()

def oddOrEve():
    oddOrEve=inp("Enter Odd or Even: ")[0].lower()
    if oddOrEve in eveList:
        return 'odd'
    elif oddOrEve in oddList:
        return 'eve'

def match():
    [usrThrow,usrNum]=inp("Throw a number: ")[0:2]
    return usrThrow

print(match())




from functionality import *

batIndex=[]; bowlIndex=[]; fieldIndex=[]
for p in players:
    if p.role==Role.field: fieldIndex.append(p.index)
    elif p.role==Role.bat: batIndex.append(p.index)
    elif p.role==Role.bowl: bowlIndex.append(p.index)

if len(batIndex)>1: raise Exception("There are multiple batsmen")
elif len(batIndex)==0: raise Exception("There are no batsmen")

if len(bowlIndex)>1: raise Exception("There are multiple bowlers")
elif len(bowlIndex)==0: raise Exception("There are no bowlers")

batIndex=batIndex[0]; bowlIndex=bowlIndex[0] 


while True:
 try:
     day = int(input("Enter days: "))
     break
 except:
     print("Please enter a whole number")
    
y=day//365
rd=day%365
m=rd//30
rd=rd%30
d=rd

print(day,"days are",y,"years",m,"months",d,"days")

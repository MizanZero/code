try:
    num1=float(input("Please enter the first number: "))
    op = input("Enter the desired operation between these numbers (only these are valid + - * / %): ")
    num2= float(input("Please enter the second number: "))

except:
    print("Please enter numbers only lil bro 🙏😭!")
    quit(code=0)


if op == "+":
    print("The sum of "+str(num1)+" and "+str(num2)+" is "+str(num1+num2))
elif op=="-":
    print(str(num2)+" subtracted from "+str(num1)+" gives "+str(num1-num2))
elif op=="*":
    print("The product of "+str(num1)+" and "+str(num2)+" is "+str(num1*num2))
elif op=="/":
    print(str(num1)+" divided by "+str(num2)+" gives "+str(num1/num2))
elif op=="%":
    print(str(num1)+" divided by "+str(num2)+" leaves a remainder "+str(num1%num2))
else:
    print("What operator is that lil bro 🙏😭! Only these will work + - * / %")


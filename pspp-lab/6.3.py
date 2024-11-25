a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

#built in max function
print('using max function:',max(a,b,c))



#nested if
if a>b:
    if a>c:
        print('Using nested if:',a)
    else:
        print('Using nested if:',c)
elif c>b:
    print('Using nested if:',c)
else:
    print('Using nested if:',b)



#if elif
if a>b and a>c:
    print('Using if elif:',a)
elif b>a and b>c:
    print('Using if elif:',b)
else:
    print('Using if elif:',c)



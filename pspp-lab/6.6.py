a=float(input('Enter first side: '))
b=float(input('Enter second side: '))
c=float(input('Enter third side: '))

if a+b>c and b+c>a and a+c>b:
    print(a,b,c,'are sides of a triangle')
else:
    print(a,b,c,'are not sides of a triangle')

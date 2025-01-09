a=float(input('Enter first side: '))
b=float(input('Enter second side: '))
c=float(input('Enter third side: '))

if a+b>=c and b+c>=a and a+c>=b:
    print(a,b,c,'are sides of a triangle')
else:
    print(a,b,c,'are not sides of a triangle')

g=max(a,c,b) 
lesser=[a,b,c]
lesser.remove(g)

if g**2==lesser[0]**2+lesser[1]**2:
    print('Right-angled triangle')
else:
    print('Not right angled')


x=int(input('Enter x: '))
y=int(input('Enter y: '))

if x>0:
    if y>0:
        print('1st')
    elif y<0:
        print('4th')
    else:
        print('Positive x-axis')
elif x<0:
    if y>0:
        print('2nd')
    elif y<0:
        print('3rd')
    else:
        print('Negative x-axis')
else:
    if y>0:
        print('positive y-axis')
    elif y<0:
        print('negative y-axis')
    else:
        print('Origin')
print()
print('Without nested:')

if x>0 and y>0:
    print('1st')
elif x>0 and y<0:
    print('4th')
elif x<0 and y>0:
    print('2nd')
elif x<0 and y<0:
    print('3rd')
elif x==0:
    print('y axis')
elif y==0:
    print('x axis')
else:
    print('Orgin')



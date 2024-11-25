n=input('Enter to check digit: ')

if len(n)==1:
    if n in '1234567890':
        print(n,'is a digit')
    else:
        print(n,'not a digit')

else:
    print('Enter only a single digit or character')

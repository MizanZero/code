a=input('Enter character: ')


if a.isalpha():
    print(a,'is in the alphabet(using .isalpha())')
else:
    print(a,'is not in the alphabet(using .isalpha())')



if ord(a) in range (65,122+1):
    print(a,'is in the alphabet(using ord() value)')
else:
    print(a,'is not in the alphabet(using ord() value)')



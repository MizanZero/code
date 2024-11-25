a=input('Enter character: ')

if len(a)==1:
    if a in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('Not vowel')
else:
    print('Enter a single character only')


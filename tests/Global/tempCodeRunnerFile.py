print("Your guess was higher than the answer, try again")


import math

k=''

while k!='exit()':
	k=input('Enter: ')
	v=''
	r=''
	
	for c in k:
		if ord(c)%2==0:
			v+=chr(ord(c)**2+1)
		else:
			v+=chr(ord(c)**2-1)
	
	for x in v:
		if math.sqrt(ord(x)-1)%2==0:
			r+=chr(int(math.sqrt(ord(x)-1)))
		else:
			r+=chr(int(math.sqrt(ord(x)+1)))

	print(k)
	print(v)
	print(r)
	print()

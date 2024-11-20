print("Your guess was higher than the answer, try again")


import math

k=''

while k!='exit()':
	k=input('Enter: ')
	v=''
	
	
	def enc(k):
		for c in k:
			if ord(c)%2==0:
				v+=chr(ord(c)**2+1)
			else:
				v+=chr(ord(c)**2-1)
		print(v)
	
	def dec(v):
		r=''
		for x in v:
			if math.sqrt(ord(x)-1)%2==0:
				r+=chr(int(math.sqrt(ord(x)-1)))
			else:
				r+=chr(int(math.sqrt(ord(x)+1)))
		print(r)

	try:
		enc(k)
		dec(v)
	except:
		dec(k) 


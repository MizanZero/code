print("Your guess was higher than the answer, try again")


for c in k:
  v=chr(ord(c)**2+1) if ord(c)%2==0 else chr(ord(c)**2-1) 

for c in v:
  k=chr(math.sqrt(ord(c)-1)) if math.sqrt(ord(c)-1)%2==0 else chr(math.sqrt(ord(c)+1))


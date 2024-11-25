n=int(input('Enter n: '))
f=1

if n in [0,1]:
         print(1)
else:
    for i in range(1,n):
        f*=i+1 
    print(f)
    i

def raise_power(a, b):
    try:
        a = int(a)
        b = int(b)

        if (a and b) != (0 and 1):
            r = a
            print(r)
            for i in range(b-1):
                r *= a
                print (r)

        elif a==0 and b==0:
            r = "0 cannot be raised to 0." #This will be printed as final result
        elif b == 0 or a==1:
            r=1
        else:
            r=a

        print("The final result is: "+str(r))

    except:
        print("Enter integers only!")

raise_power(input("Base: "), input("Exponent: "))
#print("The final result: "+ str(raise_power(int(input("Base: ")), int(input(("Exponent: "))))))

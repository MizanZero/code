a = "1"
if a == ("b" or "c" or "n" or "f"):
    print("Is a vowel")
else:
    print ("Not a vowel")

b = int(input("Enter integer for b: "))
a = int(input("Enter integer for a: "))
c = int(input("Enter integer for c: "))


if len({a,b,c} & {0,1,2}) == 2: #'and' implies that both a and b are applicable and 'or' implies that either 0 or 1 can be found for declaring true, which finally implies that if either 0 or 1 are found after checking a and b
    print("2 common")
else:
    print("Not")

#print(bool ({}))


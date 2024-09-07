a = "1"
if a == ("b" or "c" or "n" or "f"):
    print("Is a vowel")
else:
    print ("Not a vowel")

b = int(input("Enter integer for b: "))
a = int(input("Enter integer for a: "))

if (b and a) == (0 or 1): #'and' implies that both a and b are applicable and 'or' implies that either 0 or 1 can be found for declaring true, which finally implies that if either 0 or 1 are found after checking a and b
    print("Binary")
else:
    print("No binary")




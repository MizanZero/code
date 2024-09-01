def counter():
    count = 0

    def increment():
        nonlocal count
        count = count+1
        return count
    
    return increment


print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
f1 = counter()
print(f1())
print(f1())
print(f1())
print(f1())
print(f1())

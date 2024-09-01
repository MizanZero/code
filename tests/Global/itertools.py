from itertools import product
A = [1,2]
B = [4]

def cartesian_product(rep = 1):
    cp = product(A,B, repeat=rep) # repeat permutes all the sets among themselves said number of times.
    return ("List of cartesian product of "+str(A)+" "+str(B)+": "+str(list(cp)))

print(cartesian_product(2))

from itertools import permutations
def set_permutation(n=2):
    sp = list(permutations(A, n)) # n is the number of elements in the permuted sets
    return sp

print(set_permutation())

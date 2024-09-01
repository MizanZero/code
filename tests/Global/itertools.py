from itertools import product
A = [1,2,3,4,5]
B = [6]

def cartesian_product(rep = 1):
    cp = product(A,B, repeat=rep) # repeat permutes all the sets among themselves said number of times.
    return ("List of cartesian product of "+str(A)+" "+str(B)+": "+str(list(cp)))

print(cartesian_product(2))

from itertools import permutations 
def set_permutation(n=2):
    sp = list(permutations(A, n)) # n is the number of elements in the permuted sets
    return sp

print(set_permutation())

from itertools import combinations, combinations_with_replacement
def set_combination(n=2):
    sc = list(combinations(A, n))
    return sc

def set_combination_replacement(n=2): # repetitions are allowed e.g.: (1,1)
    scr = list(combinations_with_replacement(A,n))
    return scr

from itertools import accumulate
import operator
def cumulate(option):
    acc = list(accumulate(A, func=eval(option))) #result of every step is dragged along and
                                           #func is applied in each step
    return acc

print(cumulate("operator.mul"))
import numpy as np
from math import exp, sqrt

def x(t): x = a1*exp(alpha1*t) + a2*exp(alpha2*t); return round(x, 2)

def v(t): v = a1*alpha1*exp(alpha1*t) + a2*alpha2*exp(alpha2*t); return round(v, 2)

t1 = 0#float(input('Initial time: '))
t2 = 100#float(input('Final time: '))
x0 = 1#float(input('Initial displacement: '))
v0 = 0#float(input('Initial velocity: '))

m = 1#float(input('Mass: '))
k = 1#float(input('Spring constant: '))
b = 2#float(input('Damping constant: ')) /2
omega = sqrt(k/m)

num = 100#int(input('Number of time points: '))

alpha1 = -b+sqrt(b**2 - omega**2)
alpha2 = -alpha1 - 2*b

print(alpha1, alpha2)

step = (t2-t1)/num

coeffs = np.array([[exp(alpha1*t1), exp(alpha2*t1)], [alpha1*exp(alpha1*t1), alpha2*exp(alpha2*t1)]])
consts = np.array([x0, v0])

a = np.linalg.solve(coeffs, consts)
a1 = a[0]; a2 = a[1]; print(a1, a2) 

t = t1

for i in range(num+1): # first is t1 last is t1 + num*step 
    print ("Time:",t, "Displacement:",x(t), "Velocity:",v(t))
    t += step


import numpy as np
from math import exp, sqrt

def x(t): x = a1*exp(alpha1*t) + a2*exp(alpha2*t); return x

def v(t): v = a1*alpha1*exp(alpha1*t) + a2*alpha2*exp(alpha2*t); return v

t1 = 0#float(input('Initial time: '))
t2 = 10#float(input('Final time: '))
x0 = 1#float(input('Initial displacement: '))
v0 = 0#float(input('Initial velocity: '))

m = 1#float(input('Mass: '))
k = 5#float(input('Spring constant: '))
b = 2.5#float(input('Damping constant: ')) /(2*m)
omega = sqrt(k/m)

num = 100#int(input('Number of time points: '))

alpha1 = -b + sqrt(b**2 - omega**2)
alpha2 = -b - sqrt(b**2 - omega**2)

print("alpha1: {}, alpha2: {}".format(alpha1, alpha2)) 

step = (t2-t1)/num

coeffs = np.array([[1, 1], [alpha1, alpha2]])
consts = np.array([x0, v0])

a = np.linalg.solve(coeffs, consts)
a1 = a[0]; a2 = a[1]; print("a1: {}, a2: {}".format(a1, a2)) 

t = np.linspace(t1, t2, num)

for i in t : print("t:{}, x:{}, v:{}".format(i, round(x(i),2), round(v(i),2)))


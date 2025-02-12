def x(t): return a1*exp(alpha1*t) + a2*exp(alpha2*t)

def v(t): return a1*alpha1*exp(alpha1*t) + a2*alpha2*exp(alpha2*t)

t1 = int(input('Initial time: '))
t2 = int(input('Final time: '))

m = float(input('Mass: '))
k = float(input('Spring constant: '))
b = float(input('Damping constant: ')) /2
omega = sqrt(k/m)

num = int(input('Number of time points: '))

alpha1 = -b+sqrt(b**2 - omega**2)
alpha2 = -alpha1 - 2*b

step = (t2-t1)/num

t=t1

for i in range(num):
    t += step
    print ("Time:",t, "Displacement:",x(t), "Velocity:",v(t))
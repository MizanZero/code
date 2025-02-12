def x(t):
    alpha1 = -b+sqrt(b**2 - omega**2)
    alpha2 = -alpha1 - 2*b

    return a1*exp(alpha1*t) + a2*exp(alpha2*t)

def 
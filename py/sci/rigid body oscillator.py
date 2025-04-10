from math import sin
from scipy.integrate import odeint

def diffEq(t, y):
    theta, omega = y
    return [
        omega,
        m*g*l*sin(theta)/(2*I)
        ]

m = input("Enter mass: ")
I = input("Enter moment of inertia: ")
g = input("Enter acceleration due to gravity: ")
l = input("Enter length(Centre of Mass to hinge): ")


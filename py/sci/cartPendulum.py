M = 1#float(input('Mass of cart: '))
m = 1#float(input('Mass of pendulum: '))
b = 0.01#float(input('Damping coefficient: '))
l = 0.3#float(input('Length for pendulum: '))
g = 9.78313#float(input('Acc due to Gravity: '))
I = m*l*l/3
Cd = 0.01#float(input('Drag coefficient: '))
rho = 1.225#float(input('Air density: '))
A = 0.1#float(input('Cross-sectional area: '))
F = 1#float(input('Force applied: '))

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

def pendulum_eq(t,y):
    theta, omega, x, v = y
    dtheta_dt = omega
    dx_dt = v
    a = cart_eq(t,y)
    I_alpha = -m*l*a*cos(theta) - m*g*l*sin(theta) - (1/2)*Cd*rho*A*l*l*omega*omega
    domega_dt = I_alpha / I
    dv_dt = a
    return [omega, domega_dt, v, dv_dt] # omega, alpha, v, a 

def cart_eq(t,y):
    theta, omega, x, v = y
    dtheta_dt = omega
    dx_dt = v
    dv_dt = (F + m*l*dtheta_dt*dtheta_dt*sin(theta) - m*l*dtheta_dt*dtheta_dt*cos(theta) - b*v) / (M + m)
    return dv_dt

t_span = (0,10)
t_eval = np.linspace(*t_span,1000) 

solution = solve_ivp(pendulum_eq, t_span, [0,0,0,0], t_eval=t_eval) 

sol = zip(solution.t, solution.y[0], solution.y[1])

for t,th,om in sol:
    print(f"""t = {t:.2f}, theta = {th:.2f}, omega = {om:.2f}""")

theta_sol, omega_sol, x_sol, v_sol = solution.y
time = solution.t

# Plot Results
plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.plot(time, theta_sol, label="Theta (rad)")
plt.plot(time, omega_sol, label="Angular Velocity (rad/s)")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Pendulum State")
plt.grid()

plt.subplot(2,1,2)
plt.plot(time, x_sol, label="Cart Position (m)")
plt.plot(time, v_sol, label="Cart Velocity (m/s)")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Cart State")
plt.grid()

plt.tight_layout()
plt.show()
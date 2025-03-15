import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# System Parameters
M = 1       # Mass of cart (kg)
m = 1       # Mass of pendulum (kg)
b = 0.01    # Damping coefficient (kg/s)
l = 0.3     # Pendulum length (m)
g = 9.78313 # Acceleration due to gravity (m/s^2)
I = m * l**2 / 3  # Moment of inertia of rod pendulum (kg·m²)
Cd = 0.01   # Drag coefficient
rho = 1.225 # Air density (kg/m³)
A = 0.1     # Cross-sectional area (m²)
F = 1       # Force applied to the cart (N)

# Equations of Motion
def cart_pendulum(t, y):
    theta, omega, x, v = y  # Unpacking state variables

    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    # Air resistance force (F_air = 0.5 * Cd * rho * A * v²)
    F_air = 0.5 * Cd * rho * A * v**2 * np.sign(v)

    # Effective mass matrix
    D = (M + m) - (m * cos_theta**2)

    # Angular acceleration (domega/dt)
    domega_dt = (-m * g * sin_theta - m * l * omega**2 * sin_theta * cos_theta - I * omega - F_air) / (l * D)

    # Linear acceleration (dv/dt)
    dv_dt = (F + m * l * omega**2 * sin_theta - m * l * domega_dt * cos_theta - b * v - F_air) / D

    return [omega, domega_dt, v, dv_dt]

# Time span
t_span = (0, 10)
t_eval = np.linspace(0, 10, 500)  # 500 time steps

# Initial Conditions: [theta0, omega0, x0, v0]
y0 = [np.pi / 6, 0, 0, 0]  # 30-degree initial angle, no initial velocity

# Solving the ODEs
solution = solve_ivp(cart_pendulum, t_span, y0, t_eval=t_eval)

# Extracting results
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

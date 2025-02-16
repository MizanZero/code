import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# System parameters
m = 1.0   # Mass (kg)
c = 5   # Damping coefficient (Ns/m)
k = 5.0   # Spring stiffness (N/m)

# Define the system of equations
def spring_mass_damper(y, t):
    x, v = y  # y[0] = x (position), y[1] = v (velocity)
    dxdt = v
    dvdt = (-c * v - k * x) / m  # Second-order differential equation
    return [dxdt, dvdt]

# Initial conditions: [initial displacement, initial velocity]
y0 = [1.0, 0.0]  

# Time array for simulation
t = np.linspace(0, 20, 1000)  # Simulate for 10 seconds

# Solve the differential equation
solution = odeint(spring_mass_damper, y0, t)

# Extract position and velocity
x = solution[:, 0]
v = solution[:, 1]

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Displacement (x)")
plt.plot(t, v, label="Velocity (v)", linestyle="dashed")
plt.xlabel("Time (s)")
plt.ylabel("Displacement & Velocity")
plt.legend()
plt.grid()
plt.title("Spring-Mass-Damper System")
plt.show()
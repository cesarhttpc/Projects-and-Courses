import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
 
def coupled_differential_equations(y, alpha, beta, p_m, p_h, delta, gamma):

    m,h = y
    dmdt = alpha * p_m * h * (1-m) - delta* m 
    dhdt = beta  * p_h * m * (1-h) - gamma* h

    return [dmdt, dhdt]
 
y0 = [1.0, 0.0]  
alpha = 1.0
beta = 2.0
p_m = 0.5
p_h = 0.1
delta = 1.0
gamma = 1.0
0
t = np.linspace(0, 10, 1000)  
 
solutions = odeint(coupled_differential_equations, y0, t, args=(k, b))
 
x_values = solutions[:, 0]
v_values = solutions[:, 1]
 
plt.plot(t, x_values, label='Position x')
plt.plot(t, v_values, label='Velocity v')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend()
plt.title('Coupled Differential Equations: Simple Harmonic Oscillator with Damping')
plt.show()
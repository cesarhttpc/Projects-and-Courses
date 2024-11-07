# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model_Ross_MacDonald(u, t, b , beta_h , gamma, beta_v, miu_v):
    N_h    = 1000
    N_v    = 2000
    I_h, I_v = u
    dI_hdt = (b*beta_h/N_h)*I_v*(N_h - I_h) - gamma*I_h
    dI_vdt = (b*beta_v/N_h)*I_h*(N_v - I_v) - miu_v*I_v
    return [dI_hdt, dI_vdt]

def funcion():

    solutions = odeint(model_Ross_MacDonald, u0, t, args=(b , beta_h , gamma, beta_v, miu_v))

    humanos = solutions[:, 0]
    vectores = solutions[:, 1]


u0 = [2,20]
# b      = 0.7
# beta_h = 1
# beta_v = 1

# gamma  = 1/2
# miu_v  = 1/2

t = np.linspace(0, 15, 50)
b = np.linspace(0,1,50)
beta_h = np.linspace(0,10,100)
beta_v = np.linspace(0,10,100)

gamma = np.linspace(0,1,50)
miu = np.linspace(0,1,100)

print( np.meshgrid(t,b,beta_h,beta_v,gamma,miu) )












# %%

plt.plot(t, humanos, label='Humanos Infectados')
plt.plot(t, vectores, label='Vectores Infectados')
plt.xlabel('Time')
plt.ylabel('Infectados')
plt.legend()
plt.show()
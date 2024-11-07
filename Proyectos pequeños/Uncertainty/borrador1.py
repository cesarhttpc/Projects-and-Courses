# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Observations
em = np.arange(0, 41)
inc = np.array([2, 27, 22, 22, 27, 37, 20, 13, 12, 43, 19, 22, 15, 23, 16, 19, 32, 19, 26, 19, 31, 25, 36, 48, 72, 83, 76, 142, 147, 146, 151, 277, 378, 589, 556, 1037, 626, 925, 1039, 704, 742])

plt.scatter(em, inc)
plt.title("Datos Observados")
plt.show()



# Model 2320898
def dengue_Ross_M(t, u, b, βh, βv, γ):
    Ih, Iv = u
    du = np.zeros_like(u)
    
    du[0] = (b * βh / 2320898) * Iv * (2320898 - Ih) - (γ + 1/(76*52)) * Ih
    du[1] = (b * βv / 2320898) * Ih * (3 * 2320898 - Iv) - (1/2) * Iv
    
    return du

# Forward Map
def FowarMap(θ):
    b, βh, βv, γ, u_01, u_02 = θ
    u0 = [u_01, u_02]
    sol = solve_ivp(dengue_Ross_M, (0, 40), u0, args=(b, βh, βv, γ), method='RK45', dense_output=True)
    return sol.sol(em)[0]

σ = 100

# Likelihood Function
def Log_Ver_Norm(θ):
    diff = inc - FowarMap(θ)
    l = (-1/(2*σ**2)) * np.sum(diff**2)
    return l

# Log Prior
def Log_Prior(θ):
    return -(np.log(1 - 0.01) + np.log(1 - 0.01) + np.log(1 - 0.01) + np.log(1 - 0.01) + np.log(10 - 1) + np.log(10 - 1))

# Function U
def Norm_U(θ):
    return -(Log_Ver_Norm(θ) + Log_Prior(θ))

# Support Function
def Supp_McDonald(θ):
    b, βh, βv, γ, u_01, u_02 = θ
    return all([0.01 <= b <= 1, 0.01 <= βh <= 1, 0.01 <= βv <= 1, 0.01 <= γ <= 1, 1 <= u_01 <= 10, 1 <= u_02 <= 10])

# Initial Conditions
x_0 = np.random.uniform(0.01, 1, 6)
x_p0 = np.random.uniform(0.01, 1, 6)

# MCMC Chain
n_iterations = 5000
chain = np.zeros((n_iterations, 6))

# Metropolis-Hastings algorithm
for i in range(1, n_iterations):
    proposal = x_0 + np.random.normal(0, 0.1, 6)
    alpha = min(1, np.exp(Norm_U(proposal) - Norm_U(x_0)))
    if np.random.uniform() < alpha and Supp_McDonald(proposal):
        x_0 = proposal
    chain[i, :] = x_0

# Plot Results
labels = ['b', 'βh', 'βv', 'γ', 'I_h0', 'I_v0']
plt.figure(figsize=(10, 8))
for i in range(6):
    plt.subplot(3, 2, i+1)
    plt.plot(chain[100:, i], label=labels[i])
    plt.legend()
plt.show()


# %%

print(chain)


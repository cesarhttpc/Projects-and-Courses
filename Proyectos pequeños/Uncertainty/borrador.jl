#using Turing
using Distributions, DifferentialEquations, JTwalk, Intervals

#Import MCMCChain, Plots, and StatsPlots for visualizations and Diagnostics. 
using MCMCChains, StatsPlots, Plots

using LinearAlgebra

#Set  a seed for reproductibility
using Random, CSV, DataFrames
Random.seed!(123)

em = [0:1:40;];
inc = [2, 27, 22, 22, 27, 37, 20, 13, 12, 43, 19, 22, 15, 23, 16, 19, 32, 19, 26, 19, 31, 25, 36, 48, 72, 83, 76, 142, 147, 146, 151, 277, 378, 589, 556, 1037, 626, 925, 1039]

scatter(sem, inc, title = "Datos Observados", label = "")

# Model 2320898
function dengue_Ross_M(du,u,p,t)
    Ih, Iv = u
    b, βh, βv, γ = p
    
    du[1] = (b*βh/2320898)*Iv*(2320898 - Ih) - (γ + 1/(76*52))*Ih
    du[2] = (b*βv/2320898)*Ih*(3*2320898 - Iv) - (1/2)*Iv
end

# Foward Map
function FowarMap(θ)
    b, βh, βv, γ, u_01, u_02 = θ
    p = [b, βh, βv, γ] 
    u0 =[u_01, u_02]
    prob1 = ODEProblem(dengue_Ross_M, u0, (0,40),p)
    sol = solve(prob1, TRBDF2(), saveat = 1);   
    return sol[1,:]
end

σ = 1;

# Función Verosimilitud
function Log_Ver_Norm(θ) 
    suma = 0     
    for i ∈ 1: length(inc)
    suma = suma + (inc[i] - FowarMap(θ)[i])^2
    end
    
     l = (-1/(2*σ^2))*suma
     return l
end

#b = Uniform(0.01,1);
#βh = Uniform(0.01,1);
#βv = Uniform(0.01,1);
#γ = Uniform(0.01,1);
#u_01 = Uniform(1,100);
#u_01 = Uniform(1,100);


# Log Prior
function Log_Prior(θ)
#    b, βh, βv, γ, u_01, u_02 = θ
 return -(log(1 - 0.01) + log(1 - 0.01) + log(1 - 0.01) + log(1 - 0.01) + log(10 - 1) + log(10 - 1))
end


# Function U
function Norm_U(θ)
    return -(Log_Ver_Norm(θ) + Log_Prior(θ))
end

I1 = Interval{Closed,Closed}(0.01,1)
I2 = Interval{Closed,Closed}(1,10);


# Sopport Function  OJO REVISAR EL SOPORTE
function Supp_McDonald(θ)
    b, βh, βv, γ, u_01, u_02 = θ
	return all([b ∈ I1, βh ∈ I1, βv ∈ I1, γ ∈ I1, u_01 ∈ I2, u_01 ∈ I2])
end


# Initial Condition
x_0 = [rand(Uniform(0.01,1)), rand(Uniform(0.01,1)), rand(Uniform(0.01,1)), rand(Uniform(0.01,1)), rand(Uniform(1,10)), rand(Uniform(1,10))]
x_p0 = [rand(Uniform(0.01,1)), rand(Uniform(0.01,1)), rand(Uniform(0.01,1)), rand(Uniform(0.01,1)), rand(Uniform(1,10)), rand(Uniform(1,10))];

Ross_MC = jtwalk( n=6, U=Norm_U, Supp=Supp_McDonald);

Run!(Ross_MC, T=5000, x0=x_0, xp0=x_p0);

p1 = plot(Ross_MC.Output[:,1], color =:green, label = "b")
p2 = plot(Ross_MC.Output[:,2], color =:red,label = "βh")
p3 = plot(Ross_MC.Output[:,3], color =:black,label = "βv")
p4 = plot(Ross_MC.Output[:,4], color =:blue,label = "γ")
p5 = plot(Ross_MC.Output[:,5], color =:orange,label = "I_h0")
p6 = plot(Ross_MC.Output[:,6], color =:yellow,label = "I_v0")

plot(p1, p2, p3, layout = (3,1))

plot(p4, p5, p6, layout = (3,1))
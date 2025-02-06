import scipy.integrate as spi
import numpy as np

# Given constants
R = 8.314  # J/(mol·K)
A = 3.280
B = 0.593e-3
C = 0  # Not provided
D = 0.04e-5
E = 0  # Not provided

n = 2  # moles of N2
T1 = 500  # Initial temperature in K
P1 = 1.5e6  # Initial pressure in Pa
P_ext = 1.0e5  # External pressure in Pa

# Function for Cp/R
def Cp_over_R(T):
    return A + B*T + C*T**2 + D*T**-2 + E*T**3

# Convert to Cv (Cv = Cp - R)
def Cv(T):
    return (Cp_over_R(T) * R) - R

# Initial volume V1
V1 = (n * R * T1) / P1
print(f"Initial volume: {V1} m^3")

# Define function for final volume V2 in terms of T2
def V2(T2):
    return (n * R * T2) / P_ext

# Work done at constant external pressure
def work(T2):
    return P_ext * (V2(T2) - V1)

# Energy balance: ΔU = -W
def energy_balance(T2):
    delta_U, _ = spi.quad(lambda T: n * Cv(T), T1, T2)  # Integrate Cv dT
    return delta_U + work(T2)  # Should equal 0 for equilibrium

# Solve for T2 using root-finding
from scipy.optimize import fsolve

T2_solution = fsolve(energy_balance, 300)[0]  # Initial guess 300K

# Compute final values
W_final = work(T2_solution)  # Work done
delta_U_final, _ = spi.quad(lambda T: n * Cv(T), T1, T2_solution)  # Internal energy change

print(T2_solution, W_final, delta_U_final)
print(Cv(500))
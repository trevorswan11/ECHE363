import sympy as sp

# Define variables
T_out = sp.Symbol('T_out')

# Constants
R = 8.314  # J/(mol·K)
T_ref = 273  # Reference temperature in K

# Given temperatures
T1 = 373  # K
T2 = 293  # K

# Given molar flow rates
n1 = 0.1613  # mol/s
n2 = 0.2064  # mol/s
n_out = n1 + n2

# Heat capacity function coefficients
A = 3.627
B = 5.324e-3

# Enthalpy differences from reference
h1 = R * (A * (T1 - T_ref) + (B / 2) * (T1**2 - T_ref**2))
h2 = R * (A * (T2 - T_ref) + (B / 2) * (T2**2 - T_ref**2))
print(h1, h2)
h_out = R * (A * (T_out - T_ref) + (B / 2) * (T_out**2 - T_ref**2))

# Energy balance equation
energy_eq = sp.Eq(n1 * h1 + n2 * h2, n_out * h_out)
print((n1 * h1 + n2 * h2) /n_out)

# Solve for T_out
T_out_solution = sp.solve(energy_eq, T_out)
print(T_out_solution)
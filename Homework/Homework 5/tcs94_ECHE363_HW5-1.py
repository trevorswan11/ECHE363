import matplotlib.pyplot as plt
import numpy as np

steam_data = {
    # pressure: [v @ 700C, v @ 800C]
    1.6: [0.27937, 0.30859],
    1.8: [0.24818, 0.27420],
    2: [0.22323, 0.24668],
    2.5: [0.17832, 0.19716],
    3: [0.14838, 0.16414],
    3.5: [0.12699, 0.14056],
    4: [0.11095, 0.12287],
    4.5: [0.09847, 0.10911],
    5: [0.08849, 0.09811],
    6: [0.07352, 0.08160],
    7: [0.06283, 0.06981],
    8: [0.05481, 0.06097],
    9: [0.04857, 0.05409],
    10: [0.04358, 0.04859],
    12.5: [0.03460, 0.03869],
    15: [0.028612, 0.032096],
    17.5: [0.0243365, 0.0273849],
    # 20: [0.0211311, 0.0238532]
}
 
T_K = 1000
T_C = T_K - 273
v_hat_1 = 0.277 # m^3/kg
v_hat_2 = 0.0277 # m^3/kg
mols = 2 # mol
mass = 2 * 18.02 * (1/1000) # kg
interpolated = {}

# Interpolate each entry in the dict to find the volume at 1000K
for i in range(len(steam_data)):
    p, v_hats = list(steam_data.items())[i]
    v_700, v_800 = v_hats[0], v_hats[1]
    interpolated.update({p: v_hats[0] + (v_hats[1] - v_hats[0]) * (T_C - 700) / (800 - 700)})
v_hats = list(interpolated.values())
pressures = list(interpolated.keys())
print(v_hats)

# Interpolate the pressure to find the pressure at 1000K at initial and final volume
initial_pressure = pressures[0] + (pressures[1] - pressures[0]) * (v_hat_1 - v_hats[0]) / (v_hats[1] - v_hats[0]) 
final_pressure = pressures[-1] + (pressures[-2] - pressures[-1]) * (v_hat_2 - v_hats[-1]) / (v_hats[-2] - v_hats[-1])
print(initial_pressure, final_pressure)

interested_volumes = [v_hat_1] + v_hats[1:-1] + [v_hat_2]
interested_pressures = [initial_pressure] + pressures[1:-1] + [final_pressure]

# Integrate!
area = np.trapz(interested_pressures[::-1], interested_volumes[::-1]) # Mpa * m^3/kg
work = mass * area # MPa * m^3
work *= 1000 # kPa * m^3 = kJ
print(work)

# Plot the data
plt.plot(v_hats, pressures)

plt.scatter([v_hat_1], [initial_pressure], color=['orange'])
plt.scatter([v_hat_2], [final_pressure], color=['red'])

plt.text(v_hat_1 - 0.005, initial_pressure + 1, f'({v_hat_1:.3f}, {initial_pressure:.3f})', fontsize=9, ha='center', color='black')
plt.text(v_hat_2 + 0.037, final_pressure, f'({v_hat_2:.3f}, {final_pressure:.3f})', fontsize=9, ha='center', color='black')

plt.fill_between(interested_volumes, interested_pressures, color='skyblue', alpha=0.3)

plt.plot([v_hat_1, v_hat_1], [0, initial_pressure], linestyle='--', color='black')
plt.plot([v_hat_2, v_hat_2], [0, final_pressure], linestyle='--', color='black')

plt.xlabel("Specific Volume (m^3/kg)")
plt.ylabel("Pressure (MPa)")
plt.title("Isothermal Expansion of Water at 1000K")
plt.legend(["Pressure vs. Volume", "Initial Volume", "Final Volume", f"Work = {work:.3f} kJ"])
plt.show()
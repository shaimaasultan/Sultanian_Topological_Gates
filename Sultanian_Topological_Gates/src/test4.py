import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Global High-Resolution Settings ---
plt.rcParams['figure.dpi'] = 300           
plt.rcParams['font.family'] = 'serif'

# --- 2. Soltanian Constants & 3D Parameters ---
L_old = np.pi - np.log(np.pi) 
E_ground = np.exp(L_old) 
b = 0.15 # Growth factor for the helix radius
pitch = 1.0 # Vertical climb rate for the Z-vector

# Data for the continuous Soltanian Helix path
t = np.linspace(0, 10 * np.pi, 2000)
x_path = E_ground * np.exp(b * t) * np.cos(t)
y_path = E_ground * np.exp(b * t) * np.sin(t)
z_path = pitch * t  # Vertical displacement (The Z-Vector)

# --- 3. Significant 3D Nodes (Zeta & Primes) ---
# Zeta Zeros (Cyan)
zeta_gammas = [14.13, 21.02, 25.01, 30.42, 32.93]
# Prime Harmonics (Orange) - Showing propulsion
primes = [2, 3, 5, 7, 11]
max_E = np.sqrt(0.25 + max(zeta_gammas)**2)
# --- 4. Create the 3D Plot ---
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')

# Plot the base Helical Path
ax.plot(x_path, y_path, z_path, color='#DAA520', linewidth=1.5, alpha=0.6, label='Soltanian Helix Path')

# Plot Zeta Nodes (Cylindrical Resonance)
for g in zeta_gammas:
    E_r = np.sqrt(0.25 + g**2)
    theta = (np.log(E_r) - L_old) / b
    z_val = pitch * theta
    ax.scatter(E_r * np.cos(theta), E_r * np.sin(theta), z_val, 
               color='#00FFFF', s=80, edgecolors='black', label='Zeta Node' if g == 14.13 else "")

# Plot Prime Vectors (Propulsion in Z)
for p in primes:
    E_p = np.exp(p / L_old) * E_ground
    theta_p = (np.log(E_p) - L_old) / b
    z_p = pitch * theta_p
    ax.scatter(E_p * np.cos(theta_p), E_p * np.sin(theta_p), z_p, 
               color='#FF4500', marker='x', s=100, linewidths=2, label='Prime Harmonic' if p == 2 else "")

# --- 5. Aesthetics & Labels ---
ax.set_title("3D Soltanian Vector Field: The Helical Interchange", pad=20, fontsize=9, fontweight='bold')
ax.set_xlabel("Real (A)", fontsize=6)
ax.set_ylabel("Imaginary (D)", fontsize=6)
ax.set_zlabel(r"Z-Vector: $\ln(C+D)$", fontsize=6)

# Professional dark theme for 3D depth
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(True, linestyle='--', alpha=0.3)

# Adjust the viewing angle to see the vertical climb
ax.view_init(elev=20, azim=25)

plt.legend(loc='upper left', prop={'size': 6}, frameon=True)
plt.tight_layout()

# plt.savefig('Soltanian_3D_Helix.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Global High-Resolution Settings ---
plt.rcParams['figure.dpi'] = 300           
plt.rcParams['font.family'] = 'serif'

# --- 2. Soltanian Constants & 3D Parameters ---
L_old = np.pi - np.log(np.pi) 
E_ground = np.exp(L_old) 
b = 0.5    # The high-growth factor
pitch = 1.0 

# --- 3. Significant 3D Nodes (Zeta & Primes) ---
zeta_gammas = [14.13, 21.02, 25.01, 30.42, 32.93]
primes = [2, 3, 5, 7, 11]

# --- DYNAMIC SYNC LOGIC (The Fix) ---
# We find the maximum energy in your dataset to bound the spiral path
max_E = np.sqrt(0.25 + max(zeta_gammas)**2)
# Solve for t: max_E = E_ground * exp(b * t)
t_limit = (np.log(max_E) - np.log(E_ground)) / b

# Generate the path precisely to fit the data
t = np.linspace(0, t_limit * 1.1, 2000) 
x_path = E_ground * np.exp(b * t) * np.cos(t)
y_path = E_ground * np.exp(b * t) * np.sin(t)
z_path = pitch * t 

# --- 4. Create the 3D Plot ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the base Helical Path
ax.plot(x_path, y_path, z_path, color='#DAA520', linewidth=2, alpha=0.6, label='Soltanian Helix Path')

# Plot Zeta Nodes (Cylindrical Resonance)
for g in zeta_gammas:
    E_r = np.sqrt(0.25 + g**2)
    # Sync the angle to the radius so they sit ON the line
    theta = (np.log(E_r) - np.log(E_ground)) / b
    z_val = pitch * theta
    ax.scatter(E_r * np.cos(theta), E_r * np.sin(theta), z_val, 
               color='#00FFFF', s=100, edgecolors='black', zorder=5, 
               label='Zeta Node' if g == 14.13 else "")

# Plot Prime Vectors (Propulsion in Z)
for p in primes:
    E_p = np.exp(p / L_old) * E_ground
    theta_p = (np.log(E_p) - np.log(E_ground)) / b
    z_p = pitch * theta_p
    # Only plot if the prime harmonic is within the visual range
    if E_p <= max_E * 1.2:
        ax.scatter(E_p * np.cos(theta_p), E_p * np.sin(theta_p), z_p, 
                   color='#FF4500', marker='x', s=120, linewidths=2, 
                   label='Prime Harmonic' if p == 2 else "")

# --- 5. Aesthetics & Labels ---
ax.set_title(f"3D Soltanian Helix (b={b}): Phase-Locked Convergence", pad=20, fontsize=12, fontweight='bold')
ax.set_xlabel("Real", fontsize=10)
ax.set_ylabel("Imaginary", fontsize=10)
ax.set_zlabel("Z-Vector climb", fontsize=10)

# Professional styling
ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
ax.view_init(elev=20, azim=45)

plt.legend(loc='upper left', prop={'size': 8})
plt.tight_layout()
plt.show()
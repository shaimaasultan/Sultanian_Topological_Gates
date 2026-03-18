import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Global Setup ---
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.family'] = 'serif'

# Soltanian Constants
L_OLD = np.pi - np.log(np.pi)
E_GROUND = np.exp(L_OLD)

# --- 2. Create Figure with Two 3D Subplots ---
fig = plt.figure(figsize=(18, 9), facecolor='white')

# --- SUBPLOT 1: THE RIEMANN SPHERE (Classical) ---
ax1 = fig.add_subplot(121, projection='3d')

# Generate Sphere Surface
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
xs = np.cos(u) * np.sin(v)
ys = np.sin(u) * np.sin(v)
zs = np.cos(v)
ax1.plot_surface(xs, ys, zs, color='lightblue', alpha=0.1, edgecolor='gray', linewidth=0.1)

# Map the "Critical Line" as a Meridian
merid_v = np.linspace(0, np.pi, 100)
merid_u = np.zeros(100)
ax1.plot(np.cos(merid_u)*np.sin(merid_v), np.sin(merid_u)*np.sin(merid_v), np.cos(merid_v), 
         color='red', linewidth=2, label='Critical Line (Meridian)')

# Add North Pole (Infinity)
ax1.scatter([0], [0], [1], color='black', s=100, label='Point at Infinity', zorder=10)

ax1.set_title("Riemann Sphere (Closed Topology)\nInfinity as a Singular Point", pad=20, fontsize=14)
ax1.set_axis_off()
ax1.legend(loc='lower center')

# --- SUBPLOT 2: THE SOLTANIAN HELIX (Dynamic) ---
ax2 = fig.add_subplot(122, projection='3d')

# Constants for Helix (Proportions corrected for visual clarity)
b = 0.04
pitch = 2.5
t = np.linspace(0, 8 * np.pi, 2000)

# Path
xh = E_GROUND * np.exp(b * t) * np.cos(t)
yh = E_GROUND * np.exp(b * t) * np.sin(t)
zh = pitch * t
ax2.plot(xh, yh, zh, color='#DAA520', linewidth=1.5, alpha=0.6, label='Soltanian Helix Path')

# Significant Nodes (Zeta Zeros)
zeta_gs = [14.13, 25.01, 32.93]
for g in zeta_gs:
    E_r = np.sqrt(0.25 + g**2)
    theta = (np.log(E_r) - L_OLD) / b
    ax2.scatter(E_r * np.cos(theta), E_r * np.sin(theta), pitch * theta, 
                color='#00FFFF', s=80, edgecolors='black', depthshade=False)

# Add Z-Vector (Direction of Infinity)
ax2.quiver(0, 0, 60, 0, 0, 20, color='black', linewidth=2, arrow_length_ratio=0.1, 
           label='Direction of Infinity (Z-Vector)')

ax2.set_title("Soltanian Helix (Open Topology)\nInfinity as a Helical Progression", pad=20, fontsize=14)
ax2.set_xlabel("Real Axis")
ax2.set_ylabel("Imaginary Axis")
ax2.set_zlabel("Z-Vector")

# Clean up axes
ax2.xaxis.pane.fill = ax2.yaxis.pane.fill = ax2.zaxis.pane.fill = False
ax2.view_init(elev=20, azim=30)
ax2.legend(loc='lower center')

plt.tight_layout()
# plt.savefig('Comparison_Riemann_vs_Soltanian.png', dpi=300)
plt.show()
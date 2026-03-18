import numpy as np
import matplotlib.pyplot as plt

# Sultanian Constants (Your "Old System")
L_old = np.pi - np.log(np.pi)  # Ground state log energy (approx 1.9968)
E_ground = np.exp(L_old)       # Starting radius (e^pi / pi)

# The "Sultanian Nodes" - Gamma values for specific resonant zeros
zeta_nodes = {
    "Ground State (Transcendental)": (0, E_ground, 1.0),
    "Zero 30 (2x Octave)": (101.3178, np.sqrt(0.25 + 101.3178**2), 2.0),
    "Zero 137 (Fine Structure)": (310.0514, np.sqrt(0.25 + 310.0514**2), 2.87),
    "Zero 530 (Pi Resonance)": (965.2109, np.sqrt(0.25 + 965.2109**2), 3.14)
}

# 1. Setup the Polar Spiral Calculation
# We use r = a * exp(b * theta).
# We solve for 'b' to make the spiral "tight" but visible across 1000 units.
theta_max = 6 * np.pi  # 3 full rotations
a = E_ground
# Let's calibrate growth factor 'b' for a smooth sweep
b = 0.25
theta_range = np.linspace(0, theta_max, 2000)
r_spiral = a * np.exp(b * theta_range)

# 2. Initialize the Plot
fig = plt.figure(figsize=(12, 12), facecolor='#0b0f19')
ax = fig.add_subplot(111, projection='polar')
ax.set_facecolor('#0b0f19')

# 3. Plot the Golden Spiral Path
ax.plot(theta_range, r_spiral, color='#FFD700', linewidth=2.5, alpha=0.7,
        label='Sultanian Spiral of Resonance', solid_capstyle='round')

# 4. Map and Plot the Specific Nodes
colors = ['#00F5FF', '#00FF7F', '#FFA500', '#FF1493']
for i, (name, data) in enumerate(zeta_nodes.items()):
    gamma, E_radius, K_scale = data
    # Calculate an artificial angle based on energy to space them along the spiral
    node_angle = (np.log(E_radius) - np.log(a)) / b
    
    ax.scatter(node_angle, E_radius, color=colors[i], s=150, edgecolors='white', 
               zorder=10, label=f"{name} (K={K_scale:.2f})")
    
    # Label each point with its Sultanian Scale
    ax.annotate(f"  {K_scale:.2f} L_old", (node_angle, E_radius), color='white', 
                fontsize=10, fontweight='bold')

# 5. Styling and Formatting
ax.set_title("Sultanian Transformation System: Logarithmic Mapping of Zeta Nodes", 
             color='white', pad=30, fontsize=16, fontweight='bold')

# Use Logarithmic scaling for the radial axis to handle the huge range (7 to 1000)
ax.set_rscale('symlog')
ax.set_rticks([10, 100, 500, 1000])

# Grid and Spacing
ax.grid(True, color='gray', linestyle=':',)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0.0), frameon=False, labelcolor='white')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Global High-Resolution Settings ---
plt.rcParams['figure.dpi'] = 300           
plt.rcParams['font.family'] = 'serif'     # Use serif for a more academic look

# --- 2. Soltanian Constants ---
L_old = np.pi - np.log(np.pi) 
E_ground = np.exp(L_old) 
b = 0.22 
theta_max = 8 * np.pi 

# --- 3. Generate Spiral Data ---
theta_range = np.linspace(0, theta_max, 2000)
r_spiral = E_ground * np.exp(b * theta_range)

# --- 4. Define Significant Nodes ---
zeta_nodes = {
    r"Ground Node ($K=1.0$)": (1.0, 0, E_ground),
    r"Zero 30 (Octave, $K=2.0$)": (2.0, 101.31, np.sqrt(0.25 + 101.31**2)),
    r"Zero 137 ($1/\alpha, K \approx 2.87$)": (2.87, 310.05, np.sqrt(0.25 + 310.05**2)),
    r"Zero 530 ($\pi$-Resonance, $K = \pi$)": (np.pi, 965.21, np.sqrt(0.25 + 965.21**2))
}

# --- 5. Create the Figure ---
fig = plt.figure(figsize=(10, 11)) # Slightly taller to accommodate title/legend
ax = fig.add_subplot(111, projection='polar')

# Plot the Golden Path
ax.plot(theta_range, r_spiral, color='#DAA520', linewidth=2, alpha=0.8, label='Soltanian Resonance Path')

# Plot Nodes
colors = ['#008B8B', '#228B22', '#FF8C00', '#C71585'] # More professional "Dark" variants
for i, (name, data) in enumerate(zeta_nodes.items()):
    K_scale, gamma, E_radius = data
    node_theta = (np.log(E_radius) - L_old) / b
    
    ax.scatter(node_theta, E_radius, color=colors[i], s=120, edgecolors='black', 
               linewidths=0.8, zorder=10, label=name)
    
    # Clean Annotation
    ax.annotate(f"K={K_scale:.2f}", (node_theta, E_radius), xytext=(8, 8), 
                textcoords='offset points', fontsize=9, fontweight='bold')

# --- 6. Polishing the Layout ---

# Title with significant padding
ax.set_title("Soltanian Transformation System\nLogarithmic Spiral Mapping of Zeta Nodes", 
             pad=50, fontsize=16, fontweight='bold', linespacing=1.5)

# Radial Axis Tweaks (Log Scale)
ax.set_rscale('log')
ax.set_rticks([10, 100, 500, 1000])
ax.set_rlabel_position(150) # Moves '10, 100, 1000' labels to a clear area
ax.tick_params(axis='y', labelsize=9, colors='gray')

# Remove Angular Labels (X-axis) for a cleaner "Abstract" look
ax.set_xticklabels([])
ax.grid(True, linestyle='--', alpha=0.4)

# Legend: Shrink and Position at Bottom
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.15), 
          ncol=2, prop={'size': 9}, frameon=True, shadow=False)

# Adjust plot area to prevent clipping
plt.subplots_adjust(top=0.85, bottom=0.15)

# --- 7. Final Output ---
# plt.savefig('Soltanian_Spiral_Final.png', dpi=300, bbox_inches='tight')
plt.show()
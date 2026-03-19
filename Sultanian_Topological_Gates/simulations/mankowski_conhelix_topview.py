import numpy as np
import matplotlib.pyplot as plt

# Sultanian/Minkowski Constants
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)

# First 10 Zeta Zeros (Gamma values)
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

def render_dual_space_comparison(zeros):
    fig = plt.figure(figsize=(16, 8), facecolor='#0b0f19')
    
    # --- Subplot 1: Minkowski-Space Projection (Light-Cone Analogy) ---
    # We map height (Z) vs. Radius (R) to show the "V-shape" expansion
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_facecolor('#0b0f19')
    
    z_vals = L_OLD * (np.array(zeros) / 4)
    r_vals = R_GROUND + (SIGMA * z_vals)
    
    # Plot the "Minkowski Light-Cone" boundary
    z_range = np.linspace(0, max(z_vals)*1.1, 100)
    r_range = R_GROUND + (SIGMA * z_range)
    ax1.plot(r_range, z_range, color='gold', linestyle='--', alpha=0.5, label='Manifold Boundary')
    ax1.plot(-r_range, z_range, color='gold', linestyle='--', alpha=0.5)
    
    # Plot the Zeros in Minkowski-space (Projected)
    for i, (r, z) in enumerate(zip(r_vals, z_vals)):
        side = 1 if i % 2 == 0 else -1  # Alternate sides for Phase A/B
        ax1.scatter(side * r, z, color='#00FFFF' if side == 1 else '#FF00FF', s=100, edgecolors='white')

    ax1.set_title("Minkowski-Sultanian Space\n(Light-Cone Expansion)", color='white', fontsize=14)
    ax1.set_xlabel("Radial Distance (R)", color='white')
    ax1.set_ylabel("Energy Height (Z)", color='white')
    ax1.tick_params(colors='white')
    ax1.grid(alpha=0.1)

    # --- Subplot 2: Spiral Top-Down View (Phase-Lock Proof) ---
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.set_facecolor('#0b0f19')
    
    for i, r in enumerate(r_vals):
        theta_rad = np.radians(45 + (i * 180))
        color = '#00FFFF' if i % 2 == 0 else '#FF00FF'
        ax2.scatter(theta_rad, r, color=color, s=120, edgecolors='white')
        
    ax2.set_thetagrids([45, 225], labels=['Phase A (45°)', 'Phase B (225°)'], color='white')
    ax2.set_title("Sultanian Top-Down View\n(Phase-Lock Alignment)", color='white', fontsize=14)
    ax2.tick_params(colors='white')
    ax2.grid(alpha=0.2)

    plt.tight_layout()
    plt.show()

render_dual_space_comparison(gammas)
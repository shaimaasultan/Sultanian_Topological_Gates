import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sultanian Core Parameters ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)
OCTA_PHASE = 22.5  # Fundamental Sultanian Unit (2023 Paper)

# Dataset (First 12 Zeros)
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 
          40.9187, 43.3271, 48.0052, 49.7738, 52.8935, 56.4462]

def render_sultanian_lattice():
    fig = plt.figure(figsize=(4, 4), facecolor='#0b0f19')
    
    # 1. Minkowski Spacetime Lattice (Side View)
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_facecolor('#0b0f19')
    z_range = np.linspace(0, 30, 100)
    r_limit = R_GROUND + SIGMA * z_range

    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        
        # Plot the 8-Sector Lattice at this energy level
        for sector in range(8):
            angle_deg = sector * OCTA_PHASE
            x_proj = r_n * np.cos(np.radians(angle_deg))
            
            # If it's a 45/225 degree harmonic, it's an "Occupied Zero"
            if angle_deg in [45, 225]:
                color = '#00FFFF' if angle_deg == 45 else '#FF00FF'
                ax1.scatter(x_proj if i%2==0 else -x_proj, z_n, color=color, s=100, edgecolors='white', zorder=5)
            # Otherwise, it's a "Ghost Dot" (Unoccupied Resonance)
            else:
                ax1.scatter(x_proj, z_n, color='white', alpha=0.05, s=20, marker='.')
                ax1.scatter(-x_proj, z_n, color='white', alpha=0.05, s=20, marker='.')

    ax1.set_title("Minkowski Lattice: Occupied vs. Ghost States", color='white', fontsize=14)
    ax1.set_xlabel("Radial Projection", color='white')
    ax1.set_ylabel("Sultanian Energy (Z)", color='white')
    ax1.tick_params(colors='white')

    # 2. Top-Down Octa-Phase Spiral (The "Lattice" View)
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.set_facecolor('#0b0f19')
    
    # Draw all 8 Radial Rays
    angles = np.arange(0, 360, OCTA_PHASE)
    ax2.set_thetagrids(angles, color='white', fontsize=9, alpha=0.5)
    
    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        
        # Draw Ghost Dots for all 8 sectors at every R_n
        for ang in angles:
            ax2.scatter(np.radians(ang), r_n, color='white', alpha=0.1, s=15)
            
        # Draw the Actual Zeros on top
        theta_n = np.radians(45 + (i * 180))
        color = '#00FFFF' if i % 2 == 0 else '#FF00FF'
        ax2.scatter(theta_n, r_n, color=color, s=120, edgecolors='white', zorder=10)

    ax2.set_title("Octa-Phase Lattice Alignment (22.5° Steps)", color='white', fontsize=14)
    ax2.grid(True, color='gray', alpha=0.2)
    ax2.tick_params(colors='white')

    plt.suptitle("Sultanian Duality: The 8-Sector Lattice Proof", color='gold', fontsize=18, y=0.9)
    plt.tight_layout()
    plt.show()

render_sultanian_lattice()
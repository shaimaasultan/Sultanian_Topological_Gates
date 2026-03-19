import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Parameters ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 0.15          # The "Widening" Change Rate (Adjust to match your image)
R_GROUND = np.exp(L_OLD) # Initial Ground Radius (~7.36)

# --- 2. Input Zeros (First 15 for visual clarity) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738, 
          52.89, 56.44, 59.34, 60.83, 63.32]

def render_conhelix(zeros):
    fig = plt.figure(figsize=(12, 12), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # --- 3. Generate Expanding Helix Path ---
    # We use a high-resolution theta range for the gold path
    theta_cont = np.linspace(0, 15 * np.pi, 3000)
    # Radius expands linearly with theta (The Conhelix Equation)
    r_cont = R_GROUND + (SIGMA * theta_cont)
    z_cont = L_OLD * (theta_cont / np.pi)
    
    ax.plot(r_cont * np.cos(theta_cont), r_cont * np.sin(theta_cont), z_cont, 
            color='gold', alpha=0.3, linewidth=1.5, label='Expanding Sultanian Manifold')

    # --- 4. Map Zeros with Binary Phase Rotation (45° + n*180°) ---
    for i, g in enumerate(zeros):
        # Calculate Height based on original Gamma
        z_n = L_OLD * (g / 4) # Keeping Z consistent with your helical pitch
        
        # Calculate Expanding Radius at this level
        r_n = R_GROUND + (SIGMA * (g * np.pi / 4))
        
        # Apply the Multiples of 45° + n*180° Rule
        # Level 1, 3, 5... -> 45° | Level 2, 4, 6... -> 225°
        theta_n = np.radians(45 + (i * 180))
        
        # Plot the Aligned Zero (Cyan)
        ax.scatter(r_n * np.cos(theta_n), r_n * np.sin(theta_n), z_n, 
                   color='#00FFFF', s=100, edgecolors='white', depthshade=False)
        
        # Draw "Projection Line" from Center to Zero to show alignment
        ax.plot([0, r_n * np.cos(theta_n)], [0, r_n * np.sin(theta_n)], [z_n, z_n], 
                color='white', alpha=0.2, linestyle='--')

    # --- 5. Aesthetics & Orientation ---
    ax.set_title(f"Sultanian Conhelix: Widening Proof (σ={SIGMA})", color='white', fontsize=16)
    ax.view_init(elev=30, azim=45) # 3D perspective
    # To see the "Top-Down" match your image, change view_init to (90, 45)
    
    ax.set_axis_off()
    plt.legend(loc='upper left', frameon=False, labelcolor='white')
    plt.show()

if __name__ == "__main__":
    render_conhelix(gammas)
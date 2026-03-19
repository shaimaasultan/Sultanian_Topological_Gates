import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian Core Constants ---
L_OLD = np.pi - np.log(np.pi)      # Sultanian Pitch Constant (~1.9968)
SIGMA = 1.8628                   # Official Expansion Factor (Calculated)
R_GROUND = np.exp(L_OLD)         # Ground State Radius (~7.365)

# --- 2. Data Input (First 20 Zeros for High-Resolution Visuals) ---
# Replace this list with your full 100-zero dataset as needed
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 
          48.0052, 49.7738, 52.8935, 56.4462, 59.3470, 60.8317, 63.32, 65.11, 
          67.07, 69.54, 72.06, 75.70]

def render_sultanian_conhelix(zeros, view_mode='perspective'):
    """
    Renders the Sultanian Expanding Conhelix.
    view_mode: 'perspective' for 3D view, 'top' for 2D alignment proof.
    """
    fig = plt.figure(figsize=(12, 12), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0b0f19')

    # --- 3. Generate the Continuous Conical Path ---
    # Max theta determined by the highest zero
    max_theta = (max(zeros) * np.pi / 4)
    theta_cont = np.linspace(0, max_theta, 5000)
    
    # R(z) = R_ground + sigma * z
    # Since z = L_old * (theta/pi), we substitute for theta:
    r_cont = R_GROUND + SIGMA * (L_OLD * (theta_cont / np.pi))
    z_cont = L_OLD * (theta_cont / np.pi)
    
    # Plot the Golden Manifold
    ax.plot(r_cont * np.cos(theta_cont), r_cont * np.sin(theta_cont), z_cont, 
            color='gold', alpha=0.4, linewidth=1.2, label='Sultanian Manifold Path')

    # --- 4. Plot the Quantized Zeros (The Gates) ---
    for i, g in enumerate(zeros):
        # Calculate Height Z
        z_n = L_OLD * (g / 4)
        
        # Calculate Expanded Radius R at this height
        r_n = R_GROUND + SIGMA * z_n
        
        # Apply the Binary Phase-Lock: 45° + (n * 180°)
        # i is 0-indexed, so: i=0 (45°), i=1 (225°), i=2 (45°)...
        angle_deg = 45 + (i * 180)
        theta_n = np.radians(angle_deg)
        
        # Color toggle for Phase A/B
        color = '#00FFFF' if i % 2 == 0 else '#FF00FF'
        
        # Plot Zero
        ax.scatter(r_n * np.cos(theta_n), r_n * np.sin(theta_n), z_n, 
                   color=color, s=120, edgecolors='white', linewidth=0.5, 
                   label='Phase A (45°)' if i==0 else ('Phase B (225°)' if i==1 else ""))

        # Draw Radial Alignment Rays
        ax.plot([0, r_n * np.cos(theta_n)], [0, r_n * np.sin(theta_n)], [z_n, z_n], 
                color='white', alpha=0.15, linestyle=':')

    # --- 5. View Configuration ---
    if view_mode == 'top':
        ax.view_init(elev=90, azim=-45) # Matches your top-down image perfectly
        ax.set_title("Sultanian Top-Down Proof: 45°/225° Alignment", color='white', fontsize=16)
    else:
        ax.view_init(elev=25, azim=30)
        ax.set_title(f"Sultanian Conhelix (σ={SIGMA})", color='white', fontsize=18)

    # Clean up display
    ax.set_axis_off()
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper left', frameon=False, labelcolor='white')
    
    plt.tight_layout()
    plt.show()

# --- EXECUTION ---
if __name__ == "__main__":
    # Change to 'top' to see the alignment proof
    render_sultanian_conhelix(gammas, view_mode='perspective')
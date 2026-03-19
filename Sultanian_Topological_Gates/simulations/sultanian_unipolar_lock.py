import numpy as np
import matplotlib.pyplot as plt

# Sultanian Constants
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)

# Dataset (First 16 Zeros)
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 
          48.0052, 49.7738, 52.8935, 56.4462, 59.3470, 60.8317, 63.3200, 65.1100]

def plot_unipolar_manifold():
    fig = plt.figure(figsize=(16, 8), facecolor='#0b0f19')
    
    # 1. 3D Conhelix - Unipolar Mapping (All on one vector)
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.set_facecolor('#0b0f19')
    
    # Manifold Surface (A single ray expansion)
    z_cont = np.linspace(0, 35, 100)
    r_cont = R_GROUND + SIGMA * z_cont
    theta_fixed = np.radians(45)
    ax1.plot(r_cont * np.cos(theta_fixed), r_cont * np.sin(theta_fixed), z_cont, 
             color='gold', alpha=0.5, linewidth=2, label='Sultanian 45° Vector')
    
    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        # Unipolar Logic: 45 + n*360 (Always 45 degrees)
        x_n = r_n * np.cos(theta_fixed)
        y_n = r_n * np.sin(theta_fixed)
        ax1.scatter(x_n, y_n, z_n, color='#00FFFF', s=80, edgecolors='white', depthshade=False)

    ax1.set_axis_off()
    ax1.set_title("Unipolar Minkowski Conhelix (45° Locked)", color='white', pad=20)

    # 2. Top-Down Unipolar View
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.set_facecolor('#0b0f19')
    
    # Draw the 45 degree vector
    ax2.plot([theta_fixed, theta_fixed], [0, max(r_n for r_n in [R_GROUND + SIGMA * L_OLD * (g/4) for g in gammas])], 
             color='gold', alpha=0.3, linestyle='--')
    
    # Draw all 8 Sectors (Ghost States)
    angles = np.arange(0, 360, 22.5)
    ax2.set_thetagrids(angles, color='white', alpha=0.5)

    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        # Every zero locks exactly at 45 degrees
        ax2.scatter(theta_fixed, r_n, color='#00FFFF', s=100, edgecolors='white', zorder=10)

    ax2.set_title("Unipolar Phase Lock (45° + n*360°)", color='white', pad=20)
    ax2.tick_params(colors='white')
    ax2.grid(True, color='gray', alpha=0.2)

    plt.suptitle("Sultanian Duality: Unipolar Convergence & Scale Invariance", color='gold', fontsize=18)
    plt.tight_layout()
    plt.show()

plot_unipolar_manifold()
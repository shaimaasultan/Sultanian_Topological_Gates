import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sultanian Core Parameters ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)
OCTA_PHASE = 22.5  # From your 2023 Paper

# Zeros Data
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271]

def plot_octaphase_minkowski():
    fig = plt.figure(figsize=(16, 8), facecolor='#0b0f19')
    
    # Left: Minkowski Octa-Sector View
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_facecolor('#0b0f19')
    z_range = np.linspace(0, 25, 100)
    r_limit = R_GROUND + SIGMA * z_range
    
    # Draw Octa-Phase "Light Cone" Boundaries
    for angle in [22.5, 45, 67.5, 90]:
        factor = np.sin(np.radians(angle))
        ax1.plot(r_limit * factor, z_range, color='gold', alpha=0.2, linestyle='--')
        ax1.plot(-r_limit * factor, z_range, color='gold', alpha=0.2, linestyle='--')

    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        ax1.scatter(r_n if i%2==0 else -r_n, z_n, color='#00FFFF', s=100, edgecolors='white')

    ax1.set_title("Minkowski-Sultanian Octa-Phase Space", color='white')
    ax1.tick_params(colors='white')

    # Right: Top-Down Octa-Phase Spiral
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.set_facecolor('#0b0f19')
    
    # Draw all 8 Octa-Phase Sectors (22.5 degree intervals)
    angles = np.arange(0, 360, 22.5)
    ax2.set_thetagrids(angles, color='white', fontsize=8)
    
    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        # 2023 Paper Logic: Alignment at harmonics of 22.5
        theta_n = np.radians(45 + (i * 180)) 
        ax2.scatter(theta_n, r_n, color='#FF00FF', s=100, edgecolors='white')
        
    ax2.set_title("Octa-Phase Resonance (2023 Identity)", color='white')
    ax2.tick_params(colors='white')
    plt.tight_layout()
    plt.show()

plot_octaphase_minkowski()
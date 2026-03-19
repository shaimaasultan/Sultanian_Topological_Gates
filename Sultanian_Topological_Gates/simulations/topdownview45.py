import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)
TARGET_ANGLE = np.deg2rad(45)

# --- 2. Input Data (First 10 Zeros) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

def plot_radial_45_alignment(zeros):
    fig = plt.figure(figsize=(10, 10), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#0b0f19')

    # 1. Calculate Radii (The Energy Scale)
    radii = [np.sqrt(0.25 + g**2) for g in zeros]

    # 2. Plot the Zeros on the 45-Degree Ray
    ax.scatter([TARGET_ANGLE]*len(radii), radii, 
               color='#00F5FF', s=120, edgecolors='white', 
               label='Aligned Topological Gates', zorder=5)

    # 3. Draw the "Phase-Locked" Ray
    ax.plot([TARGET_ANGLE, TARGET_ANGLE], [0, max(radii)*1.1], 
            color='gold', linewidth=2, alpha=0.6, label='45° Resonance Ray')

    # 4. Optional: Show the Original Spiral for Comparison (Ghost)
    theta_spiral = np.linspace(0, max(zeros)*(np.pi/4), 1000)
    r_spiral = np.sqrt(0.25 + (theta_spiral / (np.pi/4))**2)
    ax.plot(theta_spiral, r_spiral, color='gold', linestyle=':', alpha=0.1)

    # Formatting
    ax.set_title("Sultanian Top-Down View: 45° Phase Alignment", color='white', fontsize=16, pad=30)
    ax.set_rscale('log') # Log scale helps see the spacing of higher zeros
    ax.grid(True, color='gray', alpha=0.3, linestyle='--')
    ax.tick_params(colors='white', labelsize=10)
    
    # Customize the 45-degree grid line
    ax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315])
    
    plt.legend(loc='upper right', frameon=False, labelcolor='white')
    plt.show()

if __name__ == "__main__":
    plot_radial_45_alignment(gammas)
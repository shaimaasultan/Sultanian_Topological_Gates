import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi) 
PHASE_SHIFT_BASE = np.pi / 4  # The 45° Baseline
TRANSFORM_SHIFT = np.radians(45) # The Transformation (+45°)
R_SHELL = np.exp(L_OLD)

# --- 2. Input Data (First 10 Zeros) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

def plot_sultanian_transformation(zeros):
    fig = plt.figure(figsize=(14, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # --- 3. Generate Continuous Helix ---
    gamma_cont = np.linspace(min(zeros), max(zeros) + 5, 2000)
    theta_path = gamma_cont * PHASE_SHIFT_BASE
    z_path = L_OLD * (theta_path / np.pi)
    ax.plot(R_SHELL * np.cos(theta_path), R_SHELL * np.sin(theta_path), z_path, 
            color='gold', alpha=0.3, linewidth=1, label='Sultanian Manifold')

    # --- 4. Plot Original Zeros (Cyan) ---
    theta_orig = np.array(zeros) * PHASE_SHIFT_BASE
    z_orig = L_OLD * (theta_orig / np.pi)
    ax.scatter(R_SHELL * np.cos(theta_orig), R_SHELL * np.sin(theta_orig), z_orig, 
               color='#00FFFF', s=100, marker='D', edgecolors='white', label='Original Zeros')

    # --- 5. Plot Transformed Zeros (Magenta) ---
    # Shift angle by +45 degrees
    theta_trans = theta_orig + TRANSFORM_SHIFT
    # Note: In the Sultanian Protocol, Z height is tied to the phase angle
    z_trans = L_OLD * (theta_trans / np.pi) 
    
    ax.scatter(R_SHELL * np.cos(theta_trans), R_SHELL * np.sin(theta_trans), z_trans, 
               color='#FF00FF', s=100, marker='o', edgecolors='white', label='Transformed (+45°)')

    # --- 6. Draw Transformation Vectors (The "Slide") ---
    for i in range(len(zeros)):
        ax.plot([R_SHELL * np.cos(theta_orig[i]), R_SHELL * np.cos(theta_trans[i])],
                [R_SHELL * np.sin(theta_orig[i]), R_SHELL * np.sin(theta_trans[i])],
                [z_orig[i], z_trans[i]], color='white', linestyle='--', alpha=0.5)

    # Formatting
    ax.set_title("Sultanian Transformation: 45° Phase Shift Analysis", color='white', fontsize=16)
    ax.set_box_aspect((1, 1, 2))
    ax.view_init(elev=25, azim=45)
    ax.axis('off')
    ax.legend(loc='upper left', frameon=False, labelcolor='white')

    plt.show()

if __name__ == "__main__":
    plot_sultanian_transformation(gammas)
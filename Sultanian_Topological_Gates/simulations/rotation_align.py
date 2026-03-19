import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi) 
R_SHELL = np.exp(L_OLD)
TARGET_ANGLE_DEG = 45
TARGET_ANGLE_RAD = np.radians(TARGET_ANGLE_DEG)

# --- 2. Data (First 10 Zeros) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

def plot_sultanian_alignment(zeros):
    fig = plt.figure(figsize=(12, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # Calculate Current Angles
    theta_orig = np.array(zeros) * (np.pi / 4)
    z_orig = L_OLD * (theta_orig / np.pi)

    # 1. Plot Original Positions (Cyan Diamonds)
    ax.scatter(R_SHELL * np.cos(theta_orig), R_SHELL * np.sin(theta_orig), z_orig, 
               color='#00FFFF', s=80, marker='D', alpha=0.4, label='Original Position')

    # 2. Plot Aligned Positions (Magenta Circles)
    # Every zero is now at TARGET_ANGLE_RAD, but at its UNIQUE Z height
    ax.scatter(R_SHELL * np.cos(TARGET_ANGLE_RAD), R_SHELL * np.sin(TARGET_ANGLE_RAD), z_orig, 
               color='#FF00FF', s=100, marker='o', edgecolors='white', label='Aligned to 45°')

    # 3. Draw "Alignment Guides"
    # Showing the rotation from original to 45 degrees
    for i in range(len(zeros)):
        # Create an arc for each zero to show the rotation path
        arc_theta = np.linspace(theta_orig[i], TARGET_ANGLE_RAD, 50)
        ax.plot(R_SHELL * np.cos(arc_theta), R_SHELL * np.sin(arc_theta), z_orig[i], 
                color='white', linestyle=':', alpha=0.3)

    # Formatting
    ax.set_title(f"Sultanian Alignment: All Zeros Synced to {TARGET_ANGLE_DEG}°", color='white', fontsize=16)
    ax.view_init(elev=30, azim=20)
    ax.set_axis_off()
    ax.legend(loc='upper left', frameon=False, labelcolor='white')

    plt.show()

if __name__ == "__main__":
    plot_sultanian_alignment(gammas)
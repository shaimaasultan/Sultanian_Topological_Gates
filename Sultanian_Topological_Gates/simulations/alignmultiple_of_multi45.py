import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi) 
R_SHELL = np.exp(L_OLD)
HARMONIC_STEP = 45 # Degrees

# --- 2. Data (Simulating 100 Zeros for the Full Effect) ---
# Use your actual 100-zero list here
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738]
for i in range(11, 101):
    gammas.append(gammas[-1] + 2.5) # Simulated spacing

def plot_harmonic_alignment(zeros):
    fig = plt.figure(figsize=(14, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # Calculate Current States
    theta_orig = np.array(zeros) * (np.pi / 4)
    z_heights = L_OLD * (theta_orig / np.pi)

    # 3. Calculate Harmonic Targets
    # Each zero (i) snaps to the next 45-degree multiple
    harmonic_indices = np.arange(len(zeros))
    theta_harmonics = np.radians((harmonic_indices * HARMONIC_STEP) % 360)

    # 4. Plot original continuous path (Ghost Gold)
    gamma_cont = np.linspace(min(zeros), max(zeros), 2000)
    ax.plot(R_SHELL * np.cos(gamma_cont * (np.pi/4)), 
            R_SHELL * np.sin(gamma_cont * (np.pi/4)), 
            L_OLD * (gamma_cont * 0.25), color='gold', alpha=0.1)

    # 5. Plot the Harmonic "Quantized" Zeros
    # Colors cycle through the 8 harmonic positions (360/45)
    colors = plt.cm.hsv(np.linspace(0, 1, 8))
    
    for i in range(len(zeros)):
        target_color = colors[i % 8]
        # These zeros now sit on 8 distinct vertical pillars
        ax.scatter(R_SHELL * np.cos(theta_harmonics[i]), 
                   R_SHELL * np.sin(theta_harmonics[i]), 
                   z_heights[i], 
                   color=target_color, s=50, edgecolors='white', alpha=0.8)

    # 6. Draw the 8 Vertical "Resonance Pillars"
    for angle in range(0, 360, 45):
        rad = np.radians(angle)
        ax.plot([R_SHELL * np.cos(rad), R_SHELL * np.cos(rad)],
                [R_SHELL * np.sin(rad), R_SHELL * np.sin(rad)],
                [0, max(z_heights)], color='white', alpha=0.1, linestyle='--')

    # Formatting
    ax.set_title("Sultanian Harmonic Quantization: 8-Phase Resonance (45° Multiples)", color='white', fontsize=16)
    ax.view_init(elev=30, azim=45)
    ax.set_axis_off()
    plt.show()

if __name__ == "__main__":
    plot_harmonic_alignment(gammas)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)  # The Thread Pitch (~1.9968)
PHASE_SHIFT = np.pi / 4         # The 45-Degree Perspective
R_SHELL = np.exp(L_OLD)        # The Constant Radial Shell

# --- 2. Input Data: First 100 Zeta Zeros (Gamma) & First 100 Primes ---
# (A complete dataset of 100 zeros and 100 primes is required)
zeta_zeros = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    52.970321, 56.446248, 59.347033, 60.831779, 65.112544,
    67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
    # ... continue to 100 zeros
]

# (A function or database is needed to provide the first 100 primes)
# Assume first_100_primes is a list [2, 3, 5, ..., 541]
import sympy # sympy is excellent for generating primes
primes = list(sympy.primerange(2, sympy.prime(100) + 1))

def plot_sultanian_helix_with_prime_projections(zeros, primes):
    # Setup Figure and 3D Axes
    fig = plt.figure(figsize=(14, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # --- 3. Generate the Continuous Helix Path (The String) ---
    gamma_continuous = np.linspace(min(zeros), max(zeros), 2000)
    theta_path = gamma_continuous * PHASE_SHIFT
    x_path = R_SHELL * np.cos(theta_path)
    y_path = R_SHELL * np.sin(theta_path)
    z_path = L_OLD * (theta_path / np.pi)

    # Plot the Golden Helix Line
    ax.plot(x_path, y_path, z_path, color='#DAA520', linewidth=2, alpha=0.7, label='Sultanian Helix Path')

    # --- 4. Map the Discrete Zeros (The Gates) ---
    theta_nodes = np.array(zeros) * PHASE_SHIFT
    x_nodes = R_SHELL * np.cos(theta_nodes)
    y_nodes = R_SHELL * np.sin(theta_nodes)
    z_nodes = L_OLD * (theta_nodes / np.pi)

    # Plot Zeros as Cyan Diamonds (Gates)
    ax.scatter(x_nodes, y_nodes, z_nodes, color='#00FFFF', s=100, 
               edgecolors='white', marker='D', depthshade=False, label='Topological Gates (Zeros)')

    # --- 5. Prime Projections (The Shadows) ---
    # We project the Primes onto the Z=0 plane (the base)
    # The Primes provide the logarithmic scaling pulse on the angle
    # theta_primes = np.log(primes) * PHASE_SHIFT  <-- This needs calibration to match gamma range
    # Let's map them proportionally across the total rotation.
    
    total_rotations = (theta_nodes[-1] - theta_nodes[0]) / (2 * np.pi)
    theta_primes = np.linspace(theta_nodes[0], theta_nodes[-1], len(primes))
    
    x_primes = R_SHELL * np.cos(theta_primes)
    y_primes = R_SHELL * np.sin(theta_primes)
    z_primes = np.zeros_like(x_primes) # Flat on the Z=0 plane

    # Plot Primes as Red 'X' projections
    ax.scatter(x_primes, y_primes, z_primes, color='#FF4500', s=80, 
               marker='x', depthshade=False, label='Prime Harmonic Projections')

    # --- 6. Aesthetic Formatting (Matching previous style) ---
    ax.set_title("Sultanian Duality: Helix Gates & Prime Projections", color='white', fontsize=18, pad=30)
    
    # Axes color and labels
    for axis, label in zip([ax.xaxis, ax.yaxis, ax.zaxis], ["Radial Shell (X)", "Radial Shell (Y)", "Vertical Propulsion (Z)"]):
        axis.label.set_color('white')
        axis.set_tick_params(colors='gray')
        axis.set_label_text(label)

    # Stretching the helix vertically
    ax.set_box_aspect((1, 1, 2)) 
    
    # Remove background panes for a clean "floating" look
    for pane in [ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane]:
        pane.set_edgecolor('black')
        pane.fill = False

    ax.legend(loc='upper left', frameon=False, labelcolor='white')
    ax.view_init(elev=20, azim=45)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Ensure you have extracted 100 zeros from the provided image/list
    plot_sultanian_helix_with_prime_projections(zeta_zeros, primes)
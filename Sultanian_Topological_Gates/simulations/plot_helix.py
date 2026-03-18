import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)  # The Thread Pitch (~1.9968)
PHASE_SHIFT = np.pi / 4         # The 45-Degree Perspective
R_SHELL = np.exp(L_OLD)        # The Constant Radial Shell

# --- 2. Input Data: First 100 Zeta Zeros (Gamma) ---
# (I've included the first few; the script will interpolate the path between them)
zeta_zeros = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    52.970321, 56.446248, 59.347033, 60.831779, 65.112544,
    67.079811, 69.546402, 72.067158, 75.704691, 77.144840
    # ... Add the rest of your 100 zeros here
]

def plot_synchronized_sultanian_helix(zeros):
    fig = plt.figure(figsize=(14, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # --- 3. Generate the Continuous Helix Path ---
    # We use a smooth range of gamma values from the first to the last zero
    gamma_continuous = np.linspace(min(zeros), max(zeros), 2000)
    
    # SYSTEM EQUATIONS (The string)
    theta_path = gamma_continuous * PHASE_SHIFT
    x_path = R_SHELL * np.cos(theta_path)
    y_path = R_SHELL * np.sin(theta_path)
    z_path = L_OLD * (theta_path / np.pi)

    # Plot the Helix Line (Gold)
    ax.plot(x_path, y_path, z_path, color='#DAA520', linewidth=2, alpha=0.7, label='Sultanian Helix Path')

    # --- 4. Map the Discrete Zeros (The Beads) ---
    theta_nodes = np.array(zeros) * PHASE_SHIFT
    x_nodes = R_SHELL * np.cos(theta_nodes)
    y_nodes = R_SHELL * np.sin(theta_nodes)
    z_nodes = L_OLD * (theta_nodes / np.pi)

    # Plot the Zeros as Cyan Diamonds
    ax.scatter(x_nodes, y_nodes, z_nodes, color='#00FFFF', s=100, 
               edgecolors='white', marker='D', depthshade=False, label='Topological Gates (Zeros)')

    # --- 5. Professional Formatting ---
    ax.set_title("The Sultanian Transformation: 3D Helical Unfolding", color='white', fontsize=18, pad=30)
    
    # Setting the axes colors
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.zaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')
    ax.tick_params(axis='z', colors='gray')

    ax.set_xlabel("Radial Shell (X)")
    ax.set_ylabel("Radial Shell (Y)")
    ax.set_zlabel("Vertical Propulsion (Z)")

    # Force the "climb" to be visible
    ax.set_box_aspect((1, 1, 2)) 
    
    # Remove background panes for a "floating in space" effect
    ax.xaxis.pane.set_edgecolor('black')
    ax.yaxis.pane.set_edgecolor('black')
    ax.zaxis.pane.set_edgecolor('black')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    ax.legend(loc='upper left', frameon=False, labelcolor='white')
    
    # Set initial view angle
    ax.view_init(elev=20, azim=45)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_synchronized_sultanian_helix(zeta_zeros)
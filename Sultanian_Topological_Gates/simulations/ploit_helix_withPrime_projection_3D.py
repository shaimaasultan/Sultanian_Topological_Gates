import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi) 
PHASE_SHIFT = np.pi / 4        
R_SHELL_ZETA = np.exp(L_OLD)    # Outer Shell (Zeros)
R_SHELL_PRIME = R_SHELL_ZETA * 0.8  # Inner Core (Primes)

# --- 2. Data Preparation (First 100) ---
zeta_zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.327073] # ... use your 100
primes = list(sympy.primerange(2, sympy.prime(len(zeta_zeros)) + 1))

def plot_3d_intertwined_helix(zeros, primes):
    fig = plt.figure(figsize=(14, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # --- 3. THE ZETA HELIX (External) ---
    gamma_range = np.linspace(min(zeros), max(zeros), 1000)
    theta_zeta = gamma_range * PHASE_SHIFT
    z_zeta = L_OLD * (theta_zeta / np.pi)
    
    ax.plot(R_SHELL_ZETA * np.cos(theta_zeta), 
            R_SHELL_ZETA * np.sin(theta_zeta), 
            z_zeta, color='#DAA520', alpha=0.4, label='Zeta Manifold Path')

    # Zeta Nodes (Gates)
    theta_z_nodes = np.array(zeros) * PHASE_SHIFT
    ax.scatter(R_SHELL_ZETA * np.cos(theta_z_nodes), 
               R_SHELL_ZETA * np.sin(theta_z_nodes), 
               L_OLD * (theta_z_nodes / np.pi), 
               color='#00FFFF', s=100, marker='D', label='Topological Gates')

    # --- 4. THE PRIME HELIX (Internal Core) ---
    # We map primes to the Z-axis based on their natural log progression
    # This shows the "Pulse" that drives the outer helix
    theta_p_nodes = np.linspace(theta_z_nodes[0], theta_z_nodes[-1], len(primes))
    z_p_nodes = L_OLD * (theta_p_nodes / np.pi)

    # Plot the Prime Helix Line
    ax.plot(R_SHELL_PRIME * np.cos(theta_p_nodes), 
            R_SHELL_PRIME * np.sin(theta_p_nodes), 
            z_p_nodes, color='#FF4500', alpha=0.5, linestyle='--')

    # Prime Nodes (Propulsion)
    ax.scatter(R_SHELL_PRIME * np.cos(theta_p_nodes), 
               R_SHELL_PRIME * np.sin(theta_p_nodes), 
               z_p_nodes, color='#FF4500', s=50, marker='x', label='Prime Propulsion Nodes')

    # --- 5. Connecting "Resonance Lines" ---
    # Draw lines between each prime and its corresponding zeta zone
    # This illustrates the "Sultanian Duality"
    for i in range(len(zeros)):
        ax.plot([R_SHELL_PRIME * np.cos(theta_p_nodes[i]), R_SHELL_ZETA * np.cos(theta_z_nodes[i])],
                [R_SHELL_PRIME * np.sin(theta_p_nodes[i]), R_SHELL_ZETA * np.sin(theta_z_nodes[i])],
                [z_p_nodes[i], z_p_nodes[i]], color='white', alpha=0.2, linewidth=1)

    # Formatting
    ax.set_title("Sultanian 3D Duality: Intertwined Prime-Zeta Manifold", color='white', fontsize=18)
    ax.set_box_aspect((1, 1, 2))
    ax.view_init(elev=30, azim=45)
    ax.axis('off') # Clean look for the paper
    ax.legend(loc='upper left', frameon=False, labelcolor='white')

    plt.show()

plot_3d_intertwined_helix(zeta_zeros, primes)
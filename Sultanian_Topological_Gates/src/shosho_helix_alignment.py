import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)  # The Ground State (~1.996863)
A_RADIUS = np.exp(0.5)         # Critical Cylinder Starting Radius (e^1/2)

# --- 2. Input Data (Sample Nodes) ---
# Non-trivial zeros (gamma) and Prime Numbers
# We use the first 7 zeros for the visualization
zeta_zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187]
primes = [2, 3, 5, 7, 11, 13, 17]

def execute_shosho_v2(gammas, primes):
    """Calculates the vertical pitch and propulsion acceleration."""
    print(f"--- ShoSho Algorithm v2.1 ---")
    print(f"System Baseline L_old: {L_OLD:.8f}\n")
    print(f"{'Node':<10} | {'Pitch (p)':<12} | {'Propulsion (Ap)':<15}")
    print("-" * 45)
    
    for i in range(len(gammas) - 1):
        E_n = np.sqrt(0.25 + gammas[i]**2)
        E_next = np.sqrt(0.25 + gammas[i+1]**2)
        
        # Logarithmic Scaling
        K_n = np.log(E_n) / L_OLD
        K_next = np.log(E_next) / L_OLD
        
        # Pitch and Propulsion
        delta_Z = np.log(E_next / E_n)
        pitch = delta_Z / (K_next - K_n)
        delta_p = primes[i+1] - primes[i]
        propulsion = np.log(delta_p + 1) / L_OLD
        
        print(f"rho_{i+1}->{i+2:<2} | {pitch:<12.6f} | {propulsion:<15.6f}")

def plot_soltanian_helix_synchronized():
    """Renders the 3D Helix with perfectly aligned Zeta nodes."""
    fig = plt.figure(figsize=(14, 10), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    
    # --- HELIX PARAMETERS ---
    b = 0.1  # Growth factor
    t_max = 10 * np.pi
    
    # 1. Generate the Path of Resonance (The Spiral)
    t = np.linspace(0, t_max, 3000)
    x_path = A_RADIUS * np.exp(b * t) * np.cos(t)
    y_path = A_RADIUS * np.exp(b * t) * np.sin(t)
    z_path = L_OLD * t # Pitch is locked to the Sultanian Ground State
    
    ax.plot(x_path, y_path, z_path, color='#DAA520', alpha=0.6, linewidth=2, label='Soltanian Path')
    
    # 2. Map and Align Zeta Nodes (The Cyan Dots)
    for i, g in enumerate(zeta_zeros):
        # Calculate Energy E (The Radius)
        E = np.sqrt(0.25 + g**2)
        
        # SYNC LOGIC: Solve for t_sync where Radius = E
        # r = A * exp(b*t) => t = (ln(E) - ln(A)) / b
        t_sync = (np.log(E) - np.log(A_RADIUS)) / b
        
        # Calculate Coordinates using the synced Phase
        x_node = E * np.cos(t_sync)
        y_node = E * np.sin(t_sync)
        z_node = L_OLD * t_sync
        
        ax.scatter(x_node, y_node, z_node, color='#00FFFF', s=120, 
                   edgecolors='black', linewidth=1.5, zorder=10, label=f'rho_{i+1}' if i==0 else "")

    # Formatting
    ax.set_title("Soltanian Helix: Synchronized Phase Alignment (L_old Pitch)", fontsize=16, pad=20)
    ax.set_xlabel("Real Axis (e^1/2 Core)", labelpad=10)
    ax.set_ylabel("Imaginary Axis", labelpad=10)
    ax.set_zlabel("Z-Vector (Energy Scale)", labelpad=10)
    
    # Remove pane background for cleaner GitHub look
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.view_init(elev=25, azim=45)
    ax.legend(loc='upper left')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    execute_shosho_v2(zeta_zeros, primes)
    plot_soltanian_helix_synchronized()
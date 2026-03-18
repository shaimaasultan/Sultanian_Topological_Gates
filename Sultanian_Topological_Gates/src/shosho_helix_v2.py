import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)  # The Ground State (~1.996863)
E_CRITICAL_RADIUS = np.exp(0.5) # e^1/2 (~1.6487)

# --- 2. Input Data (Sample Nodes) ---
# Non-trivial zeros (gamma) and Prime Numbers
zeta_zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187]
primes = [2, 3, 5, 7, 11, 13, 17]

def execute_shosho_v2(gammas, primes):
    """
    Core ShoSho Algorithm: Calculates the vertical pitch and prime propulsion.
    """
    print(f"{'Node':<10} | {'Pitch (p)':<12} | {'Propulsion (Ap)':<15} | {'K-Scale':<8}")
    print("-" * 55)
    
    for i in range(len(gammas) - 1):
        # Energy Shell Calculation (Euclidean Norm)
        E_n = np.sqrt(0.25 + gammas[i]**2)
        E_next = np.sqrt(0.25 + gammas[i+1]**2)
        
        # Z-Vector Displacement
        delta_Z = np.log(E_next / E_n)
        
        # Resonance Scaling
        K_n = np.log(E_n) / L_OLD
        K_next = np.log(E_next) / L_OLD
        
        # Pitch Sync and Prime Propulsion
        pitch = delta_Z / (K_next - K_n)
        delta_p = primes[i+1] - primes[i]
        propulsion = np.log(delta_p + 1) / L_OLD
        
        print(f"rho_{i+1}->{i+2:<2} | {pitch:<12.6f} | {propulsion:<15.6f} | {K_n:.4f}")

# --- 3. 3D Helix Visualization ---
def plot_soltanian_helix():
    fig = plt.figure(figsize=(12, 8), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate Helical Path
    t = np.linspace(0, 10 * np.pi, 1000)
    b = 0.05  # Growth factor
    pitch_vis = 2.0 # Vertical spacing
    
    x = E_CRITICAL_RADIUS * np.exp(b * t) * np.cos(t)
    y = E_CRITICAL_RADIUS * np.exp(b * t) * np.sin(t)
    z = pitch_vis * t
    
    ax.plot(x, y, z, color='#DAA520', alpha=0.7, label='Soltanian Helix (L_old Pitch)')
    
    # Plot Zeta Nodes (Zeros)
    for g in zeta_zeros:
        E = np.sqrt(0.25 + g**2)
        theta = (np.log(E) - L_OLD) / b
        ax.scatter(E * np.cos(theta), E * np.sin(theta), pitch_vis * theta, 
                   color='#00FFFF', s=50, edgecolors='black')

    ax.set_title("Soltanian Helix: 3D Resonance Mapping", fontsize=14)
    ax.set_xlabel("Real (E_critical)")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("Z-Vector (Energy Scale)")
    ax.legend()
    plt.show()

def plot_soltanian_helix_aligned():
    fig = plt.figure(figsize=(12, 8), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. Constants
    b = 0.05  # Growth factor (must be consistent)
    a = np.exp(0.5) # Starting Radius (Critical Cylinder)
    
    # 2. Generate the "Path of Resonance" (The Spiral)
    t = np.linspace(0, 10 * np.pi, 2000)
    x_path = a * np.exp(b * t) * np.cos(t)
    y_path = a * np.exp(b * t) * np.sin(t)
    z_path = L_OLD * t # Pitch is locked to L_OLD
    
    ax.plot(x_path, y_path, z_path, color='#DAA520', alpha=0.5, label='Sultanian Resonance Path')
    
    # 3. Plot Zeta Nodes (The Cyan Dots)
    for g in zeta_zeros:
        E = np.sqrt(0.25 + g**2) # Energy of the zero
        
        # KEY: Solve for t (the phase) where the spiral reaches energy E
        t_sync = (np.log(E) - np.log(a)) / b
        
        # Calculate coordinates using the SYNCED phase
        x_node = E * np.cos(t_sync)
        y_node = E * np.sin(t_sync)
        z_node = L_OLD * t_sync
        
        ax.scatter(x_node, y_node, z_node, color='#00FFFF', s=100, edgecolors='black', zorder=5)

    ax.set_title("Soltanian Helix: Synchronized Phase Alignment", fontsize=14)
    plt.show()
# --- Execution ---
if __name__ == "__main__":
    print(f"--- ShoSho Algorithm v2.1 ---")
    print(f"System Baseline L_old: {L_OLD:.8f}\n")
    execute_shosho_v2(zeta_zeros, primes)
    plot_soltanian_helix()
    plot_soltanian_helix_aligned()
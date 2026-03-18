import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi) 
PHASE_SHIFT = np.pi / 4        
R_ZETA = np.exp(L_OLD)        # Zeta Shell Radius
R_PRIME_BASE = R_ZETA * 0.7   # Internal Prime Core

# --- 2. Data Preparation ---
n_points = 50
zeta_zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271] 
# Note: For the full paper, use the 100-zero list provided earlier.
primes = list(sympy.primerange(2, sympy.prime(len(zeta_zeros)) + 1))

def plot_sultanian_cross_section(zeros, primes):
    fig = plt.figure(figsize=(18, 8), facecolor='black')
    
    # --- 3D VIEW: INTERTWINED MANIFOLD ---
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_facecolor('black')
    
    theta_z = np.array(zeros) * PHASE_SHIFT
    z_vals = L_OLD * (theta_z / np.pi)
    
    # Plot Zeta Gates (External)
    ax1.scatter(R_ZETA * np.cos(theta_z), R_ZETA * np.sin(theta_z), z_vals, 
                color='#00FFFF', s=80, marker='D', label='Zeta Gates')
    
    # Plot Prime Propulsion (Internal)
    # We use a slight logarithmic expansion for the prime radius to show energy growth
    r_p_dynamic = R_PRIME_BASE + (np.log(primes) / 10) 
    ax1.scatter(r_p_dynamic * np.cos(theta_z), r_p_dynamic * np.sin(theta_z), z_vals, 
                color='#FF4500', s=40, marker='x', label='Prime Core')

    # Resonance Bridges
    for i in range(len(zeros)):
        ax1.plot([r_p_dynamic[i] * np.cos(theta_z[i]), R_ZETA * np.cos(theta_z[i])],
                 [r_p_dynamic[i] * np.sin(theta_z[i]), R_ZETA * np.sin(theta_z[i])],
                 [z_vals[i], z_vals[i]], color='white', alpha=0.3)

    ax1.set_title("3D Sultanian Manifold", color='white')
    ax1.set_box_aspect((1,1,2))
    ax1.axis('off')

    # --- 2D VIEW: CROSS-SECTION (Top-Down) ---
    ax2 = fig.add_subplot(122, projection='polar')
    ax2.set_facecolor('#0b0f19')
    
    # Plot the Rings
    ax2.scatter(theta_z, np.full_like(theta_z, R_ZETA), color='#00FFFF', s=100, label='Zeta Shell')
    ax2.scatter(theta_z, r_p_dynamic, color='#FF4500', s=60, marker='x', label='Prime Core')
    
    # Fill the "Interference Zone"
    ax2.fill_between(np.linspace(0, 2*np.pi, 100), R_PRIME_BASE, R_ZETA, color='gold', alpha=0.1, label='Resonance Zone')

    ax2.set_title("Sultanian Cross-Section (Top-Down)", color='white', pad=20)
    ax2.tick_params(colors='white')
    ax2.grid(True, color='gray', alpha=0.3)
    
    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0), frameon=False, labelcolor='white')
    plt.tight_layout()
    plt.show()

plot_sultanian_cross_section(zeta_zeros, primes)
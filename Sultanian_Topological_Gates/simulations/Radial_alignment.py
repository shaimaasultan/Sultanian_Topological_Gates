import numpy as np
import matplotlib.pyplot as plt
import sympy

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)
TARGET_ZETA_ANGLE = np.deg2rad(45)   # Zeros (Cyan)
TARGET_PRIME_ANGLE = np.deg2rad(225) # Primes (Red)

# --- 2. Input Data (First 10 Zeros & First 10 Primes) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]
primes = list(sympy.primerange(2, sympy.prime(len(gammas)) + 1))

def plot_dual_radial_alignment(zeros, primes):
    fig = plt.figure(figsize=(10, 10), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#0b0f19')

    # 1. ZETA ZEROS (THE GATES)
    # Calculate Radii (The Energy Scale, log-scaled for visualization)
    radii_zeta = np.log1p([np.sqrt(0.25 + g**2) for g in zeros]) # Use log1p to avoid log(0)
    
    # Plot Zeta Zeros on the 45° Ray
    ax.scatter([TARGET_ZETA_ANGLE]*len(radii_zeta), radii_zeta, 
               color='#00F5FF', s=120, edgecolors='white', 
               label='Zeta Gates (Aligned)', zorder=5)

    # Draw the 45° Resonance Ray
    ax.plot([TARGET_ZETA_ANGLE, TARGET_ZETA_ANGLE], [0, max(radii_zeta)*1.1], 
            color='#00F5FF', linewidth=1.5, alpha=0.3)

    # 2. PRIME NUMBERS (THE PROPULSION)
    # Calculate Radii (Log-scaling the primes directly for energy scale)
    radii_prime = np.log1p(primes)
    
    # Plot Primes on the 225° Ray (Opposite side)
    ax.scatter([TARGET_PRIME_ANGLE]*len(radii_prime), radii_prime, 
               color='#FF4500', s=100, marker='x', edgecolors='white', 
               label='Prime Propulsion (Aligned)', zorder=5)

    # Draw the 225° Resonance Ray
    ax.plot([TARGET_PRIME_ANGLE, TARGET_PRIME_ANGLE], [0, max(radii_prime)*1.1], 
            color='#FF4500', linewidth=1.5, alpha=0.3)

    # Formatting
    ax.set_title("Sultanian Duality: Aligned Zeta & Prime Manifolds", color='white', fontsize=16, pad=30)
    
    # Grid and tick customization (matching the 45/225 duality)
    ax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315])
    ax.grid(True, color='gray', alpha=0.3, linestyle='--')
    ax.tick_params(colors='white', labelsize=10)
    
    # Set the radial limits for the log scale
    ax.set_rlabel_position(0)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['e^1', 'e^2', 'e^3', 'e^4', 'e^5'], color='white', alpha=0.6)

    plt.legend(loc='lower left', bbox_to_anchor=(0.8, 0.8), frameon=False, labelcolor='white')
    plt.show()

if __name__ == "__main__":
    plot_dual_radial_alignment(gammas, primes)
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sultanian System Constants (Ground State) ---
L_old = np.pi - np.log(np.pi)  # L_old ~1.996863
E_ground = np.exp(L_old)       # Ground State Energy Shell

# --- 2. Data Sets (Prime Numbers & Zeta Zeros) ---
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

# --- 3. Geometric Parameters ---
theta_max = 4 * np.pi          # Two full rotations
a = E_ground                   # Starting Radius is Ground State
b = 0.1                       # Tightened Growth Factor (The update)

# --- 4. Plot Initialization ---
fig = plt.figure(figsize=(12, 12), facecolor='#0b0f19') # Sultanian Void Color
ax = fig.add_subplot(111, projection='polar')
ax.set_facecolor('#0b0f19')

# 5. Generate the Soltanian Resonance Path (The Golden Helix)
# We plot on a logarithmic radial axis to manage energy states.
theta_range = np.linspace(0, theta_max, 1000)
r_spiral = a * np.exp(b * theta_range)
ax.plot(theta_range, r_spiral, color='gold', linewidth=1.5, alpha=0.3, label='Sultanian Resonance Path')

# --- 6. The ShoSho Alignment: Mapping Nodes onto the Helix ---
for i in range(10):
    # Mapping Zeta Zeros (Cyan Nodes)
    # E_zeta is the radial distance derived from the zero's height.
    E_zeta = np.sqrt(0.25 + gammas[i]**2)
    # Angle is determined by solving r=a*exp(b*theta) for theta, using E_zeta.
    angle_zeta = (np.log(E_zeta) - np.log(a)) / b
    ax.scatter(angle_zeta, E_zeta, color='#00F5FF', s=80, alpha=0.8, edgecolors='white', label='Zeta Node' if i == 0 else "")
    
    # Mapping Prime Numbers (Orange 'X' Harmonics)
    # We use the Prime Harmonnic Identity e^p_n, projected into the same complex plane.
    E_prime = np.exp(primes[i])
    angle_prime = (np.log(E_prime) - np.log(a)) / b
    ax.scatter(angle_prime, E_prime, color='#FF4500', marker='x', s=100, label='Prime Harmonic' if i == 0 else "")

# --- 7. Formatting & Final Display ---
ax.set_rscale('log') # Essential logarithmic scale for visualization
ax.set_title(f"Sultanian Duality: Prime Harmonics vs. Zeta Shells\nGrowth Factor b = {b} (Tightened Helix)", color='white', fontsize=16, pad=20)
ax.grid(True, color='gray', alpha=0.3)
ax.tick_params(colors='white') # Corrected for compatibility
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), frameon=False, labelcolor='white')

plt.show()
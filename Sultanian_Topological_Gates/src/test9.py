import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sultanian System Constants ---
L_old = np.pi - np.log(np.pi)
E_ground = np.exp(L_old)

# --- 2. Data Sets ---
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

# --- 3. Geometric Parameters ---
theta_max = 3 * np.pi          # Slightly reduced rotation for clarity at b=0.5
a = E_ground                   # Ground state anchor
b = 0.5                        # ACCELERATED growth factor

# --- 4. Plotting Configuration ---
fig = plt.figure(figsize=(12, 12), facecolor='#0b0f19') 
ax = fig.add_subplot(111, projection='polar')
ax.set_facecolor('#0b0f19')

# 5. Generate Resonance Path
theta_range = np.linspace(0, theta_max, 1000)
r_spiral = a * np.exp(b * theta_range)
ax.plot(theta_range, r_spiral, color='gold', linewidth=1.5, alpha=0.3, label='Sultanian Resonance Path')

# 6. Mapping Nodes (ShoSho Alignment)
for i in range(len(gammas)):
    # Zeta Zeros Mapping
    E_zeta = np.sqrt(0.25 + gammas[i]**2)
    angle_zeta = (np.log(E_zeta) - np.log(a)) / b
    ax.scatter(angle_zeta, E_zeta, color='#00F5FF', s=100, alpha=0.9, edgecolors='white')
    
    # Prime Harmonic Mapping
    E_prime = np.exp(primes[i])
    angle_prime = (np.log(E_prime) - np.log(a)) / b
    ax.scatter(angle_prime, E_prime, color='#FF4500', marker='x', s=120)

# 7. Final Touches
ax.set_rscale('log')
ax.set_title(f"Soltanian Helix: b = {b} (Accelerated Phase)", color='white', fontsize=18, pad=30)
ax.grid(True, color='gray', alpha=0.2)
ax.tick_params(colors='white')
plt.show()
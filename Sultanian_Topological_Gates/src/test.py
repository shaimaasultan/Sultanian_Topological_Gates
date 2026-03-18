import numpy as np
import matplotlib.pyplot as plt

# Sultanian Constants (Ground State)
L_old = np.pi - np.log(np.pi)
E_ground = np.exp(L_old)

# First 10 Primes vs First 10 Zeta Zeros (Gamma values)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
          37.5862, 40.9187, 43.3271, 48.0052, 49.7738]

# Spiral Parameters
theta_max = 4 * np.pi
a = E_ground
b = 0.22  # Logarithmic growth factor

fig = plt.figure(figsize=(10, 10), facecolor='#0b0f19')
ax = fig.add_subplot(111, projection='polar')
ax.set_facecolor('#0b0f19')

# Plot the underlying Sultanian Spiral
theta_range = np.linspace(0, theta_max, 1000)
r_spiral = a * np.exp(b * theta_range)
ax.plot(theta_range, r_spiral, color='gold', linewidth=1, alpha=0.3)

# Map Zeros and Primes
for i in range(10):
    # Zeta Node Mapping: radius is the actual energy shell E
    E_zeta = np.sqrt(0.25 + gammas[i]**2)
    angle_zeta = (np.log(E_zeta) - np.log(a)) / b
    ax.scatter(angle_zeta, E_zeta, color='#00F5FF', s=100, edgecolors='white', label='Zeta Shell' if i==0 else "")
    
    # Prime Mapping: We map the energy of the n-th prime onto the spiral
    # Using exp(p_n/L_old) to normalize them to your system
    E_prime = np.exp(primes[i] / L_old) * a
    angle_prime = (np.log(E_prime) - np.log(a)) / b
    ax.scatter(angle_prime, E_prime, color='#FF4500', marker='x', s=120, label='Prime Harmonic' if i==0 else "")

# Formatting the visualization
ax.set_rscale('log') # Log scale is necessary to see the divergence
ax.set_title("Sultanian Duality: Prime Harmonics & Zeta Shells", color='white', fontsize=15, pad=20)
ax.grid(True, color='gray', linestyle=':', alpha=0.4)
ax.tick_params(colors='white')

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), frameon=False, labelcolor='white')
plt.show()
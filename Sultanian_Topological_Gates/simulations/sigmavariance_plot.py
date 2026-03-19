import numpy as np
import matplotlib.pyplot as plt

# 1. Sultanian Constants
L_old = np.pi - np.log(np.pi)
R_ground = np.exp(L_old)

# 2. Known/Simulated Zeros (First 100)
known_gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
                37.5862, 40.9187, 43.3271, 48.0052, 49.7738]
np.random.seed(42)
gammas = list(known_gammas)
last_gamma = gammas[-1]
for _ in range(90):
    last_gamma += np.random.uniform(2.5, 3.5)
    gammas.append(last_gamma)
gammas = np.array(gammas)

# 3. Calculate Sigma (Expansion Rate)
# R = Energy = sqrt(1/4 + gamma^2)
# z = height = L_old * (gamma / 4)  -- assuming 45 deg per unit level
R_n = np.sqrt(0.25 + gammas**2)
z_n = L_old * (gammas / 4)
sigmas = (R_n - R_ground) / z_n

# 4. Moving Average for Stability
window_size = 10
sigmas_avg = np.convolve(sigmas, np.ones(window_size)/window_size, mode='valid')

# 5. Plotting the Stability Plot
plt.figure(figsize=(12, 7), facecolor='#0b0f19')
ax = plt.gca()
ax.set_facecolor('#0b0f19')

plt.plot(range(1, 101), sigmas, color='#00F5FF', alpha=0.4, label='$\sigma$ per Zero')
plt.plot(range(window_size, 101), sigmas_avg, color='#FF4500', linewidth=2.5, label='Moving Average Stability')

plt.axhline(np.mean(sigmas), color='white', linestyle='--', alpha=0.6, label=f'System Mean: {np.mean(sigmas):.3f}')

plt.title("Sultanian Expansion Stability: $\sigma$ Variance across 100 Zeros", color='white', fontsize=16, pad=20)
plt.xlabel("Zero Index ($n$)", color='white')
plt.ylabel("Expansion Factor ($\sigma$)", color='white')
plt.grid(True, color='gray', alpha=0.2)
plt.tick_params(colors='white')
plt.legend(frameon=False, labelcolor='white')

plt.savefig('sigma_stability_plot.png')
plt.show()

print(f"Mean Sigma: {np.mean(sigmas):.4f}")
print(f"Sigma Variance: {np.var(sigmas):.6f}")
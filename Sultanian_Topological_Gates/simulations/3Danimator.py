import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import sympy

# --- 1. Sultanian Constants ---
L_OLD = np.pi - np.log(np.pi) 
R_SHELL = np.exp(L_OLD)

# --- 2. Data Preparation (First 20 for a clean visual) ---
known_gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
                37.5862, 40.9187, 43.3271, 48.0052, 49.7738]
# Simulate next 10 for density
np.random.seed(42)
gammas = list(known_gammas)
for i in range(10):
    gammas.append(gammas[-1] + np.random.uniform(2.5, 3.5))

primes = list(sympy.primerange(2, sympy.prime(len(gammas)) + 1))

# Phase mappings
theta_zeta = np.array(gammas) * (np.pi / 4)
z_zeta = L_OLD * (theta_zeta / np.pi)

# Prime scaling (Logarithmic representation for the inner core)
r_prime = np.log1p(primes) * 0.5 

# --- 3. Setup the 3D Figure ---
fig = plt.figure(figsize=(10, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
ax.axis('off') # Hide the grid for a clean, cinematic look

# Draw Continuous Golden Helix
gamma_cont = np.linspace(min(gammas), max(gammas), 2000)
theta_cont = gamma_cont * (np.pi / 4)
z_cont = L_OLD * (theta_cont / np.pi)
ax.plot(R_SHELL * np.cos(theta_cont), R_SHELL * np.sin(theta_cont), z_cont, 
        color='gold', linewidth=2, alpha=0.6, label='Zeta Manifold')

# Draw Zeta Zeros (Cyan)
ax.scatter(R_SHELL * np.cos(theta_zeta), R_SHELL * np.sin(theta_zeta), z_zeta, 
           color='#00FFFF', s=80, edgecolors='white', alpha=0.9)

# Draw Prime Harmonics (Red Inner Core)
ax.scatter(r_prime * np.cos(theta_zeta), r_prime * np.sin(theta_zeta), z_zeta, 
           color='#FF4500', s=60, marker='o', edgecolors='white', alpha=0.9)

# Draw Resonance Bridges (White Lines connecting Primes to Zeros)
for i in range(len(gammas)):
    ax.plot([r_prime[i] * np.cos(theta_zeta[i]), R_SHELL * np.cos(theta_zeta[i])],
            [r_prime[i] * np.sin(theta_zeta[i]), R_SHELL * np.sin(theta_zeta[i])],
            [z_zeta[i], z_zeta[i]], color='white', linestyle='-', alpha=0.3)

ax.set_title("Sultanian Protocol: Prime Propulsion & Zeta Gates", color='white', fontsize=16, pad=20)

# --- 4. Animation Function ---
def rotate(angle):
    # Update the camera angle (Azimuth)
    ax.view_init(elev=20, azim=angle)
    return fig,

# Create the animation (360 frames for a full smooth rotation)
print("Rendering animation... this may take a minute.")
ani = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 360, 2), interval=50)

# --- 5. Save the Output ---
# Save as GIF (Easiest, works directly in GitHub without extra software)
output_filename = 'sultanian_rotation.gif'
ani.save(output_filename, writer='pillow', fps=20)
print(f"Success! Saved as {output_filename}")

# Note: If you have FFmpeg installed on your machine and want an MP4, 
# you can uncomment the line below:
# ani.save('sultanian_rotation.mp4', writer='ffmpeg', fps=30, dpi=200)
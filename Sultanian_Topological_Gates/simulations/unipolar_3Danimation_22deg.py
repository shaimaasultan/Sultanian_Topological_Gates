import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Sultanian Constants ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)
OCTA_PHASE = 22.5  # 2023 Identity Unit

# --- Dataset ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 
          48.0052, 49.7738, 52.8935, 56.4462]

def generate_ghost_ray_manifold():
    fig = plt.figure(figsize=(12, 12), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0b0f19')

    # 1. Generate the Expansion Shells (Surface)
    z_max = L_OLD * (max(gammas) / 4)
    z_surf = np.linspace(0, z_max + 5, 20)
    theta_surf = np.linspace(0, 2*np.pi, 60)
    Z_mesh, THETA_mesh = np.meshgrid(z_surf, theta_surf)
    R_mesh = R_GROUND + SIGMA * Z_mesh
    
    X_mesh = R_mesh * np.cos(THETA_mesh)
    Y_mesh = R_mesh * np.sin(THETA_mesh)
    ax.plot_wireframe(X_mesh, Y_mesh, Z_mesh, color='white', alpha=0.03, linewidth=0.5)

    # 2. Plot the 8-Sector Ghost Rays (The Lattice)
    for i in range(16): # 16 half-sectors of 22.5
        angle = np.radians(i * OCTA_PHASE)
        r_ray = R_GROUND + SIGMA * z_surf
        
        # Distinguish between the Active Ray and Ghost Rays
        if np.isclose(i * OCTA_PHASE, 45.0):
            ax.plot(r_ray * np.cos(angle), r_ray * np.sin(angle), z_surf, 
                    color='gold', alpha=0.9, linewidth=3, label='Active 45° Resonance')
        else:
            ax.plot(r_ray * np.cos(angle), r_ray * np.sin(angle), z_surf, 
                    color='white', alpha=0.1, linewidth=1, linestyle='--')

    # 3. Plot the Zeros (Occupied States)
    theta_fixed = np.radians(45)
    zeros_x, zeros_y, zeros_z = [], [], []
    for g in gammas:
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        zeros_x.append(r_n * np.cos(theta_fixed))
        zeros_y.append(r_n * np.sin(theta_fixed))
        zeros_z.append(z_n)
    
    ax.scatter(zeros_x, zeros_y, zeros_z, color='#00FFFF', s=100, 
               edgecolors='white', linewidth=1.2, depthshade=False, alpha=1)

    ax.set_axis_off()
    ax.view_init(elev=30, azim=30)
    
    plt.title("Sultanian Octa-Phase Lattice: Active vs. Ghost Sectors", color='white', pad=-30)
    plt.show()

if __name__ == "__main__":
    generate_ghost_ray_manifold()
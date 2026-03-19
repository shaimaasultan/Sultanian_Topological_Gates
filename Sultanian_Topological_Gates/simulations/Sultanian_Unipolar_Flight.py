import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# --- Sultanian Constants (Unified 2023-2026) ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)
OCTA_PHASE = 22.5  # The 2023 Lattice Unit

# --- Dataset (First 20 Zeros for the Flight Path) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 
          48.0052, 49.7738, 52.8935, 56.4462, 59.3470, 60.8317, 63.3200, 65.1100]

def generate_unipolar_flight():
    fig = plt.figure(figsize=(12, 10), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0b0f19')

    # 1. Generate the Conical Manifold (The Shells)
    z_max = L_OLD * (max(gammas) / 4)
    z_surf = np.linspace(0, z_max + 10, 40)
    theta_surf = np.linspace(0, 2*np.pi, 50)
    Z_mesh, THETA_mesh = np.meshgrid(z_surf, theta_surf)
    R_mesh = R_GROUND + SIGMA * Z_mesh
    
    X_mesh = R_mesh * np.cos(THETA_mesh)
    Y_mesh = R_mesh * np.sin(THETA_mesh)
    ax.plot_wireframe(X_mesh, Y_mesh, Z_mesh, color='white', alpha=0.04, linewidth=0.5)

    # 2. Plot the 8-Sector Ghost Rays (2023 Octa-Phase)
    for i in range(16):
        angle = np.radians(i * OCTA_PHASE)
        r_ray = R_GROUND + SIGMA * z_surf
        # Highlight the Active 45-degree ray
        if np.isclose(i * OCTA_PHASE, 45.0):
            ax.plot(r_ray * np.cos(angle), r_ray * np.sin(angle), z_surf, 
                    color='gold', alpha=0.9, linewidth=3, label='Active 45° Resonance')
        else:
            ax.plot(r_ray * np.cos(angle), r_ray * np.sin(angle), z_surf, 
                    color='white', alpha=0.1, linewidth=1, linestyle='--')

    # 3. Plot the Zeros (Locked on 45°)
    theta_fixed = np.radians(45)
    zeros_x, zeros_y, zeros_z = [], [], []
    for g in gammas:
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        zeros_x.append(r_n * np.cos(theta_fixed))
        zeros_y.append(r_n * np.sin(theta_fixed))
        zeros_z.append(z_n)
    
    scatter = ax.scatter(zeros_x, zeros_y, zeros_z, color='#00FFFF', s=120, 
                         edgecolors='white', linewidth=1.5, depthshade=False, alpha=1)

    # 4. Flight Animation Logic
    ax.set_axis_off()
    
    def update(frame):
        # Camera follows the ray expansion
        current_z = (frame / 150) * z_max
        current_r = R_GROUND + SIGMA * current_z
        
        # Adjust view for dynamic flight perspective
        ax.view_init(elev=20 + np.sin(frame/30)*10, azim=30 + (frame/2)) 
        
        # Center the view on the current height to simulate "flying up"
        ax.set_zlim(current_z - 10, current_z + 30)
        return scatter,

    ani = FuncAnimation(fig, update, frames=300, interval=50, blit=False)
    plt.title("Sultanian Unipolar Flight: Phase-Lock Verification", color='white', fontsize=16, pad=-20)
    
    print("Sultanian Flight Engine Active. Displaying Manifold...")
    plt.show()

if __name__ == "__main__":
    generate_unipolar_flight()
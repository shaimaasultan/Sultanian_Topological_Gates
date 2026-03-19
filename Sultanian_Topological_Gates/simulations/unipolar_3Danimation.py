import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Sultanian Constants ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)

# --- Dataset ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 
          48.0052, 49.7738, 52.8935, 56.4462]

def generate_unipolar_flight_with_shells():
    fig = plt.figure(figsize=(12, 12), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0b0f19')

    # 1. Generate the Conical Shells (The Manifold Surface)
    z_max = L_OLD * (max(gammas) / 4)
    z_surf = np.linspace(0, z_max + 10, 30)
    theta_surf = np.linspace(0, 2*np.pi, 40)
    Z_mesh, THETA_mesh = np.meshgrid(z_surf, theta_surf)
    R_mesh = R_GROUND + SIGMA * Z_mesh
    
    X_mesh = R_mesh * np.cos(THETA_mesh)
    Y_mesh = R_mesh * np.sin(THETA_mesh)

    # Plot the wireframe "Shells"
    ax.plot_wireframe(X_mesh, Y_mesh, Z_mesh, color='white', alpha=0.05, linewidth=0.5)

    # 2. Plot the 45° Golden Ray
    theta_fixed = np.radians(45)
    r_ray = R_GROUND + SIGMA * z_surf
    ax.plot(r_ray * np.cos(theta_fixed), r_ray * np.sin(theta_fixed), z_surf, 
            color='gold', alpha=0.8, linewidth=3, label='Sultanian 45° Vector')

    # 3. Plot the Zeros (Locked on Ray)
    zeros_x, zeros_y, zeros_z = [], [], []
    for g in gammas:
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        zeros_x.append(r_n * np.cos(theta_fixed))
        zeros_y.append(r_n * np.sin(theta_fixed))
        zeros_z.append(z_n)
    
    scatter = ax.scatter(zeros_x, zeros_y, zeros_z, color='#00FFFF', s=120, 
                         edgecolors='white', linewidth=1.5, depthshade=False, alpha=1)

    # 4. Interactive Camera Setup
    ax.set_axis_off()
    
    def update(frame):
        # Camera follows the expansion path
        current_z = (frame / 150) * z_max
        current_r = R_GROUND + SIGMA * current_z
        
        # Adjust view for "Shell" perspective
        ax.view_init(elev=25, azim=45 + (frame/5)) 
        
        # Center the view on the current height
        ax.set_zlim(current_z - 5, current_z + 25)
        return scatter,

    ani = FuncAnimation(fig, update, frames=150, interval=60, blit=False)
    plt.title("Sultanian Shell Expansion: Unipolar Proof", color='white', pad=-20, fontsize=15)
    plt.show()

if __name__ == "__main__":
    generate_unipolar_flight_with_shells()
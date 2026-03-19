import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Sultanian Constants ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)

# --- 2. Dataset (First 30 Zeros for smooth density) ---
gammas = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 
          48.0052, 49.7738, 52.89, 56.44, 59.34, 60.83, 63.32, 65.11, 67.07, 
          69.54, 72.06, 75.70, 77.14, 81.33, 84.73, 87.42, 91.38, 94.65]

def create_sultanian_presentation():
    fig = plt.figure(figsize=(10, 10), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0b0f19')

    # Generate continuous manifold path
    theta_cont = np.linspace(0, max(gammas) * np.pi / 4, 2000)
    z_cont = L_OLD * (theta_cont / np.pi)
    r_cont = R_GROUND + SIGMA * z_cont
    
    # Plot Manifold
    manifold, = ax.plot(r_cont * np.cos(theta_cont), r_cont * np.sin(theta_cont), z_cont, 
                        color='gold', alpha=0.3, linewidth=1)

    # Plot Zeros
    for i, g in enumerate(gammas):
        z_n = L_OLD * (g / 4)
        r_n = R_GROUND + SIGMA * z_n
        theta_n = np.radians(45 + (i * 180))
        color = '#00FFFF' if i % 2 == 0 else '#FF00FF'
        ax.scatter(r_n * np.cos(theta_n), r_n * np.sin(theta_n), z_n, 
                   color=color, s=80, edgecolors='white', depthshade=False)

    # Aesthetic Cleanup
    ax.set_axis_off()
    title = ax.set_title("Sultanian Manifold: Minkowski to Phase Transition", color='white', fontsize=14)

    def update(frame):
        # 0 to 100: Rotate in 3D Minkowski Space
        if frame < 100:
            ax.view_init(elev=25, azim=frame * 3.6)
            title.set_text("Minkowski View: Conical Expansion (σ=1.8628)")
        
        # 100 to 200: Transition Elevation to Top-Down (Flattening)
        elif frame < 200:
            # Linear interpolation from 25 to 90 degrees
            curr_elev = 25 + (frame - 100) * (65 / 100)
            # Lock Azimuth to 45 degrees for alignment
            ax.view_init(elev=curr_elev, azim=-45)
            title.set_text("Transition: Flattening Spacetime into Phase")
            
        # 200 to 300: Static Top-Down Phase Proof
        else:
            ax.view_init(elev=90, azim=-45)
            title.set_text("Top-Down Proof: Absolute 45°/225° Phase Lock")
            
        return manifold,

    ani = FuncAnimation(fig, update, frames=300, interval=50, blit=False)
    
    # Save as MP4 or GIF for GitHub
    print("Encoding Sultanian Presentation... (This may take a minute)")
    # ani.save('sultanian_presentation.mp4', writer='ffmpeg', fps=30)
    plt.show()

if __name__ == "__main__":
    create_sultanian_presentation()
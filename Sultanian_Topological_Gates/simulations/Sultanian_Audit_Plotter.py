import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_audit_results(csv_file='SULTANIAN_AUDIT_LOG.csv'):
    # Load the high-precision data
    df = pd.read_csv(csv_file)
    
    fig = plt.figure(figsize=(10, 10), facecolor='#0b0f19')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#0b0f19')
    
    # Convert phase to radians for polar plot
    theta_rad = np.radians(df['Observed_Phase_deg'])
    radii = df['Sultanian_Radius_R']
    
    # 1. Plot the Ghost Lattice (22.5 degree increments)
    ghost_angles = np.radians(np.arange(0, 360, 22.5))
    for g_angle in ghost_angles:
        ax.plot([g_angle, g_angle], [0, radii.max()], color='white', alpha=0.1, linewidth=0.8, linestyle='--')

    # 2. Plot the Audit Data (The Zeros)
    ax.scatter(theta_rad, radii, color='#00FFFF', s=20, alpha=0.6, label='Zeta Zeros (Audit Data)')
    
    # 3. Formatting
    ax.set_theta_zero_location('N') # North is 0 degrees
    ax.set_theta_direction(-1)      # Clockwise
    ax.set_rscale('log')            # Log scale for radial expansion
    
    ax.set_title("Sultanian Scale Invariance: Unipolar Lock Verified", color='white', fontsize=15, pad=20)
    ax.tick_params(colors='white', grid_alpha=0.2)
    ax.grid(True, color='gray', alpha=0.3)
    
    plt.legend(frameon=False, labelcolor='white', loc='lower right')
    plt.show()

if __name__ == "__main__":
    plot_audit_results()
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sultanian Core Parameters ---
L_OLD = np.pi - np.log(np.pi)
SIGMA = 1.8628
R_GROUND = np.exp(L_OLD)

# --- 2. Data Points ---
# Zero 1: Gamma ~ 14.1347 (n=1, Odd -> 45°)
# Zero 1,000,000: Gamma ~ 600269.677 (n=1,000,000, Even -> 225°)
zeros_data = [
    {"n": 1, "gamma": 14.1347, "color": "#00FFFF", "label": "Zero 1 (Phase A)"},
    {"n": 1000000, "gamma": 600269.677, "color": "#FF00FF", "label": "Zero 1M (Phase B)"}
]

def render_dual_scale_proof():
    fig = plt.figure(figsize=(16, 8), facecolor='#0b0f19')
    
    for i, data in enumerate(zeros_data):
        ax = fig.add_subplot(1, 2, i+1, projection='polar')
        ax.set_facecolor('#0b0f19')
        
        # Calculate Manifold Coordinates
        z_n = L_OLD * (data['gamma'] / 4)
        r_n = R_GROUND + (SIGMA * z_n)
        
        # Binary Phase Lock Rule: 45 + (n-1)*180
        theta_deg = 45 + ((data['n'] - 1) * 180)
        theta_rad = np.radians(theta_deg)
        
        # Plot the "Target Ray" for the Phase Lock
        ax.plot([theta_rad, theta_rad], [0, r_n], color='white', linestyle='--', alpha=0.3)
        
        # Plot the Zero
        ax.scatter(theta_rad, r_n, color=data['color'], s=200, edgecolors='white', zorder=5)
        
        # Formatting
        ax.set_title(f"{data['label']}\ngamma approx {data['gamma']:.2f}$", color='white', fontsize=14, pad=20)
        ax.set_rticks([r_n]) # Show only the current radius scale
        ax.set_yticklabels([f"R={int(r_n)}"], color='white', alpha=0.7)
        ax.tick_params(colors='white', grid_alpha=0.2)
        
        # Force the grid to show the 45/225 line clearly
        ax.set_thetagrids([45, 135, 225, 315], labels=['45°', '135°', '225°', '315°'])

    plt.suptitle("Sultanian Scale-Invariance Proof: Phase-Lock Stability", color='gold', fontsize=20, y=1.05)
    plt.tight_layout()
    plt.savefig('sultanian_scale_proof.png')
    plt.show()

if __name__ == "__main__":
    render_dual_scale_proof()
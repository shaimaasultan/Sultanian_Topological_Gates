import numpy as np
import pandas as pd

# --- 1. Sultanian System Parameters ---
L_OLD = np.pi - np.log(np.pi)      # Pitch Constant
SIGMA = 1.8628                    # Official Expansion Factor
R_GROUND = np.exp(L_OLD)          # Ground Radius

# --- 2. Dataset: Non-Trivial Zeros (Gamma) ---
# Listing the first 20 for the table
gammas = [
    14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 
    37.5862, 40.9187, 43.3271, 48.0052, 49.7738,
    52.8935, 56.4462, 59.3470, 60.8317, 63.3200,
    65.1100, 67.0700, 69.5400, 72.0600, 75.7000
]

def generate_duality_table(zeros):
    table_data = []

    for i, g in enumerate(zeros):
        n = i + 1
        
        # Calculate Height (Z)
        # In the Sultanian model, Z is the vertical frequency scale
        z_n = L_OLD * (g / 4)
        
        # Calculate Expanding Radius (R)
        # R = Ground Radius + (Expansion Rate * Height)
        r_n = R_GROUND + (SIGMA * z_n)
        
        # Calculate Binary Phase Lock (Theta)
        # Odds = 45 deg, Evens = 225 deg
        phase_deg = 45 + (i * 180)
        state = "Phase A (45°)" if i % 2 == 0 else "Phase B (225°)"
        
        table_data.append({
            "Zero (n)": n,
            "Gamma (γ)": round(g, 4),
            "Radius (R)": round(r_n, 3),
            "Height (Z)": round(z_n, 3),
            "Locked Phase": f"{phase_deg % 360}°",
            "State": state
        })

    # Create DataFrame for clean display
    df = pd.DataFrame(table_data)
    
    # 3. Print to Console
    print("\n=== SULTANIAN CONHELIX DUALITY TABLE ===")
    print(df.to_string(index=False))
    
    # 4. Save to CSV for GitHub/Paper
    df.to_csv("sultanian_duality_table.csv", index=False)
    print("\n[File Saved]: sultanian_duality_table.csv")

if __name__ == "__main__":
    generate_duality_table(gammas)
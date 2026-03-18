import numpy as np
import pandas as pd
from mpmath import zetazero

# 1. Sultanian Constants
L_OLD = np.pi - np.log(np.pi)  # ~1.9968
PHASE_SHIFT = np.pi / 4        # 45 Degrees

def generate_sultanian_data(n_zeros=2):
    print(f"Generating Sultanian coordinates for {n_zeros} zeros...")
    
    # Fetch first n non-trivial zeros (imaginary parts/gamma)
    # Note: mpmath provides the imaginary part 'gamma' assuming Re(s)=1/2
    zeros = [float(zetazero(i).imag) for i in range(1, n_zeros + 1)]
    
    data = []
    for i, gamma in enumerate(zeros):
        # The 45-Degree Phase-Shift transformation
        theta = gamma * PHASE_SHIFT
        print(i+1, gamma, theta)  # Debug: Print the gamma and corresponding theta
        
        # Radial Shell (The 'Even' Pressure)
        # Derived from the exponential of the Sultanian Constant
        r = np.exp(L_OLD)
        
        # Vertical Propulsion (The 'Odd' Tail / Z-climb)
        # This is where the 2023 Identity maps to the 3D manifold
        z = L_OLD * (theta / np.pi) 
        
        data.append({
            'Index': i + 1,
            'Gamma': gamma,
            'Radial_R': r,
            'Theta_Rad': theta,
            'Vertical_Z': z
        })
        
    return pd.DataFrame(data)

# Execute and Save
df_manifold = generate_sultanian_data(1000)
df_manifold.to_csv('sultanian_manifold_10k.csv', index=False)

print("Success! File 'sultanian_manifold_10k.csv' created.")
print(df_manifold.head())
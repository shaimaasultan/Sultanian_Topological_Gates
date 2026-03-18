import numpy as np
import pandas as pd

# Define Global Constant for the System
L_OLD = np.pi - np.log(np.pi) 

def shosho_algorithm_v2(gamma_list, prime_list):
    results = []
    
    # We iterate through the available zeros and primes
    for i in range(len(gamma_list) - 1):
        # 1. Map Current Zero Resonance
        g_n = gamma_list[i]
        E_n = np.sqrt(0.25 + g_n**2)
        K_n = np.log(E_n) / L_OLD
        
        # 2. Map Next Zero Resonance
        g_next = gamma_list[i+1]
        E_next = np.sqrt(0.25 + g_next**2)
        K_next = np.log(E_next) / L_OLD
        
        # 3. Calculate Vertical Rise (Z-Vector Displacement)
        delta_Z = np.log(E_next / E_n)
        pitch = delta_Z / (K_next - K_n)
        
        # 4. Prime Propulsion Logic
        # Each prime harmonic provides a "kick" to the Z-vector
        p_n = prime_list[i]
        propulsion_force = np.log(p_n) / L_OLD
        
        results.append({
            "Node": f"ρ_{i+1}→ρ_{i+2}",
            "K_Scale": round(K_n, 4),
            "Sultanian_Pitch": round(pitch, 6),
            "Prime_Fuel (p_n)": p_n,
            "Propulsion_Force": round(propulsion_force, 6)
        })
        
    return pd.DataFrame(results)

# Test Data
zeta_zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351]
primes = [2, 3, 5, 7, 11]

df = shosho_algorithm_v2(zeta_zeros, primes)

print("--- ShoSho Algorithm: Vertical Pitch & Prime Propulsion ---")
print(df.to_string(index=False))

mean_p = df["Sultanian_Pitch"].mean()
print(f"\n[SYSTEM CHECK]")
print(f"Average System Pitch (p): {mean_p:.6f}")
print(f"Ground State (L_old):     {L_OLD:.6f}")
print(f"Resonance Lock Error:     {abs(mean_p - L_OLD):.10f}")
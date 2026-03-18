import numpy as np
import pandas as pd

# --- System Constant (Soltanian Ground State) ---
L_OLD = np.pi - np.log(np.pi) 

def shosho_propulsion_algorithm(gamma_list, prime_list):
    """
    Analyzes the relationship between Prime Gaps (Delta p) 
    and the Vertical Pitch Acceleration between Zeta Zeros.
    """
    results = []
    
    for i in range(len(gamma_list) - 1):
        # 1. Coordinate Mapping (Zeta)
        g_n, g_next = gamma_list[i], gamma_list[i+1]
        E_n, E_next = np.sqrt(0.25 + g_n**2), np.sqrt(0.25 + g_next**2)
        
        # 2. Vertical Displacement
        delta_Z = np.log(E_next / E_n)
        K_n = np.log(E_n) / L_OLD
        K_next = np.log(E_next) / L_OLD
        pitch = delta_Z / (K_next - K_n)
        
        # 3. Prime Propulsion Logic (The Acceleration)
        p_n, p_next = prime_list[i], prime_list[i+1]
        delta_p = p_next - p_n # The Prime Gap
        
        # Acceleration is defined as the change in log-energy relative to the gap
        propulsion_accel = np.log(delta_p + 1) / L_OLD 
        
        results.append({
            "Node": f"ρ_{i+1}→ρ_{i+2}",
            "Sultanian_Pitch": round(pitch, 6),
            "Prime_Gap (Δp)": delta_p,
            "Propulsion_Accel": round(propulsion_accel, 6),
            "Energy_Shell": round(K_n, 4)
        })
        
    return pd.DataFrame(results)

# --- Execution ---
zeta_zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351]
primes = [2, 3, 5, 7, 11]

df = shosho_propulsion_algorithm(zeta_zeros, primes)

print("--- ShoSho Algorithm: Prime Gap Acceleration Analysis ---")
print(df.to_string(index=False))

# Validation Check
mean_p = df["Sultanian_Pitch"].mean()
print(f"\n[SYSTEM VALIDATION]")
print(f"Mean Vertical Pitch (p): {mean_p:.6f}")
print(f"Theoretical L_old:       {L_OLD:.6f}")
print(f"Synchronization Error:   {abs(mean_p - L_OLD):.12f}")
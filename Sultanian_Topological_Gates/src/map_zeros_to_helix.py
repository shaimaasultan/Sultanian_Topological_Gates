import numpy as np
import pandas as pd

# Load your 100 zeros (Assuming you've extracted them from the image/list)
# Here are the first few for the example:
zeta_zeros_100 = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 
                  37.586178, 40.918719, 43.327073, 48.005151, 49.773832] # ... continue to 100

L_OLD = np.pi - np.log(np.pi)
PHASE_SHIFT = np.pi / 4

def map_to_sultanian(gamma_list):
    manifold_nodes = []
    for gamma in gamma_list:
        theta = gamma * PHASE_SHIFT
        r = np.exp(L_OLD)
        z = L_OLD * (theta / np.pi)
        manifold_nodes.append((r, theta, z))
    return manifold_nodes

nodes_3d = map_to_sultanian(zeta_zeros_100)
print(f"Mapped {len(nodes_3d)} Sultanian Gates.")
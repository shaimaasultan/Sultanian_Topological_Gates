import pandas as pd
import plotly.graph_objects as go
import numpy as np

def visualize_dynamic_helix(csv_file='sultanian_manifold_10k.csv', tightness_factor=1.0):
    df = pd.read_csv(csv_file).head(10) # Using 100 zeros to see the spiral clearly
    
    # Sultanian Constants
    L_OLD_BASE = np.pi - np.log(np.pi)
    L_EFFECTIVE = L_OLD_BASE * tightness_factor # Adjusting the "Propulsion"
    
    # 1. Generate the Adjusted Helix Path
    theta_line = np.linspace(df['Theta_Rad'].min(), df['Theta_Rad'].max(), 2000)
    r_line = np.full_like(theta_line, np.exp(L_OLD_BASE)) # Radius stays constant for the shell
    z_line = L_EFFECTIVE * (theta_line / np.pi) # Adjusted Vertical Climb

    # 2. Adjust the Zero Coordinates (The Nodes)
    z_nodes = L_EFFECTIVE * (df['Theta_Rad'] / np.pi)

    fig = go.Figure()

    # Add the Path
    fig.add_trace(go.Scatter3d(
        x=r_line, y=theta_line, z=z_line,
        mode='lines',
        line=dict(color='gold', width=3),
        name=f'Helix (Tightness: {tightness_factor})'
    ))

    # Add the Nodes
    fig.add_trace(go.Scatter3d(
        x=df['Radial_R'], y=df['Theta_Rad'], z=z_nodes,
        mode='markers',
        marker=dict(size=4, color='cyan', opacity=0.8),
        name='Topological Gates'
    ))

    fig.update_layout(
        template="plotly_dark",
        title=f"Sultanian Manifold: Vertical Propulsion Adjusted (Factor: {tightness_factor})",
        scene=dict(
            aspectratio=dict(x=1, y=1, z=2),
            zaxis=dict(title='Vertical Propulsion (Z)')
        )
    )
    fig.show()

# Try changing this value: 0.5 (Tight), 1.0 (Standard), 2.0 (Stretched)
visualize_dynamic_helix(tightness_factor=0.1,csv_file='sultanian_topological_gates/data/sultanian_manifold_10k.csv')
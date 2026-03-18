import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

# --- 1. Sultanian System Constants ---
L_OLD = np.pi - np.log(np.pi)  # The Thread Pitch (~1.9968)
PHASE_SHIFT = np.pi / 4         # The 45-Degree Perspective
R_SHELL = np.exp(L_OLD)        # The Constant Radial Shell

def verify_sultanian_path(csv_filename='zeros_100.csv'):
    print(f"Loading data from {csv_filename}...")
    
    # --- 2. Read the File ---
    if not os.path.exists(csv_filename):
        print(f"Error: Could not find '{csv_filename}'.")
        print("Please ensure your file is in the same folder and named correctly.")
        return
        
    df = pd.read_csv(csv_filename)
    
    # Check if 'Gamma' column exists. If not, assume the first column holds the zeros.
    if 'Gamma' in df.columns:
        gammas = df['Gamma'].values
    else:
        gammas = df.iloc[:, 0].values
        print("Column 'Gamma' not found. Using the first column as zero values.")

    # --- 3. Calculate the Discrete Nodes (The Gates) ---
    theta_nodes = gammas * PHASE_SHIFT
    x_nodes = R_SHELL * np.cos(theta_nodes)
    y_nodes = R_SHELL * np.sin(theta_nodes)
    z_nodes = L_OLD * (theta_nodes / np.pi)

    # --- 4. Calculate the Continuous Helix (The Path) ---
    # We use a very high resolution (5000 points) to ensure the curve is perfectly smooth
    gamma_continuous = np.linspace(min(gammas), max(gammas), 5000)
    theta_path = gamma_continuous * PHASE_SHIFT
    x_path = R_SHELL * np.cos(theta_path)
    y_path = R_SHELL * np.sin(theta_path)
    z_path = L_OLD * (theta_path / np.pi)

    # --- 5. Build the Interactive 3D Plot ---
    fig = go.Figure()

    # Layer 1: The Continuous Helix Path (Gold Line)
    fig.add_trace(go.Scatter3d(
        x=x_path, y=y_path, z=z_path,
        mode='lines',
        line=dict(color='gold', width=4),
        name='Sultanian Helix Path',
        hoverinfo='none' # Turn off hover for the line so it doesn't block the nodes
    ))

    # Layer 2: The Zeta Zeros from your File (Cyan Diamonds)
    fig.add_trace(go.Scatter3d(
        x=x_nodes, y=y_nodes, z=z_nodes,
        mode='markers',
        marker=dict(
            size=8,
            color='cyan',
            symbol='diamond',
            line=dict(color='white', width=1),
            opacity=0.9
        ),
        name='Zeta Zeros (From File)',
        text=[f"Zero #{i+1}<br>Gamma: {g:.4f}<br>Z-Height: {z:.4f}" for i, (g, z) in enumerate(zip(gammas, z_nodes))],
        hoverinfo='text'
    ))

    # --- 6. Formatting for Verification ---
    fig.update_layout(
        template="plotly_dark",
        title="Verification: Sultanian Helix Intersecting 100 Zeta Zeros",
        scene=dict(
            xaxis_title='Radial X',
            yaxis_title='Radial Y',
            zaxis_title='Vertical Propulsion (Z)',
            aspectratio=dict(x=1, y=1, z=2.5) # Stretch Z to see the intersections clearly
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    # Save and show
    output_file = 'verification_plot.html'
    fig.write_html(output_file)
    print(f"Success! Opening '{output_file}' in your web browser...")
    
    import webbrowser
    webbrowser.open(output_file)

# --- EXECUTION ---
# Ensure you have a file named 'sultanian_manifold_10k.csv' with a header 'Gamma'
if __name__ == "__main__":
    verify_sultanian_path('sultanian_topological_gates/data/sultanian_manifold_10k.csv')
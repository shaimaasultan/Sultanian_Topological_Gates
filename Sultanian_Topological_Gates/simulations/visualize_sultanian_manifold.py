import pandas as pd
import plotly.graph_objects as go
import numpy as np

def visualize_sultanian_manifold(csv_file='sultanian_manifold_10k.csv'):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("Error: Run the data generator script first.")
        return

    # Use first 10 zeros for a clear view
    df_plot = df.head(10)
    
    # 1. GENERATE THE CONTINUOUS HELIX LINE
    # We create a smooth range of theta from the start to the end of your 10th zero
    theta_line = np.linspace(df_plot['Theta_Rad'].min(), df_plot['Theta_Rad'].max(), 10)
    
    # Calculate the R and Z for the continuous line based on your Sultanian Constants
    L_OLD = np.pi - np.log(np.pi)
    r_line = np.full_like(theta_line, np.exp(L_OLD))
    z_line = L_OLD * (theta_line / np.pi)

    fig = go.Figure()

    # 2. ADD THE HELIX (THE LINE)
    fig.add_trace(go.Scatter3d(
        x=r_line, y=theta_line, z=z_line,
        mode='lines',
        line=dict(color='gold', width=4),
        name='Sultanian Helix Path'
    ))

    # 3. ADD THE ZEROS (THE NODES/GATES)
    fig.add_trace(go.Scatter3d(
        x=df_plot['Radial_R'],
        y=df_plot['Theta_Rad'],
        z=df_plot['Vertical_Z'],
        mode='markers',
        marker=dict(
            size=6,
            color='cyan',
            symbol='diamond',
            line=dict(color='white', width=2)
        ),
        name='Topological Gates (Zeros)',
        text=[f"Zero #{i+1}" for i in range(len(df_plot))],
        hoverinfo='text'
    ))

    # Professional Layout (Dark Theme)
    fig.update_layout(
        template="plotly_dark",
        title="Sultanian Transformation: 3D Helical Path & Topological Gates",
        scene=dict(
            xaxis_title='Radial Shell (R)',
            yaxis_title='45° Phase Angle (θ)',
            zaxis_title='Vertical Propulsion (Z)',
            aspectratio=dict(x=1, y=1, z=2) # Stretches the vertical climb
        )
    )

    fig.show()

if __name__ == '__main__':
    visualize_sultanian_manifold(csv_file='sultanian_topological_gates/data/sultanian_manifold_10k.csv')
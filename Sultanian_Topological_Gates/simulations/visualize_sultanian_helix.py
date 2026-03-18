import pandas as pd
import plotly.graph_objects as go
import numpy as np

def visualize_sultanian_manifold(csv_file='sultanian_manifold_10k.csv'):
    print(f"Loading data from {csv_file}...")
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found. Please run the data generator script first.")
        return

    # Check for empty data
    if df.empty:
        print("Error: The CSV file is empty.")
        return

    # Limit to first 10,000 (or total available)
    df_plot = df.head(10)
    
    print(f"Plotting {len(df_plot)} points on the Sultanian Manifold...")

    # Define color scale based on the vertical climb (Z) to show progression
    marker_color = df_plot['Vertical_Z']
    
    # Create the 3D Scatter Plot
    fig = go.Figure(data=[go.Scatter3d(
        x=df_plot['Radial_R'],
        y=df_plot['Theta_Rad'],
        z=df_plot['Vertical_Z'],
        mode='markers',
        marker=dict(
            size=2,                  # Small markers for 10k points
            color=marker_color,       # Color linked to Z-axis/Propulsion
            colorscale='Viridis',    # Professional gradient (Blue -> Yellow)
            opacity=0.6,             # Slight transparency for depth
            showscale=True,          # Include the colorbar
            colorbar=dict(title='Vertical Propulsion (Z)')
        ),
        text=[f"Zero #{i+1}<br>Gamma: {g:.2f}" for i, g in zip(df_plot['Index'], df_plot['Gamma'])],
        hoverinfo='text'             # Show info on hover
    )])

    # 4. Professional Layout and Labeling
    fig.update_layout(
        title={
            'text': "The Sultanian Transformation System: 3D Helical Unfolding",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        scene=dict(
            xaxis=dict(title='Radial Shell (R)', nticks=6, range=[df_plot['Radial_R'].min()*0.9, df_plot['Radial_R'].max()*1.1]),
            yaxis=dict(title='45° Phase Angle (θ)', nticks=10),
            zaxis=dict(title='Vertical Propulsion (Z)', nticks=10),
            aspectmode='manual', # Control the shape of the plot
            aspectratio=dict(x=1, y=1, z=2) # Emphasize the vertical climb
        ),
        margin=dict(l=0, r=0, b=0, t=50), # Maximize plot area
        paper_bgcolor='black', # Dark theme for contrast
        font=dict(color='white') # White text for dark theme
    )

    # Save as an interactive HTML file
    output_html = 'sultanian_helix_interactive.html'
    fig.write_html(output_html)
    print(f"Success! Interactive visualization saved as '{output_html}'.")
    
    # Optionally open it immediately (works on most systems)
    import webbrowser
    webbrowser.open(output_html)

if __name__ == '__main__':
    # Make sure you've generated the data first!
    visualize_sultanian_manifold(csv_file='sultanian_topological_gates/data/sultanian_manifold_10k.csv')
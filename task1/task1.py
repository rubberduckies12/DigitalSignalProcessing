import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Create data
t = np.arange(-2*np.pi, 2*np.pi, 0.01)
f = 5 * np.cos(t)

# Create interactive plot with plotly
fig = go.Figure()

# Add scatter plot with hover information
fig.add_trace(go.Scatter(
    x=t,
    y=f,
    mode='markers',
    marker=dict(
        symbol='star',
        size=4,
        color='blue'
    ),
    name='5*cos(t)',
    hovertemplate='<b>t:</b> %{x:.3f}<br>' +
                  '<b>f(t):</b> %{y:.3f}<br>' +
                  '<b>Function:</b> 5*cos(t)<br>' +
                  '<extra></extra>' 
))

# Update layout
fig.update_layout(
    title='Task 1: 5*cos(t) - Interactive Plot',
    xaxis_title='t',
    yaxis_title='f(t)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zeroline=True,
        zerolinecolor='black',
        zerolinewidth=1
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zeroline=True,
        zerolinecolor='black',
        zerolinewidth=1
    ),
    hovermode='closest',
    width=800,
    height=600,
    template='plotly_white'
)

# Add some styling for better interactivity
fig.update_traces(
    marker=dict(
        line=dict(width=0.5, color='darkblue')
    )
)

# Show the plot
fig.show()

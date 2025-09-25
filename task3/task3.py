import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

x = np.linspace(-2*np.pi, 2*np.pi, 120)
y = np.linspace(-2*np.pi, 2*np.pi, 120)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'type': 'surface'}, {'type': 'surface'}],
           [{'type': 'xy'}, {'type': 'xy'}]],
    subplot_titles=[
        '<span style="color:#2E86C1; font-size:16px;">🌊 Interactive 3D Surface: z = sin(x² + y²)</span>',
        '<span style="color:#E74C3C; font-size:16px;">⚡ Wireframe with Contours</span>',
        '<span style="color:#17A2B8; font-size:16px;">🔥 Contour Heatmap</span>',
        '<span style="color:#28A745; font-size:16px;">📊 Cross-sections Analysis</span>'
    ],
    vertical_spacing=0.1,
    horizontal_spacing=0.08
)

colorscale = 'viridis'
wireframe_colorscale = 'plasma'

fig.add_trace(
    go.Surface(
        x=X, y=Y, z=Z,
        colorscale=colorscale,
        showscale=True,
        opacity=0.9,
        hovertemplate='<b style="color:#2E86C1;">🎯 COORDINATES</b><br>' +
                      '<b>x:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>y:</b> <span style="color:#E67E22;">%{y:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{z:.3f}</span><br>' +
                      '<b>Function:</b> <span style="color:#8E44AD;">sin(x² + y²)</span><extra></extra>',
        name='🌊 Main Surface',
        lighting=dict(
            ambient=0.4,
            diffuse=0.7,
            fresnel=0.1,
            specular=1.0,
            roughness=0.1
        ),
        lightposition=dict(x=100, y=100, z=50),
        colorbar=dict(
            title=dict(text="<b>z values</b>", font=dict(color='#2E86C1', size=14)),
            tickfont=dict(color='#333333'),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#2E86C1',
            borderwidth=2,
            len=0.4,
            x=0.47
        )
    ),
    row=1, col=1
)

fig.add_trace(
    go.Surface(
        x=X, y=Y, z=Z,
        colorscale=wireframe_colorscale,
        showscale=False,
        opacity=0.7,
        hovertemplate='<b style="color:#E74C3C;">⚡ WIREFRAME</b><br>' +
                      '<b>x:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>y:</b> <span style="color:#E67E22;">%{y:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{z:.3f}</span><extra></extra>',
        name='⚡ Wireframe',
        contours=dict(
            x=dict(show=True, start=-2*np.pi, end=2*np.pi, size=np.pi/2, color="#2E86C1", width=2),
            y=dict(show=True, start=-2*np.pi, end=2*np.pi, size=np.pi/2, color="#E74C3C", width=2),
            z=dict(show=True, start=-1, end=1, size=0.25, color="#F39C12", width=2)
        )
    ),
    row=1, col=2
)

fig.add_trace(
    go.Contour(
        x=x, y=y, z=Z,
        colorscale='RdYlBu_r',
        showscale=True,
        contours=dict(
            coloring='heatmap',
            showlabels=True,
            labelfont=dict(size=10, color='black'),
            start=-1,
            end=1,
            size=0.1
        ),
        hovertemplate='<b style="color:#17A2B8;">🔥 HEATMAP</b><br>' +
                      '<b>x:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>y:</b> <span style="color:#E67E22;">%{y:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{z:.3f}</span><extra></extra>',
        name='🔥 Contour Map',
        colorbar=dict(
            title=dict(text="<b>Intensity</b>", font=dict(color='#17A2B8', size=14)),
            tickfont=dict(color='#333333'),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#17A2B8',
            borderwidth=2,
            len=0.4,
            x=1.02
        )
    ),
    row=2, col=1
)

z_cross_x = np.sin(x**2)
z_cross_y = np.sin(y**2)

fig.add_trace(
    go.Scatter(
        x=x, y=z_cross_x,
        mode='lines+markers',
        name='🔴 x-axis (y=0)',
        line=dict(color='#E74C3C', width=4, shape='spline'),
        marker=dict(size=4, color='#E74C3C', symbol='circle'),
        hovertemplate='<b style="color:#E74C3C;">🔴 X-AXIS CROSS</b><br>' +
                      '<b>x:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{y:.3f}</span><br>' +
                      '<b>Section:</b> <span style="color:#8E44AD;">y = 0</span><extra></extra>'
    ),
    row=2, col=2
)

fig.add_trace(
    go.Scatter(
        x=y, y=z_cross_y,
        mode='lines+markers',
        name='🔵 y-axis (x=0)',
        line=dict(color='#3498DB', width=4, shape='spline'),
        marker=dict(size=4, color='#3498DB', symbol='diamond'),
        hovertemplate='<b style="color:#3498DB;">🔵 Y-AXIS CROSS</b><br>' +
                      '<b>y:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{y:.3f}</span><br>' +
                      '<b>Section:</b> <span style="color:#8E44AD;">x = 0</span><extra></extra>'
    ),
    row=2, col=2
)

diagonal = np.linspace(-2*np.pi, 2*np.pi, 120)
z_diagonal = np.sin(2 * diagonal**2)
fig.add_trace(
    go.Scatter(
        x=diagonal, y=z_diagonal,
        mode='lines+markers',
        name='🟢 Diagonal (x=y)',
        line=dict(color='#28A745', width=4, dash='dash', shape='spline'),
        marker=dict(size=4, color='#28A745', symbol='star'),
        hovertemplate='<b style="color:#28A745;">🟢 DIAGONAL</b><br>' +
                      '<b>t:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{y:.3f}</span><br>' +
                      '<b>Section:</b> <span style="color:#8E44AD;">x = y</span><extra></extra>'
    ),
    row=2, col=2
)

radial = np.linspace(0, 2*np.sqrt(2)*np.pi, 120)
z_radial = np.sin(radial**2)
fig.add_trace(
    go.Scatter(
        x=radial, y=z_radial,
        mode='lines+markers',
        name='🟡 Radial (r from origin)',
        line=dict(color='#F39C12', width=3, dash='dot', shape='spline'),
        marker=dict(size=3, color='#F39C12', symbol='triangle-up'),
        hovertemplate='<b style="color:#F39C12;">🟡 RADIAL</b><br>' +
                      '<b>r:</b> <span style="color:#E67E22;">%{x:.3f}</span><br>' +
                      '<b>z:</b> <span style="color:#27AE60;">%{y:.3f}</span><br>' +
                      '<b>Section:</b> <span style="color:#8E44AD;">radial from origin</span><extra></extra>'
    ),
    row=2, col=2
)

fig.update_layout(
    title={
        'text': '<span style="color:#2E86C1; font-size:24px;">🚀 ADVANCED 3D VISUALIZATION</span><br>' +
                '<span style="color:#E67E22; font-size:18px;">z = sin(x² + y²)</span>',
        'x': 0.5,
        'xanchor': 'center'
    },
    height=1100,
    width=1500,
    template='plotly_white',
    paper_bgcolor='white',
    plot_bgcolor='white',
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.98,
        xanchor="left",
        x=1.02,
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#2E86C1',
        borderwidth=2,
        font=dict(color='#333333', size=12)
    ),
    scene=dict(
        bgcolor='white',
        xaxis=dict(
            title=dict(text='x-axis', font=dict(color='#E74C3C', size=14)),
            tickfont=dict(color='#333333'),
            gridcolor='#CCCCCC',
            backgroundcolor='white'
        ),
        yaxis=dict(
            title=dict(text='y-axis', font=dict(color='#17A2B8', size=14)),
            tickfont=dict(color='#333333'),
            gridcolor='#CCCCCC',
            backgroundcolor='white'
        ),
        zaxis=dict(
            title=dict(text='z = sin(x² + y²)', font=dict(color='#F39C12', size=14)),
            tickfont=dict(color='#333333'),
            gridcolor='#CCCCCC',
            backgroundcolor='white'
        ),
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.2))
    ),
    scene2=dict(
        bgcolor='white',
        xaxis=dict(
            title=dict(text='x-axis', font=dict(color='#E74C3C', size=14)),
            tickfont=dict(color='#333333'),
            gridcolor='#CCCCCC',
            backgroundcolor='white'
        ),
        yaxis=dict(
            title=dict(text='y-axis', font=dict(color='#17A2B8', size=14)),
            tickfont=dict(color='#333333'),
            gridcolor='#CCCCCC',
            backgroundcolor='white'
        ),
        zaxis=dict(
            title=dict(text='z values', font=dict(color='#F39C12', size=14)),
            tickfont=dict(color='#333333'),
            gridcolor='#CCCCCC',
            backgroundcolor='white'
        ),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.8))
    )
)

fig.update_xaxes(
    title_text="<b style='color:#E74C3C;'>x values</b>", 
    showgrid=True, 
    gridcolor='#DDDDDD', 
    tickfont=dict(color='#333333'),
    row=2, col=1
)
fig.update_yaxes(
    title_text="<b style='color:#17A2B8;'>y values</b>", 
    showgrid=True, 
    gridcolor='#DDDDDD', 
    tickfont=dict(color='#333333'),
    row=2, col=1
)
fig.update_xaxes(
    title_text="<b style='color:#F39C12;'>Position / Radius</b>", 
    showgrid=True, 
    gridcolor='#DDDDDD', 
    tickfont=dict(color='#333333'),
    row=2, col=2
)
fig.update_yaxes(
    title_text="<b style='color:#27AE60;'>z values</b>", 
    showgrid=True, 
    gridcolor='#DDDDDD', 
    tickfont=dict(color='#333333'),
    row=2, col=2
)

fig.add_annotation(
    text='<span style="color:#2E86C1; font-size:20px;">⚡ z = sin(x² + y²) ⚡</span>',
    xref="paper", yref="paper",
    x=0.25, y=0.97,
    showarrow=False,
    bgcolor="rgba(46,134,193,0.1)",
    bordercolor="#2E86C1",
    borderwidth=3
)

fig.add_annotation(
    text='<span style="color:#E67E22; font-size:16px;">📊 Range: x,y ∈ [-2π, 2π] 📊</span>',
    xref="paper", yref="paper",
    x=0.75, y=0.97,
    showarrow=False,
    bgcolor="rgba(230,126,34,0.1)",
    bordercolor="#E67E22",
    borderwidth=2
)

fig.add_annotation(
    text='<span style="color:#8E44AD; font-size:12px;">🎮 INTERACTIVE CONTROLS:<br>' +
         '• 🖱️ Rotate, zoom, pan surfaces<br>' +
         '• 🎯 Hover for exact coordinates<br>' +
         '• 👁️ Toggle traces on/off<br>' +
         '• 📱 Responsive design</span>',
    xref="paper", yref="paper",
    x=0.02, y=0.02,
    showarrow=False,
    bgcolor="rgba(142,68,173,0.1)",
    bordercolor="#8E44AD",
    borderwidth=2,
    align="left"
)

fig.add_annotation(
    text='<span style="color:#17A2B8; font-size:14px;">🔬 ANALYSIS FEATURES:<br>' +
         '• Surface + Wireframe views<br>' +
         '• Contour heatmap projection<br>' +
         '• Multi-axis cross-sections<br>' +
         '• Radial symmetry analysis</span>',
    xref="paper", yref="paper",
    x=0.98, y=0.02,
    showarrow=False,
    bgcolor="rgba(23,162,184,0.1)",
    bordercolor="#17A2B8",
    borderwidth=2,
    align="left"
)

fig.show()

print("🚀 CLEAN 3D VISUALIZATION COMPLETE! 🚀")
print("✨ Professional Features:")
print("  • 🎨 Clean white theme with professional colors")
print("  • 🌈 Professional color schemes (viridis, plasma, RdYlBu)")  
print("  • 💫 Enhanced lighting optimized for white background")
print("  • 📊 Clean hover templates with professional styling")
print("  • 🎯 4 different cross-section analyses")
print("  • ⚡ Wireframe with multi-colored contours")
print("  • 🔥 Professional heatmap with custom colorbar")
print("  • 🎮 Comprehensive interactive annotations")
print("  • 📱 Responsive design for all devices")
print("  • 🚀 Ultra-high resolution (120x120 points)")
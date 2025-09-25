import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

t = np.arange(-2*np.pi, 2*np.pi, 0.005)

s = np.zeros_like(t)
s[t >= 0] = 1
f = 2 * s * np.sin(3*t)

smooth_transition_width = 0.5
s_smooth = 1 / (1 + np.exp(-t / smooth_transition_width))

f_complex = 2 * s * (np.sin(3*t) + 0.5*np.sin(9*t) + 0.25*np.sin(15*t))

envelope = np.exp(-0.2 * np.abs(t))
f_decay = 2 * s * np.sin(3*t) * envelope

f_phase1 = 2 * s * np.sin(3*t + np.pi/4)
f_phase2 = 2 * s * np.sin(3*t + np.pi/2)

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=[
        'Original vs Smooth Step Functions',
        'Multi-frequency Weighted Sine',
        'Exponentially Decaying Envelope',
        'Phase Variations Analysis'
    ],
    specs=[[{"secondary_y": False}, {"secondary_y": True}],
           [{"secondary_y": True}, {"secondary_y": False}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.1
)

fig.add_trace(
    go.Scatter(
        x=t, y=s,
        name='Sharp Step',
        line=dict(color='red', width=3),
        hovertemplate='<b>Sharp Step</b><br>t: %{x:.3f}<br>s(t): %{y:.3f}<extra></extra>'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=t, y=s_smooth,
        name='Smooth Step',
        line=dict(color='orange', width=2, dash='dash'),
        hovertemplate='<b>Smooth Step</b><br>t: %{x:.3f}<br>s_smooth(t): %{y:.3f}<extra></extra>'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=t, y=f,
        name='Original Weighted Sine',
        line=dict(color='blue', width=2),
        hovertemplate='<b>Original</b><br>t: %{x:.3f}<br>f(t): %{y:.3f}<extra></extra>'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=t, y=f_complex,
        name='Multi-frequency',
        line=dict(color='green', width=2),
        hovertemplate='<b>Multi-freq</b><br>t: %{x:.3f}<br>f(t): %{y:.3f}<extra></extra>'
    ),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(
        x=t, y=2 * s * np.sin(3*t),
        name='Base (3ω)',
        line=dict(color='lightblue', width=1, dash='dot'),
        opacity=0.7,
        hovertemplate='<b>Base freq</b><br>t: %{x:.3f}<br>f(t): %{y:.3f}<extra></extra>'
    ),
    row=1, col=2, secondary_y=True
)

fig.add_trace(
    go.Scatter(
        x=t, y=s * np.sin(9*t),
        name='Harmonic (9ω)',
        line=dict(color='lightgreen', width=1, dash='dot'),
        opacity=0.7,
        hovertemplate='<b>2nd harmonic</b><br>t: %{x:.3f}<br>f(t): %{y:.3f}<extra></extra>'
    ),
    row=1, col=2, secondary_y=True
)

fig.add_trace(
    go.Scatter(
        x=t, y=f_decay,
        name='Decaying Sine',
        line=dict(color='purple', width=2),
        hovertemplate='<b>Decaying</b><br>t: %{x:.3f}<br>f(t): %{y:.3f}<extra></extra>'
    ),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(
        x=t, y=envelope,
        name='Envelope',
        line=dict(color='magenta', width=2, dash='dash'),
        opacity=0.8,
        hovertemplate='<b>Envelope</b><br>t: %{x:.3f}<br>env(t): %{y:.3f}<extra></extra>'
    ),
    row=2, col=1, secondary_y=True
)

colors = ['darkblue', 'darkred', 'darkgreen']
phases = [0, np.pi/4, np.pi/2]
phase_names = ['0°', '45°', '90°']
phase_functions = [f, f_phase1, f_phase2]

for i, (phase_f, color, phase_name) in enumerate(zip(phase_functions, colors, phase_names)):
    fig.add_trace(
        go.Scatter(
            x=t, y=phase_f,
            name=f'Phase {phase_name}',
            line=dict(color=color, width=2),
            hovertemplate=f'<b>Phase {phase_name}</b><br>t: %{{x:.3f}}<br>f(t): %{{y:.3f}}<extra></extra>'
        ),
        row=2, col=2
    )

fig.update_layout(
    title={
        'text': 'Advanced Task 2: Multi-Aspect Analysis of Step-Weighted Sinusoids',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16}
    },
    height=800,
    width=1200,
    template='plotly_white',
    hovermode='closest',
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02
    )
)

fig.update_xaxes(title_text="Time (t)", showgrid=True, gridcolor='lightgray')
fig.update_yaxes(title_text="Amplitude", showgrid=True, gridcolor='lightgray')

fig.add_annotation(
    x=0, y=1,
    text="Step Transition",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="red",
    ax=20, ay=-30,
    row=1, col=1
)

fig.add_annotation(
    text="f(t) = 2·s(t)·sin(3t)",
    xref="paper", yref="paper",
    x=0.25, y=0.95,
    showarrow=False,
    font=dict(size=12, color="blue"),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor="blue",
    borderwidth=1
)

fig.add_annotation(
    text="f_complex(t) = 2·s(t)·[sin(3t) + 0.5·sin(9t) + 0.25·sin(15t)]",
    xref="paper", yref="paper",
    x=0.75, y=0.95,
    showarrow=False,
    font=dict(size=10, color="green"),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor="green",
    borderwidth=1
)

fig.add_annotation(
    text="f_decay(t) = 2·s(t)·sin(3t)·e^(-0.2|t|)",
    xref="paper", yref="paper",
    x=0.25, y=0.45,
    showarrow=False,
    font=dict(size=10, color="purple"),
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor="purple",
    borderwidth=1
)

fig.show()

print("Advanced Task 2 Analysis Complete!")
print("Features included:")
print("1. High-resolution plotting (0.005 step size)")
print("2. Smooth step function using sigmoid")
print("3. Multi-frequency harmonic analysis")
print("4. Exponential decay envelope")
print("5. Phase shift analysis")
print("6. Interactive subplots with detailed hover information")
print("7. Mathematical annotations and formulas")
print("8. Secondary y-axes for component analysis")

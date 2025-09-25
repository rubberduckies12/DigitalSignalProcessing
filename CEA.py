import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dataclasses import dataclass
import pandas as pd

@dataclass
class CEAComponents:
    """Common Emitter Amplifier component values"""
    Vcc: float = 12.0      # Supply voltage (V)
    RB: float = 100e3      # Base resistor (Ω)
    RC: float = 4.7e3      # Collector resistor (Ω)
    RE: float = 1e3        # Emitter resistor (Ω)
    C1: float = 10e-6      # Input coupling capacitor (F)
    C2: float = 10e-6      # Output coupling capacitor (F)
    CE: float = 100e-6     # Emitter bypass capacitor (F)
    beta: float = 100      # Transistor current gain
    VBE: float = 0.7       # Base-emitter voltage drop (V)
    Vin_amp: float = 0.01  # Input signal amplitude (V)
    freq: float = 1000     # Signal frequency (Hz)

class CEASimulator:
    def __init__(self, components: CEAComponents):
        self.comp = components
        self.calculate_all()
        
    def calculate_operating_point(self):
        """Calculate DC operating point"""
        # Thévenin equivalent for bias circuit
        self.VTH = self.comp.Vcc * self.comp.RB / (self.comp.RB + self.comp.RB)  # Simplified
        self.RTH = self.comp.RB
        
        # Base current
        self.IB = (self.comp.Vcc - self.comp.VBE) / (self.comp.RB + self.comp.beta * self.comp.RE)
        
        # Collector current
        self.IC = self.comp.beta * self.IB
        
        # Emitter current
        self.IE = self.IC + self.IB
        
        # Node voltages
        self.VE = self.IE * self.comp.RE
        self.VB = self.comp.VBE + self.VE
        self.VC = self.comp.Vcc - self.IC * self.comp.RC
        self.VCE = self.VC - self.VE
        
    def calculate_ac_analysis(self):
        """Calculate AC small-signal parameters"""
        # Transconductance
        self.gm = self.IC / 0.026  # VT = 26mV at room temp
        
        # AC voltage gain (with RE unbypassed)
        self.Av_with_RE = -self.gm * self.comp.RC / (1 + self.gm * self.comp.RE)
        
        # AC voltage gain (with RE bypassed by CE)
        self.Av_bypassed = -self.gm * self.comp.RC
        
        # Input impedance
        self.Rin = self.comp.RB
        
        # Output impedance
        self.Rout = self.comp.RC
        
    def calculate_frequency_response(self):
        """Calculate frequency response"""
        frequencies = np.logspace(1, 6, 1000)
        
        # Low frequency response (coupling capacitors)
        fc_low = 1 / (2 * np.pi * self.Rin * self.comp.C1)
        
        # High frequency response (simplified)
        fc_high = 1e6  # 1MHz typical
        
        # Calculate magnitude response
        H_low = frequencies / np.sqrt(frequencies**2 + fc_low**2)
        H_high = fc_high / np.sqrt(frequencies**2 + fc_high**2)
        
        gain_magnitude = abs(self.Av_bypassed) * H_low * H_high
        gain_db = 20 * np.log10(np.maximum(gain_magnitude, 1e-10))
        phase = -180 + np.arctan(frequencies/fc_low) * 180/np.pi - np.arctan(frequencies/fc_high) * 180/np.pi
        
        return frequencies, gain_db, phase
        
    def calculate_all(self):
        """Calculate all circuit parameters"""
        self.calculate_operating_point()
        self.calculate_ac_analysis()
        
    def get_waveforms(self, t_points=1000):
        """Generate input/output waveforms"""
        t = np.linspace(0, 5/self.comp.freq, t_points)
        
        # Input waveform
        vin = self.comp.Vin_amp * np.sin(2 * np.pi * self.comp.freq * t)
        
        # Output waveform (AC coupled)
        vout = self.Av_bypassed * vin  # AC component only
        
        # DC + AC output
        vout_total = self.VC + vout
        
        return t, vin, vout, vout_total

def create_interactive_circuit_diagram(simulator):
    """Create interactive circuit diagram with hover information"""
    
    fig = go.Figure()
    
    # Circuit node positions
    nodes = {
        'vin': (-2, 0),
        'base': (0, 0),
        'collector': (2, 2),
        'emitter': (2, -2),
        'vout': (4, 2),
        'vcc': (2, 4),
        'gnd': (0, -4)
    }
    
    # Add interactive components
    components = [
        {
            'name': 'Vin',
            'pos': nodes['vin'],
            'symbol': '~',
            'color': '#9B59B6',
            'info': f"AC Input Signal<br>Amplitude: {simulator.comp.Vin_amp*1000:.1f}mV<br>Frequency: {simulator.comp.freq}Hz",
            'size': 30
        },
        {
            'name': 'RB',
            'pos': (-1, 2),
            'symbol': '⬜',
            'color': '#3498DB',
            'info': f"Base Bias Resistor<br>Value: {simulator.comp.RB/1e3:.1f}kΩ<br>Sets IB = {simulator.IB*1e6:.1f}µA",
            'size': 25
        },
        {
            'name': 'RC',
            'pos': (2, 3),
            'symbol': '⬜',
            'color': '#E74C3C',
            'info': f"Collector Resistor<br>Value: {simulator.comp.RC/1e3:.1f}kΩ<br>Sets gain ≈ RC/RE",
            'size': 25
        },
        {
            'name': 'RE',
            'pos': (2, -3),
            'symbol': '⬜',
            'color': '#27AE60',
            'info': f"Emitter Resistor<br>Value: {simulator.comp.RE/1e3:.1f}kΩ<br>Provides stability",
            'size': 25
        },
        {
            'name': 'Q1',
            'pos': nodes['base'],
            'symbol': '▲',
            'color': '#F39C12',
            'info': f"NPN Transistor<br>β = {simulator.comp.beta}<br>VBE = {simulator.comp.VBE}V<br>gm = {simulator.gm:.3f}S",
            'size': 35
        },
        {
            'name': 'Vcc',
            'pos': nodes['vcc'],
            'symbol': '⊕',
            'color': '#E67E22',
            'info': f"Supply Voltage<br>Value: {simulator.comp.Vcc}V<br>Powers the circuit",
            'size': 30
        }
    ]
    
    # Add components with hover information
    for comp in components:
        fig.add_trace(go.Scatter(
            x=[comp['pos'][0]], 
            y=[comp['pos'][1]],
            mode='markers+text',
            marker=dict(
                size=comp['size'],
                color=comp['color'],
                symbol='circle',
                line=dict(width=2, color='white')
            ),
            text=[comp['symbol']],
            textposition="middle center",
            textfont=dict(size=14, color='white'),
            name=comp['name'],
            hovertemplate=f"<b>{comp['name']}</b><br>{comp['info']}<extra></extra>",
            showlegend=False
        ))
    
    # Add voltage node indicators with real values
    voltage_nodes = [
        ('VB', nodes['base'], f"{simulator.VB:.2f}V", '#3498DB'),
        ('VC', nodes['collector'], f"{simulator.VC:.2f}V", '#E74C3C'),
        ('VE', nodes['emitter'], f"{simulator.VE:.2f}V", '#27AE60'),
    ]
    
    for name, pos, value, color in voltage_nodes:
        fig.add_annotation(
            x=pos[0], y=pos[1]+0.7,
            text=f"<b>{name}={value}</b>",
            showarrow=False,
            font=dict(size=12, color=color),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor=color,
            borderwidth=2
        )
    
    # Add connection wires
    connections = [
        # Input to base
        ([nodes['vin'][0], nodes['base'][0]], [nodes['vin'][1], nodes['base'][1]]),
        # Base bias
        ([nodes['base'][0], -1], [nodes['base'][1], 2]),
        ([-1, nodes['vcc'][0]], [2, nodes['vcc'][1]]),
        # Collector circuit
        ([nodes['collector'][0], nodes['collector'][0]], [nodes['collector'][1], 3]),
        ([nodes['collector'][0], nodes['vcc'][0]], [3, nodes['vcc'][1]]),
        # Emitter circuit
        ([nodes['emitter'][0], nodes['emitter'][0]], [nodes['emitter'][1], -3]),
        ([nodes['emitter'][0], 0], [-3, -4]),
        # Output
        ([nodes['collector'][0], nodes['vout'][0]], [nodes['collector'][1], nodes['vout'][1]]),
    ]
    
    for connection in connections:
        fig.add_trace(go.Scatter(
            x=connection[0], 
            y=connection[1],
            mode='lines',
            line=dict(color='#34495E', width=3),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add ground symbols
    ground_points = [nodes['gnd'], (4, 1), (-2, -1)]
    for gp in ground_points:
        fig.add_shape(
            type="line",
            x0=gp[0]-0.2, y0=gp[1],
            x1=gp[0]+0.2, y1=gp[1],
            line=dict(color="#7F8C8D", width=4)
        )
    
    fig.update_layout(
        title="🔧 Interactive Common Emitter Amplifier Circuit",
        xaxis=dict(range=[-3, 5], showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(range=[-5, 5], showgrid=False, showticklabels=False, zeroline=False),
        plot_bgcolor='white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

def create_unified_dashboard():
    """Create unified interactive dashboard"""
    
    # Initialize with default values
    default_components = CEAComponents()
    simulator = CEASimulator(default_components)
    
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    app.layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("🚀 Interactive Common Emitter Amplifier Simulator", 
                       className="text-center mb-4"),
                html.Hr()
            ])
        ]),
        
        # Control Panel
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🎛️ Circuit Parameters"),
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.Label("Supply Voltage (V):"),
                                dcc.Slider(
                                    id='vcc-slider',
                                    min=5, max=20, step=0.5, value=12,
                                    marks={i: str(i) for i in range(5, 21, 5)},
                                    tooltip={"placement": "bottom", "always_visible": True}
                                )
                            ], width=3),
                            dbc.Col([
                                html.Label("Base Resistor (kΩ):"),
                                dcc.Slider(
                                    id='rb-slider',
                                    min=10, max=500, step=10, value=100,
                                    marks={i: str(i) for i in range(0, 501, 100)},
                                    tooltip={"placement": "bottom", "always_visible": True}
                                )
                            ], width=3),
                            dbc.Col([
                                html.Label("Collector Resistor (kΩ):"),
                                dcc.Slider(
                                    id='rc-slider',
                                    min=1, max=10, step=0.1, value=4.7,
                                    marks={i: str(i) for i in range(1, 11, 2)},
                                    tooltip={"placement": "bottom", "always_visible": True}
                                )
                            ], width=3),
                            dbc.Col([
                                html.Label("Emitter Resistor (kΩ):"),
                                dcc.Slider(
                                    id='re-slider',
                                    min=0.1, max=5, step=0.1, value=1.0,
                                    marks={i: str(i) for i in range(0, 6)},
                                    tooltip={"placement": "bottom", "always_visible": True}
                                )
                            ], width=3)
                        ]),
                        html.Hr(),
                        dbc.Row([
                            dbc.Col([
                                html.Label("Input Amplitude (mV):"),
                                dcc.Slider(
                                    id='vin-slider',
                                    min=1, max=50, step=1, value=10,
                                    marks={i: str(i) for i in range(0, 51, 10)},
                                    tooltip={"placement": "bottom", "always_visible": True}
                                )
                            ], width=6),
                            dbc.Col([
                                html.Label("Frequency (Hz):"),
                                dcc.Slider(
                                    id='freq-slider',
                                    min=100, max=10000, step=100, value=1000,
                                    marks={i: f"{i//1000}k" if i>=1000 else str(i) for i in [100, 1000, 5000, 10000]},
                                    tooltip={"placement": "bottom", "always_visible": True}
                                )
                            ], width=6)
                        ])
                    ])
                ])
            ], width=12)
        ], className="mb-4"),
        
        # Main Dashboard
        dbc.Row([
            # Circuit Diagram
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🔧 Interactive Circuit"),
                    dbc.CardBody([
                        dcc.Graph(id='circuit-diagram')
                    ])
                ])
            ], width=6),
            
            # Operating Point Display
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📊 Operating Point"),
                    dbc.CardBody([
                        html.Div(id='operating-point-display')
                    ])
                ])
            ], width=6)
        ], className="mb-4"),
        
        # Waveform Analysis
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🌊 Real-time Waveform Analysis"),
                    dbc.CardBody([
                        dcc.Graph(id='waveform-analysis')
                    ])
                ])
            ], width=12)
        ], className="mb-4"),
        
        # Frequency Response & Sensitivity
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("📈 Frequency Response"),
                    dbc.CardBody([
                        dcc.Graph(id='frequency-response')
                    ])
                ])
            ], width=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("🎯 Parameter Sensitivity"),
                    dbc.CardBody([
                        dcc.Graph(id='sensitivity-analysis')
                    ])
                ])
            ], width=6)
        ])
    ], fluid=True)
    
    # Callback for real-time updates
    @app.callback(
        [Output('circuit-diagram', 'figure'),
         Output('operating-point-display', 'children'),
         Output('waveform-analysis', 'figure'),
         Output('frequency-response', 'figure'),
         Output('sensitivity-analysis', 'figure')],
        [Input('vcc-slider', 'value'),
         Input('rb-slider', 'value'),
         Input('rc-slider', 'value'),
         Input('re-slider', 'value'),
         Input('vin-slider', 'value'),
         Input('freq-slider', 'value')]
    )
    def update_dashboard(vcc, rb, rc, re, vin_mv, freq):
        # Create new components with slider values
        components = CEAComponents(
            Vcc=vcc,
            RB=rb*1000,  # Convert to ohms
            RC=rc*1000,
            RE=re*1000,
            Vin_amp=vin_mv/1000,  # Convert to volts
            freq=freq
        )
        
        # Create new simulator
        sim = CEASimulator(components)
        
        # 1. Update circuit diagram
        circuit_fig = create_interactive_circuit_diagram(sim)
        
        # 2. Operating point display
        op_display = [
            dbc.Row([
                dbc.Col([
                    dbc.Alert([
                        html.H5("🔋 DC Operating Point", className="alert-heading"),
                        html.P(f"Base Current: {sim.IB*1e6:.1f} µA"),
                        html.P(f"Collector Current: {sim.IC*1e3:.1f} mA"),
                        html.P(f"VCE: {sim.VCE:.2f} V"),
                        html.P(f"Operating Region: {'✅ Active' if 2 < sim.VCE < vcc-2 else '❌ Not Active'}")
                    ], color="primary")
                ], width=6),
                dbc.Col([
                    dbc.Alert([
                        html.H5("⚡ AC Performance", className="alert-heading"),
                        html.P(f"Voltage Gain: {sim.Av_bypassed:.1f}"),
                        html.P(f"Input Impedance: {sim.Rin/1000:.1f} kΩ"),
                        html.P(f"Transconductance: {sim.gm:.3f} S"),
                        html.P(f"Output Swing: ±{min(sim.VC, vcc-sim.VC):.1f} V")
                    ], color="success")
                ], width=6)
            ])
        ]
        
        # 3. Waveform analysis
        t, vin, vout, vout_total = sim.get_waveforms()
        
        waveform_fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=["Input Signal", "Output Signal"],
            shared_xaxes=True
        )
        
        waveform_fig.add_trace(
            go.Scatter(x=t*1000, y=vin*1000, name="Input (mV)", line=dict(color='#3498DB')),
            row=1, col=1
        )
        
        waveform_fig.add_trace(
            go.Scatter(x=t*1000, y=vout_total, name="Output (V)", line=dict(color='#E74C3C')),
            row=2, col=1
        )
        
        waveform_fig.add_trace(
            go.Scatter(x=t*1000, y=[sim.VC]*len(t), name="DC Level", 
                      line=dict(color='#95A5A6', dash='dash')),
            row=2, col=1
        )
        
        waveform_fig.update_layout(height=400, title="Real-time Waveform Analysis")
        waveform_fig.update_xaxes(title_text="Time (ms)", row=2, col=1)
        waveform_fig.update_yaxes(title_text="Amplitude (mV)", row=1, col=1)
        waveform_fig.update_yaxes(title_text="Amplitude (V)", row=2, col=1)
        
        # 4. Frequency response
        frequencies, gain_db, phase = sim.calculate_frequency_response()
        
        freq_fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=["Magnitude Response", "Phase Response"],
            shared_xaxes=True
        )
        
        freq_fig.add_trace(
            go.Scatter(x=frequencies, y=gain_db, name="Gain (dB)", line=dict(color='#27AE60')),
            row=1, col=1
        )
        
        freq_fig.add_trace(
            go.Scatter(x=frequencies, y=phase, name="Phase (°)", line=dict(color='#8E44AD')),
            row=2, col=1
        )
        
        freq_fig.update_xaxes(type="log", title_text="Frequency (Hz)", row=2, col=1)
        freq_fig.update_yaxes(title_text="Gain (dB)", row=1, col=1)
        freq_fig.update_yaxes(title_text="Phase (°)", row=2, col=1)
        freq_fig.update_layout(height=400, title="Frequency Response Analysis")
        
        # 5. Sensitivity analysis
        rc_range = np.linspace(1, 10, 20)
        re_range = np.linspace(0.5, 3, 20)
        gains = []
        
        for rc_val in rc_range:
            row_gains = []
            for re_val in re_range:
                gain = rc_val / re_val
                row_gains.append(gain)
            gains.append(row_gains)
        
        sensitivity_fig = go.Figure(data=go.Heatmap(
            z=gains,
            x=re_range,
            y=rc_range,
            colorscale='Viridis',
            hovertemplate='RC: %{y:.1f}kΩ<br>RE: %{x:.1f}kΩ<br>Gain: %{z:.1f}<extra></extra>'
        ))
        
        sensitivity_fig.update_layout(
            title="Gain Sensitivity to RC and RE",
            xaxis_title="RE (kΩ)",
            yaxis_title="RC (kΩ)"
        )
        
        return circuit_fig, op_display, waveform_fig, freq_fig, sensitivity_fig
    
    return app

if __name__ == "__main__":
    app = create_unified_dashboard()
    app.run_server(debug=True)
<div align="center">

# 🚀 Digital Signal Processing & Interactive Visualization Suite

<img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Plotly-Interactive-brightgreen?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
<img src="https://img.shields.io/badge/NumPy-Mathematical-orange?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/Status-Complete-success?style=for-the-badge" alt="Status">

### 🎯 Advanced Mathematical Visualization & Signal Analysis

*Transform static plots into interactive experiences*

---

</div>

## 🌟 Project Overview

This repository contains a comprehensive suite of **interactive mathematical visualizations** built with Python, featuring advanced signal processing concepts and 3D mathematical functions. Each task demonstrates the evolution from basic static plots to sophisticated, interactive analytical tools.

<details>
<summary>🎮 <strong>Click to see what makes this special</strong></summary>

```
✨ From Static to Interactive
📊 Multi-dimensional Analysis  
🎯 Real-time Hover Information
🌈 Professional Color Schemes
📱 Responsive Design
🔬 Mathematical Annotations
⚡ High-Performance Rendering
```

</details>

---

## 📁 Project Structure

```
universityWork/
├── task1/
│   └── task1.py          # 🌊 Interactive Cosine Visualization
├── task2/
│   └── task2.py          # ⚡ Advanced Step-Weighted Sinusoids
├── task3/
│   └── task3.py          # 🚀 3D Surface & Multi-Panel Analysis
└── README.md             # 📖 This comprehensive guide
```

---

## 🎯 Task Breakdown

### 🌊 Task 1: Interactive Cosine Function
**From basic matplotlib to stunning interactive visualization**

<div align="center">

```python
# Original Challenge: Plot f(t) = 5*cos(t)
t = np.arange(-2*np.pi, 2*np.pi, 0.01)
f = 5 * np.cos(t)
```

</div>

**🔥 Enhanced Features:**
- ✨ **Interactive Star Markers**: Hover for exact coordinates
- 🎯 **Smart Hover Templates**: Displays t, f(t), and function name
- 📱 **Zoom & Pan**: Full mouse/touch interaction
- 🌈 **Professional Styling**: Custom colors and grid systems
- ⚡ **High Resolution**: Smooth curve rendering

**🚀 Technologies:** `plotly.graph_objects`, `numpy`, interactive hover systems

---

### ⚡ Task 2: Multi-Aspect Signal Analysis
**Advanced step-weighted sinusoids with comprehensive analysis**

<div align="center">

```python
# Core Function: f(t) = 2 * s(t) * sin(3t)
# Where s(t) is a step function
```

</div>

**🔬 Advanced Analysis Components:**

<table>
<tr>
<td width="50%">

**📊 Panel 1: Step Function Comparison**
- Sharp vs Smooth step transitions
- Sigmoid-based smooth stepping
- Mathematical formula overlays

**🎵 Panel 2: Multi-Frequency Analysis**
- Base frequency (3ω)
- 2nd harmonic (9ω) 
- 3rd harmonic (15ω)
- Complex waveform synthesis

</td>
<td width="50%">

**💫 Panel 3: Exponential Decay**
- Time-varying envelope: `e^(-0.2|t|)`
- Amplitude modulation effects
- Decay visualization

**🔄 Panel 4: Phase Analysis**
- 0°, 45°, 90° phase shifts
- Comparative waveform analysis
- Phase relationship visualization

</td>
</tr>
</table>

**🎨 Visual Enhancements:**
- 🌈 **4-Panel Layout**: Comprehensive multi-aspect analysis
- 🎯 **Rich Hover Information**: Detailed coordinate and function data
- 📈 **Secondary Y-Axes**: Component comparison capabilities
- 🔬 **Mathematical Annotations**: Formula displays and explanations

---

### 🚀 Task 3: Ultimate 3D Visualization Suite
**Professional-grade 3D mathematical surface analysis**

<div align="center">

```python
# Challenge: Visualize z = sin(x² + y²) for x,y ∈ [-2π, 2π]
# Solution: 4-panel interactive 3D analysis system
```

</div>

**🌟 Four-Panel Analysis System:**

| Panel | Description | Features |
|-------|-------------|----------|
| 🌊 **3D Surface** | Interactive surface plot | Advanced lighting, custom colorbars, smooth rendering |
| ⚡ **Wireframe** | Contour-enhanced wireframe | Multi-colored contour lines, transparency effects |
| 🔥 **Heatmap** | 2D contour projection | Turbo colorscale, labeled contours, intensity mapping |
| 📊 **Cross-Sections** | Multi-axis analysis | 4 different cross-sectional views with styling |

**🎯 Cross-Sectional Analysis:**
- 🔴 **X-Axis Cross-Section** (y=0): `z = sin(x²)`
- 🔵 **Y-Axis Cross-Section** (x=0): `z = sin(y²)`
- 🟢 **Diagonal Cross-Section** (x=y): `z = sin(2t²)`
- 🟡 **Radial Analysis**: Distance from origin effects

**💎 Professional Features:**
- 🎨 **Clean White Theme**: Professional academic presentation
- 🌈 **Multiple Color Schemes**: Viridis, Plasma, RdYlBu for different data aspects
- 💫 **Advanced 3D Lighting**: Ambient, diffuse, specular lighting systems
- 📱 **Responsive Design**: Optimized for different screen sizes
- 🎮 **Interactive Annotations**: Comprehensive feature descriptions
- 🚀 **Ultra-High Resolution**: 120×120 point sampling for smooth surfaces

---

## 🛠️ Installation & Setup

### Prerequisites
```bash
# Ensure Python 3.9+ is installed
python3 --version
```

### Quick Start
```bash
# Clone or navigate to the project directory
cd universityWork

# Install required packages
pip install numpy plotly

# Or use requirements file
pip install -r requirements.txt
```

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Install packages
pip install numpy plotly
```

---

## 🚀 Running the Visualizations

### Task 1: Interactive Cosine
```bash
cd task1
python3 task1.py
```
**Expected Output:** Browser opens with interactive cosine visualization

### Task 2: Advanced Signal Analysis
```bash
cd task2
python3 task2.py
```
**Expected Output:** 4-panel signal processing analysis dashboard

### Task 3: 3D Mathematical Surface
```bash
cd task3
python3 task3.py
```
**Expected Output:** Professional 3D visualization suite with multiple analysis panels

---

## 🎨 Visual Showcase

<div align="center">

### 🌊 Task 1: Interactive Cosine
*Hover-enabled star markers with professional styling*

### ⚡ Task 2: Multi-Panel Signal Analysis
*Comprehensive 4-panel analysis with mathematical annotations*

### 🚀 Task 3: 3D Surface Visualization Suite
*Professional-grade 3D analysis with multiple perspectives*

</div>

---

## 🧠 Mathematical Concepts Demonstrated

<details>
<summary>📚 <strong>Click to explore the mathematics</strong></summary>

### 🔢 Core Functions

**Task 1:** `f(t) = 5cos(t)`
- Basic trigonometric visualization
- Period: 2π, Amplitude: 5

**Task 2:** `f(t) = 2·s(t)·sin(3t)` where `s(t) = H(t)` (Heaviside)
- Step function analysis
- Harmonic content: `sin(3t) + 0.5sin(9t) + 0.25sin(15t)`
- Envelope modulation: `e^(-0.2|t|)`
- Phase variations: 0°, π/4, π/2

**Task 3:** `z = sin(x² + y²)`
- 2D → 3D mapping
- Radial symmetry properties
- Cross-sectional analysis in multiple planes

### 🔬 Advanced Concepts
- **Signal Processing**: Frequency domain analysis, harmonic synthesis
- **Mathematical Visualization**: Multi-dimensional data representation
- **Interactive Analysis**: Real-time parameter exploration
- **Professional Presentation**: Academic-quality visualization standards

</details>

---

## 🎯 Key Features & Innovations

<table>
<tr>
<td width="33%" align="center">

### 🎮 **Interactivity**
- Real-time hover information
- Zoom, pan, rotate capabilities
- Toggle trace visibility
- Responsive touch/mouse control

</td>
<td width="33%" align="center">

### 🎨 **Professional Design**
- Clean white theme
- Bootstrap-inspired color palette
- Mathematical typography
- Academic presentation standards

</td>
<td width="33%" align="center">

### 🔬 **Advanced Analysis**
- Multi-panel layouts
- Cross-sectional analysis
- Harmonic decomposition
- Phase relationship studies

</td>
</tr>
</table>

---

## 🛡️ Technical Specifications

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Core Language** | Python | 3.9+ | Mathematical computation |
| **Visualization** | Plotly | Latest | Interactive plotting |
| **Mathematics** | NumPy | Latest | Numerical arrays & functions |
| **3D Graphics** | WebGL | Auto | Hardware-accelerated rendering |
| **UI Framework** | HTML/CSS/JS | Auto | Interactive web interface |

**Performance Optimizations:**
- ⚡ High-resolution sampling (up to 120×120 points)
- 🎯 Efficient memory management
- 🚀 WebGL-accelerated 3D rendering
- 📱 Responsive design for multiple devices

---

## 📈 Learning Outcomes

<details>
<summary>🎓 <strong>Skills and concepts mastered</strong></summary>

### 🔧 Technical Skills
- **Python Programming**: Advanced NumPy operations, object-oriented design
- **Data Visualization**: Plotly ecosystem, interactive plot design
- **Mathematical Computing**: Signal processing, 3D function analysis
- **Web Technologies**: HTML/CSS integration, responsive design

### 📊 Mathematical Concepts
- **Trigonometric Functions**: Cosine, sine transformations
- **Signal Processing**: Step functions, harmonic analysis, phase relationships
- **3D Mathematics**: Surface visualization, cross-sectional analysis
- **Interactive Analysis**: Parameter exploration, multi-dimensional data

### 🎨 Design Principles
- **User Experience**: Intuitive interaction design
- **Visual Communication**: Effective mathematical presentation
- **Professional Standards**: Academic-quality visualizations
- **Accessibility**: Cross-platform compatibility

</details>

---

## 🤝 Contributing & Usage

### 📝 Academic Use
This project is designed for educational purposes and demonstrates advanced mathematical visualization techniques. Feel free to adapt and extend for your own learning projects.

### 🔧 Customization
Each task can be modified by adjusting:
- **Mathematical functions**: Change equations and parameters
- **Color schemes**: Modify colorscales and themes
- **Resolution**: Adjust sampling rates for performance/quality trade-offs
- **Layout**: Customize panel arrangements and sizing

### 🐛 Issues & Improvements
Found a bug or have an enhancement idea? The code is designed to be readable and modular for easy modification.

---

## 🏆 Project Achievements

<div align="center">

🎯 **Transformed static MATLAB-style plots into modern interactive visualizations**

⚡ **Implemented advanced signal processing concepts with real-time analysis**

🚀 **Created professional-grade 3D mathematical visualization suite**

📱 **Achieved responsive design compatible with multiple devices**

🔬 **Demonstrated academic-quality mathematical presentation standards**

</div>

---

## 📚 References & Inspiration

- **Mathematical Functions**: Classical signal processing and trigonometry
- **Visualization Design**: Modern web-based scientific plotting standards
- **Interaction Design**: Professional data analysis application patterns
- **Color Theory**: Scientific visualization best practices

---

<div align="center">

### 🌟 Ready to Explore?

**Choose your visualization journey:**

[🌊 Start with Task 1](task1/) | [⚡ Jump to Task 2](task2/) | [🚀 Experience Task 3](task3/)

---

*Built with ❤️ using Python, NumPy & Plotly*

**Happy Visualizing! 🎉**

</div>

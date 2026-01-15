# Lattice Boltzmann Simulation of Vortex Shedding Behind a Cylinder

This repository contains a **from-scratch Python implementation of the Lattice Boltzmann Method (LBM)** to simulate **vortex shedding behind a circular cylinder** in 2D.

The project was built as a hands-on exploration after repeatedly encountering vortex shedding in fluid mechanics textbooks and wanting to understand how it emerges numerically.

---

## 🌊 What This Simulation Shows

- 2D incompressible flow past a circular cylinder  
- Formation of alternating vortices (von Kármán vortex street)
- Vorticity (curl of velocity field) visualization
- Time-dependent wake dynamics at moderate Reynolds number

The simulation uses the **D2Q9 lattice** with a **BGK (single-relaxation-time) collision operator**.

---

<img width="1480" height="424" alt="image" src="https://github.com/user-attachments/assets/7aae5bf4-80df-47ac-a54f-de76b8eb7f7f" />


## 🧠 Method Overview

- **Numerical Method:** Lattice Boltzmann Method (LBM)
- **Lattice:** D2Q9
- **Collision Model:** BGK
- **Boundary Conditions:**
  - Bounce-back no-slip condition on the cylinder
  - Simple inlet/outlet boundary treatment
- **Macroscopic Quantities:**
  - Density and velocity obtained as moments of the distribution functions
- **Visualization:**
  - Vorticity (curl of velocity field)

## 🛠️ Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies with:
```bash
pip install numpy matplotlib

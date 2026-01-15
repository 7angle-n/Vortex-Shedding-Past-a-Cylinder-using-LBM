import numpy as np
import matplotlib.pyplot as plt

# Parameters
Nx, Ny = 400, 100
rho0 = 100
tau = 0.53
Nt = 30000
plot_every = 100

# Lattice speeds and weights
NL = 9
cxs = np.array([0, 0, 1, 1, 1, 0, -1, -1, -1])
cys = np.array([0, 1, 1, 0, -1, -1, -1, 0, 1])
weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])

def distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial conditions
F = np.ones((Ny, Nx, NL)) + 0.01*np.random.randn(Ny, Nx, NL)
F[:, :, 3] = 2.3
rho = np.sum(F, axis=2)
for i in range(NL):
    F[:, :, i] *= rho0 / rho

# Cylinder mask
cylinder = np.zeros((Ny, Nx), dtype=bool)
for y in range(Ny):
    for x in range(Nx):
        if distance(Nx//4, Ny//2, x, y) < 13:
            cylinder[y, x] = True

# Simulation loop
for it in range(Nt):
    # Simple inlet/outlet
    F[:, -1, [6,7,8]] = F[:, -2, [6,7,8]]
    F[:, 0, [2,3,4]] = F[:, 1, [2,3,4]]

    # Drift (streaming)
    for i, cx, cy in zip(range(NL), cxs, cys):
        F[:, :, i] = np.roll(F[:, :, i], cx, axis=1)
        F[:, :, i] = np.roll(F[:, :, i], cy, axis=0)

    # Bounce-back on cylinder
    bndryF = F[cylinder, :]
    bndryF = bndryF[:, [0,5,6,7,8,1,2,3,4]]
    F[cylinder, :] = bndryF

    # Macroscopic variables
    rho = np.sum(F, axis=2)
    ux = np.sum(F * cxs, axis=2) / rho
    uy = np.sum(F * cys, axis=2) / rho
    ux[cylinder] = 0
    uy[cylinder] = 0

    # Collision
    Feq = np.zeros_like(F)
    for i, cx, cy, w in zip(range(NL), cxs, cys, weights):
        cu = cx*ux + cy*uy
        Feq[:, :, i] = rho * w * (1 + 3*cu + 4.5*cu**2 - 1.5*(ux**2 + uy**2))
    F += -(1.0/tau) * (F - Feq)

    # Visualization
    if it % plot_every == 0:
        dUydx = uy[1:-1, 2:] - uy[1:-1, :-2]
        dUxdy = ux[2:, 1:-1] - ux[:-2, 1:-1]
        curl = dUydx - dUxdy

        plt.imshow(curl, cmap="bwr")
        plt.pause(0.1)
        plt.cla()

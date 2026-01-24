import matplotlib.pyplot as plt
import numpy as np

# Fig. 1: Manifold Visualization
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# Sample 128D points projected to 3D (PCA-like)
points = np.random.randn(1000, 3) * 0.5
ax.scatter(points[:, 0], points[:, 1], points[:, 2], alpha=0.5)
# Viability set as ellipsoid
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r", alpha=0.3)
ax.set_title("Cognitive Manifold with Viability Set K")
plt.savefig("figures/manifold_viability_set.png")
plt.show()

# Fig. 2: Tri-band Schematic
fig, ax = plt.subplots()
bands = ['Regulatory (32D)', 'Pathway (64D)', 'Affective (32D)']
colors = ['red', 'blue', 'purple']
bottom = 0
for band, color in zip(bands, colors):
    ax.barh(0, 1, left=bottom, height=0.5, color=color, label=band)
    bottom += 1
ax.set_xlim(0, 3)
ax.set_yticks([])
ax.legend()
ax.set_title("Tri-band Homeostasis Mechanism")
plt.savefig("figures/tri_band_schematic.png")
plt.show()

# Fig. 3: Pathways Topology
fig, ax = plt.subplots()
# Central CCN
ax.scatter(0, 0, s=200, color='black', label='CCN')
# Eight pathways
angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
for i, angle in enumerate(angles):
    x, y = np.cos(angle), np.sin(angle)
    ax.scatter(x, y, s=100, label=f'Pathway {i+1}')
    ax.arrow(0, 0, x*0.8, y*0.8, head_width=0.05, head_length=0.05, fc='red', ec='red')
ax.set_aspect('equal')
ax.legend()
ax.set_title("Eight-pathway Topology")
plt.savefig("figures/eight_pathways_topology.png")
plt.show()

# Fig. 4: Phase Plot
fig, ax = plt.subplots()
# Sample phase differences
runs = np.arange(500)
phases = 74 + np.random.randn(500) * 5  # Around 74°
ax.scatter(runs, phases, alpha=0.5)
ax.axhspan(72, 76, color='green', alpha=0.3, label='Stability Region')
ax.set_xlabel('Run Index')
ax.set_ylabel('Phase Difference (°)')
ax.legend()
ax.set_title("Phase-lock Stability Plot")
plt.savefig("figures/phase_lock_plot.png")
plt.show()
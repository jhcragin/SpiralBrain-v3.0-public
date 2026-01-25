import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Simulate recovery trajectories
time_steps = np.arange(0, 10, 1)
with_regulation = 0.2 + 0.8 * (1 - np.exp(-time_steps / 2))
with_regulation = np.clip(with_regulation, 0, 1)
without_regulation = 0.2 + 0.1 * time_steps
without_regulation = np.clip(without_regulation, 0, 1)

plt.figure(figsize=(8, 6))
plt.plot(time_steps, with_regulation, label='With Regulation', marker='o')
plt.plot(time_steps, without_regulation, label='Without Regulation', marker='x')
plt.xlabel('Time Steps Since Stress Onset')
plt.ylabel('Coherence Recovery Metric')
plt.title('Recovery Trajectories With vs. Without Regulation')
plt.legend()
plt.grid(True)
plt.savefig('../figures/fig2_recovery_trajectories.png')
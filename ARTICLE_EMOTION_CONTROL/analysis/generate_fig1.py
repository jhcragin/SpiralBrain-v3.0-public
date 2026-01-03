import yaml
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Load data from emotional logs
data_dir = Path('../data/emotional_logs')
coherences = []
sec_drifts = []

for file in data_dir.glob('*.yaml'):
    with open(file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if 'interventions' in data:
            for intervention in data['interventions']:
                pre_coherence = intervention['pre_state']['rhacc']['coherence']
                post_coherence = intervention['post_state']['rhacc']['coherence']
                pre_arousal = intervention['pre_state']['sec_vector']['arousal']
                post_arousal = intervention['post_state']['sec_vector']['arousal']
                sec_drift = abs(post_arousal - pre_arousal)
                coherences.append(post_coherence)
                sec_drifts.append(sec_drift)

# Figure 1: Coherence Collapse vs. SEC Drift
plt.figure(figsize=(8, 6))
plt.scatter(sec_drifts, coherences, alpha=0.7)
plt.xlabel('SEC Drift (Arousal Change)')
plt.ylabel('Symbolic Coherence Metric')
plt.title('Coherence Collapse vs. SEC Drift Under Stress')
plt.grid(True)
plt.savefig('../figures/fig1_coherence_vs_sec_drift.png')
#!/usr/bin/env python3
"""
Trajectory Visualization Script for SpiralBrain Cognitive Integrity Analysis

This script generates the flagship trajectory figure showing baseline → perturbation → recovery
dynamics under emotional overload, demonstrating regulatory endurance.
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_trajectory_data(filepath):
    """Load trajectory data from JSONL file."""
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line.strip()))
    return data

def extract_time_series(data):
    """Extract time series data for key metrics."""
    t_rel = [d['t_rel'] for d in data]
    coherence = [d['coherence'] for d in data]
    stability = [d['stability'] for d in data]
    hazard_pressure = [d['hazard_pressure'] for d in data]
    sec_drift = [d['sec_drift'] for d in data]

    return {
        'time': np.array(t_rel),
        'coherence': np.array(coherence),
        'stability': np.array(stability),
        'hazard_pressure': np.array(hazard_pressure),
        'sec_drift': np.array(sec_drift)
    }

def identify_phases(time_series):
    """Identify baseline, perturbation, and recovery phases."""
    sec_drift = time_series['sec_drift']

    # Find perturbation onset (first significant drift)
    perturbation_start = np.where(np.abs(sec_drift) > 0.05)[0]
    if len(perturbation_start) > 0:
        perturbation_idx = perturbation_start[0]
    else:
        perturbation_idx = len(sec_drift) // 3

    # Find recovery (return to low drift)
    recovery_idx = np.where(np.abs(sec_drift[perturbation_idx:]) < 0.02)[0]
    if len(recovery_idx) > 0:
        recovery_idx = perturbation_idx + recovery_idx[0]
    else:
        recovery_idx = int(len(sec_drift) * 0.8)

    return {
        'baseline_end': perturbation_idx,
        'perturbation_end': recovery_idx,
        'recovery_end': len(sec_drift)
    }

def create_trajectory_plot(time_series, phases, output_path):
    """Create the flagship trajectory visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('SpiralBrain Regulatory Trajectory: Emotional Overload Perturbation',
                 fontsize=14, fontweight='bold')

    time = time_series['time']

    # Phase backgrounds
    phase_colors = ['lightblue', 'lightcoral', 'lightgreen']
    phase_labels = ['Baseline', 'Perturbation', 'Recovery']

    for ax in axes.flat:
        for i, (start, end, color, label) in enumerate([
            (0, phases['baseline_end'], phase_colors[0], phase_labels[0]),
            (phases['baseline_end'], phases['perturbation_end'], phase_colors[1], phase_labels[1]),
            (phases['perturbation_end'], phases['recovery_end'], phase_colors[2], phase_labels[2])
        ]):
            ax.axvspan(time[start] if start < len(time) else time[-1],
                      time[min(end, len(time)-1)],
                      alpha=0.2, color=color, label=label if i == 0 else "")

    # Plot 1: Coherence and Stability
    ax1 = axes[0, 0]
    ax1.plot(time, time_series['coherence'], 'b-', label='Coherence', linewidth=2)
    ax1.plot(time, time_series['stability'], 'g-', label='Stability', linewidth=2)
    ax1.set_ylabel('Regulatory Metrics')
    ax1.set_title('Coherence & Stability')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: SEC Drift
    ax2 = axes[0, 1]
    ax2.plot(time, time_series['sec_drift'], 'r-', linewidth=2)
    ax2.set_ylabel('SEC Drift')
    ax2.set_title('Emotional Drift Magnitude')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='k', linestyle='--', alpha=0.5)

    # Plot 3: Hazard Pressure
    ax3 = axes[1, 0]
    ax3.plot(time, time_series['hazard_pressure'], 'orange', linewidth=2)
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Hazard Pressure')
    ax3.set_title('Regulatory Pressure')
    ax3.grid(True, alpha=0.3)

    # Plot 4: Combined view (smaller metrics)
    ax4 = axes[1, 1]
    ax4.plot(time, time_series['coherence'], 'b-', alpha=0.7, label='Coherence')
    ax4.plot(time, time_series['stability'], 'g-', alpha=0.7, label='Stability')
    ax4.plot(time, np.abs(time_series['sec_drift']), 'r-', alpha=0.7, label='|SEC Drift|')
    ax4.set_xlabel('Time (s)')
    ax4.set_ylabel('Normalized Metrics')
    ax4.set_title('Integrated Regulatory Response')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Trajectory plot saved to: {output_path}")

def main():
    # File paths
    data_file = Path('c:/Users/johnc/source/repos/SpiralBrain-v3.0-public/results/brain_trace.jsonl')
    output_file = Path('c:/Users/johnc/source/repos/SpiralBrain-v3.0-public/publication_package/figures/cognitive_trajectory_emotional_overload.png')
    
    print(f"Data file: {data_file}")
    print(f"Data file exists: {data_file.exists()}")

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Load and process data
    print("Loading trajectory data...")
    data = load_trajectory_data(data_file)
    time_series = extract_time_series(data)

    print(f"Loaded {len(data)} data points")
    print(f"Duration: {time_series['time'][-1]:.3f} seconds")
    # Identify phases
    phases = identify_phases(time_series)
    print(f"Phases identified: Baseline (0-{phases['baseline_end']}), "
          f"Perturbation ({phases['baseline_end']}-{phases['perturbation_end']}), "
          f"Recovery ({phases['perturbation_end']}-{phases['recovery_end']})")

    # Create plot
    print("Generating trajectory visualization...")
    create_trajectory_plot(time_series, phases, output_file)

    print("Trajectory analysis complete!")

if __name__ == '__main__':
    main()
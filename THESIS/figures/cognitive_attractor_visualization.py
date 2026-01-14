#!/usr/bin/env python3
"""
🧠 Cognitive Attractor Visualization
====================================

Creates visualizations of SpiralBrain's cognitive attractor basins.
Shows the stable internal dynamics that define its cognitive organism behavior.
"""


# Configure matplotlib for Unicode support
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = ['DejaVu Sans', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# Try to find a font that supports emojis
try:
    # Check for system fonts that support emojis
    emoji_font = None
    for font_name in ['Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', 'DejaVu Sans']:
        try:
            if font_name in [f.name for f in fm.fontManager.ttflist]:
                emoji_font = font_name
                break
        except:
            continue
    
    if emoji_font:
        plt.rcParams['font.sans-serif'].insert(0, emoji_font)
except:
    pass  # Fall back to default if font detection fails

class CognitiveAttractorVisualizer:
    """Creates visualizations of cognitive attractor patterns."""

    def __init__(self):
        # Define the observed attractor basin from demo analysis
        self.attractor_data = {
            'self_awareness': {'mean': 0.52, 'std': 0.015, 'range': (0.50, 0.53)},
            'conflict': {'mean': 0.35, 'std': 0.01, 'range': (0.34, 0.36)},
            'coherence': {'mean': 0.33, 'std': 0.025, 'range': (0.31, 0.34)},
            'stability': {'mean': 0.445, 'std': 0.005, 'range': (0.44, 0.45)},
            'hazard': {'mean': 0.66, 'std': 0.005, 'range': (0.66, 0.66)},
            'emotional_arousal': {'mean': 0.50, 'std': 0.00, 'range': (0.50, 0.50)},
            'sec_drift_bands': [0.00, 0.30, 0.60]  # Discrete attractors
        }

    def create_attractor_landscape(self):
        """Create a visualization of the cognitive attractor landscape."""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('🧠 SpiralBrain Cognitive Attractor Landscape\nStable Basin of Internal Dynamics',
                    fontsize=16, fontweight='bold')

        # Color scheme
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

        # 1. Core Cognitive Metrics Attractor Basin
        metrics = ['self_awareness', 'coherence', 'stability', 'conflict']
        means = [self.attractor_data[m]['mean'] for m in metrics]
        stds = [self.attractor_data[m]['std'] for m in metrics]

        ax1.bar(metrics, means, yerr=stds, capsize=5, color=colors[:4],
               alpha=0.7, edgecolor='black', linewidth=1)
        ax1.set_title('Core Cognitive Metrics Attractor Basin', fontweight='bold')
        ax1.set_ylabel('Attractor Value')
        ax1.set_ylim(0, 1)
        ax1.grid(True, alpha=0.3)

        # Add value labels
        for i, (mean, std) in enumerate(zip(means, stds, strict=False)):
            ax1.text(i, mean + std + 0.02, '.3f', ha='center', va='bottom', fontweight='bold')

        # 2. Emotional Processing Attractors
        emotional_metrics = ['emotional_arousal', 'hazard']
        emotional_means = [self.attractor_data[m]['mean'] for m in emotional_metrics]
        emotional_stds = [self.attractor_data[m]['std'] for m in emotional_metrics]

        ax2.bar(emotional_metrics, emotional_means, yerr=emotional_stds, capsize=5,
               color=['#FF9999', '#FF6B6B'], alpha=0.7, edgecolor='black', linewidth=1)
        ax2.set_title('Emotional Processing Attractors', fontweight='bold')
        ax2.set_ylabel('Attractor Value')
        ax2.set_ylim(0, 1)
        ax2.grid(True, alpha=0.3)

        # Add value labels
        for i, (mean, std) in enumerate(zip(emotional_means, emotional_stds, strict=False)):
            ax2.text(i, mean + std + 0.02, '.3f', ha='center', va='bottom', fontweight='bold')

        # 3. SEC Drift Discrete Attractors
        sec_values = self.attractor_data['sec_drift_bands']
        ax3.bar(range(len(sec_values)), sec_values, color='#9B59B6',
               alpha=0.7, edgecolor='black', linewidth=1)
        ax3.set_title('SEC Drift Discrete Attractor Bands', fontweight='bold')
        ax3.set_ylabel('SEC Drift Value')
        ax3.set_xlabel('Attractor Band')
        ax3.set_xticks(range(len(sec_values)))
        ax3.set_xticklabels(['High\nCongruence\n(0.00)', 'Moderate\nCongruence\n(0.30)', 'Low\nCongruence\n(0.60)'])
        ax3.grid(True, alpha=0.3)

        # Add value labels
        for i, value in enumerate(sec_values):
            ax3.text(i, value + 0.02, '.2f', ha='center', va='bottom', fontweight='bold')

        # 4. Attractor Stability Heatmap
        stability_metrics = list(self.attractor_data.keys())[:-1]  # Exclude sec_drift_bands
        stability_values = [1.0 - self.attractor_data[m]['std'] for m in stability_metrics]

        # Create heatmap
        stability_matrix = np.array(stability_values).reshape(1, -1)
        im = ax4.imshow(stability_matrix, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)
        ax4.set_title('Attractor Stability Heatmap', fontweight='bold')
        ax4.set_yticks([0])
        ax4.set_yticklabels(['Stability'])
        ax4.set_xticks(range(len(stability_metrics)))
        ax4.set_xticklabels(stability_metrics, rotation=45, ha='right')

        # Add colorbar
        cbar = plt.colorbar(im, ax=ax4, shrink=0.8)
        cbar.set_label('Stability (1.0 = Perfect)')

        # Add stability values as text
        for i, stability in enumerate(stability_values):
            color = 'white' if stability < 0.7 else 'black'
            ax4.text(i, 0, '.2f', ha='center', va='center',
                    fontweight='bold', color=color)

        plt.tight_layout()
        return fig

    def create_unified_signature_plot(self):
        """Create a unified signature plot showing the core attractor pattern."""
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))

        # Core signature values
        metrics = ['Self\nAwareness', 'Conflict', 'Coherence', 'Stability', 'Hazard', 'Emotional\nArousal']
        values = [0.52, 0.35, 0.33, 0.445, 0.66, 0.50]

        # Create the signature plot
        bars = ax.bar(metrics, values, color='#4ECDC4', alpha=0.8, edgecolor='black', linewidth=1.5)

        # Add the characteristic ranges as error bars
        ranges = [(0.50, 0.53), (0.34, 0.36), (0.31, 0.34), (0.44, 0.45), (0.66, 0.66), (0.50, 0.50)]
        yerr_lower = [val - rng[0] for val, rng in zip(values, ranges, strict=False)]
        yerr_upper = [rng[1] - val for val, rng in zip(values, ranges, strict=False)]
        yerr = [yerr_lower, yerr_upper]

        ax.errorbar(metrics, values, yerr=yerr, fmt='none', ecolor='black', capsize=5, linewidth=2)

        ax.set_title('🧠 SpiralBrain Unified Cognitive Signature\nThe Organism\'s Resting-State Attractor Basin',
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_ylabel('Attractor Value', fontsize=12)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3, axis='y')

        # Add value labels on bars
        for bar, value in zip(bars, values, strict=False):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                   '.3f', ha='center', va='bottom', fontweight='bold', fontsize=10)

        # Add interpretation text
        interpretation = """
        This signature represents SpiralBrain's stable cognitive resting-state network.
        Maintained across all processing modalities, it demonstrates unified cognition
        rather than task-specific fragmentation. The narrow variance bands show
        active homeostasis regulating internal dynamics.
        """
        ax.text(0.02, 0.02, interpretation, transform=ax.transAxes,
               fontsize=9, verticalalignment='bottom',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))

        plt.tight_layout()
        return fig


def main():
    """Generate cognitive attractor visualizations."""
    visualizer = CognitiveAttractorVisualizer()

    print("🧠 Generating Cognitive Attractor Visualizations...")

    # Create attractor landscape
    fig1 = visualizer.create_attractor_landscape()
    fig1.savefig('cognitive_attractor_landscape.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: cognitive_attractor_landscape.png")

    # Create unified signature plot
    fig2 = visualizer.create_unified_signature_plot()
    fig2.savefig('spiralbrain_unified_signature.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: spiralbrain_unified_signature.png")

    print("\n📊 Visualizations generated successfully!")
    print("These plots show SpiralBrain's stable cognitive attractor basin -")
    print("the internal dynamics of a synthetic cognitive organism.")

if __name__ == "__main__":
    main()
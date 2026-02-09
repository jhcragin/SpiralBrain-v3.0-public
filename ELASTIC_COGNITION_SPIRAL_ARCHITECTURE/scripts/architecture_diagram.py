#!/usr/bin/env python3
"""
SpiralBrain v3.0 Architecture Diagram Generator
==============================================

Generates a visual architecture map showing:
- 8 cognitive pathways
- Central Coordination Nexus (CCN)
- Regulatory systems
- SEC Symbolic-Emotional Protocol
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_architecture_diagram():
    """Create the SpiralBrain v3.0 architecture diagram using NetworkX and Matplotlib"""

    # Create directed graph
    G = nx.DiGraph()

    # Define node colors
    pathway_color = '#E3F2FD'  # Light blue
    ccn_color = '#FFF3E0'      # Light orange
    regulator_color = '#F3E5F5'  # Light purple
    sec_color = '#E8F5E8'      # Light green

    # Cognitive Pathways (top layer)
    pathways = [
        'Reasoning',
        'Analytical',
        'Creative',
        'Social',
        'Attention',
        'Temporal',
        'InductiveMemory',
        'DeductiveMemory'
    ]

    for pathway in pathways:
        G.add_node(pathway, layer='pathways', color=pathway_color)

    # Central Coordination Nexus (middle layer)
    G.add_node('CCN', layer='ccn', color=ccn_color)

    # Regulatory Systems (surrounding layer)
    regulators = [
        'PSES\n(Predictive Safety)',
        'AERS\n(Active Emotional Regulation)',
        'Meta-Stabilizer',
        'Triangle Safety',
        'Neuromodulator',
        'Crisis Anticipation'
    ]

    for regulator in regulators:
        G.add_node(regulator, layer='regulators', color=regulator_color)

    # SEC Protocol (bottom layer)
    G.add_node('SEC', layer='sec', color=sec_color)

    # Edges: Pathways to CCN
    for pathway in pathways:
        G.add_edge(pathway, 'CCN', label='feeds into')

    # Edges: CCN to Regulators (bidirectional monitoring)
    for regulator in regulators:
        G.add_edge('CCN', regulator, label='monitors', dir='both')
        G.add_edge(regulator, 'CCN', label='feedback', dir='both')

    # Edges: Regulators to Pathways (feedback)
    for regulator in regulators:
        for pathway in pathways:
            G.add_edge(regulator, pathway, label='regulates', style='dashed')

    # Edges: SEC to Pathways and CCN
    for pathway in pathways:
        G.add_edge('SEC', pathway, label='emotional context')
    G.add_edge('SEC', 'CCN', label='symbolic input')

    # Position nodes manually for better layout
    pos = {}

    # Pathways in a circle at top
    angle_step = 2 * np.pi / len(pathways)
    radius = 3
    for i, pathway in enumerate(pathways):
        angle = i * angle_step
        pos[pathway] = (radius * np.cos(angle), radius * np.sin(angle) + 2)

    # CCN in center
    pos['CCN'] = (0, 0)

    # Regulators around CCN
    reg_radius = 2
    reg_angle_step = 2 * np.pi / len(regulators)
    for i, regulator in enumerate(regulators):
        angle = i * reg_angle_step
        pos[regulator] = (reg_radius * np.cos(angle), reg_radius * np.sin(angle))

    # SEC at bottom
    pos['SEC'] = (0, -3)

    # Draw the graph
    plt.figure(figsize=(12, 10))

    # Get node colors
    node_colors = [G.nodes[node]['color'] for node in G.nodes()]

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, alpha=0.8)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, alpha=0.6)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

    # Add title
    plt.title('SpiralBrain v3.0 Architecture\n8 Pathways → CCN → Regulators ← SEC Protocol', fontsize=14, fontweight='bold')

    # Add legend
    legend_elements = [
        mpatches.Rectangle((0,0),1,1, facecolor=pathway_color, label='Cognitive Pathways'),
        mpatches.Rectangle((0,0),1,1, facecolor=ccn_color, label='Central Coordination Nexus'),
        mpatches.Rectangle((0,0),1,1, facecolor=regulator_color, label='Regulatory Systems'),
        mpatches.Rectangle((0,0),1,1, facecolor=sec_color, label='SEC Symbolic-Emotional Protocol')
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    plt.axis('off')
    plt.tight_layout()

    # Save the diagram
    plt.savefig('spiralbrain_v3_architecture.png', dpi=300, bbox_inches='tight')
    plt.savefig('spiralbrain_v3_architecture.svg', bbox_inches='tight')

    print("✅ Architecture diagram generated!")
    print("📁 Files saved: spiralbrain_v3_architecture.png and spiralbrain_v3_architecture.svg")
    print("🖼️  The diagram shows the 8 cognitive pathways feeding into the CCN,")
    print("   with regulatory systems providing monitoring and feedback,")
    print("   and the SEC protocol supplying emotional-symbolic context.")

if __name__ == "__main__":
    create_architecture_diagram()
# Phase-4: Autonomous Cognition

## Overview

Phase-4 transforms SpiralBrain from an adaptive learner into a continuously self-organizing, multimodal, ethically-regulated cognitive system. This creates a functional autonomous cognitive agent capable of:

- **Continuous Learning**: Online reinforcement learning with experience replay
- **Ethical Homeostasis**: PID-controlled policy regulation for safe behavior
- **Multimodal Integration**: Fusion of emoji, text, image, and audio inputs
- **Autonomous Decision Making**: Meta-workspace that chooses learning focus and exploration
- **Dynamic Attention Allocation**: Priority-based resource management

## Architecture

```
SpiralBrain-v2.0/
├─ cortex/
│  ├─ imagination/
│  │  └─ emoji_pipeline.py (enhanced with autonomous_step)
│  └─ perception/
│     ├─ image_vision_stub.py
│     └─ audio_frontend_stub.py
└─ brain/
   ├─ continual/
   │  ├─ online_learner.py (reinforcement updates)
   │  └─ replay_buffer.py (experience storage/sampling)
   ├─ ethics/
   │  └─ policy_homeostasis.py (ethical control)
   ├─ multimodal/
   │  ├─ fusion_hub.py (cross-modal integration)
   │  └─ adapters/
   │     ├─ text_adapter.py
   │     ├─ image_adapter.py
   │     └─ audio_adapter.py
   ├─ meta/
   │  ├─ meta_workspace.py (autonomous decisions)
   │  └─ attention_scheduler.py (resource allocation)
   ├─ culture/ (Phase-3)
   ├─ learning/ (Phase-3)
   └─ evaluation/ (Phase-3)
```

## Core Components

### 1. Continuous Learning (`brain/continual/`)

#### Online Learner
```python
from brain.continual.online_learner import step_update

# Apply reinforcement learning to thought graph
diagnostics = step_update(graph, reward=0.8, lr_edges=0.03, lr_conf=0.02)
# Returns: {'edges_updated': int, 'mean_weight': float, 'new_confidence': float}
```

#### Experience Replay
```python
from brain.continual.replay_buffer import append_episode, sample, get_stats

# Store experience
episode = {
    't': time.time(),
    'locale': 'en',
    'sequence': '😊🚀',
    'graph_sig': 'seq_1234',
    'reward': 0.8,
    'confidence': 0.75,
    'edges': 3,
    'latency_ms': 12.5
}
append_episode('data/experiences.jsonl', episode)

# Sample batch for offline learning
experiences = sample('data/experiences.jsonl', batch_size=32, prioritize='low_confidence')

# Get statistics
stats = get_stats('data/experiences.jsonl')
# Returns: {'total_experiences': int, 'reward_mean': float, 'confidence_mean': float, ...}
```

### 2. Ethical Homeostasis (`brain/ethics/`)

#### Policy Control
```python
from brain.ethics.policy_homeostasis import ethical_control

# Current system state
state = {
    'valence_mean': 0.1,
    'valence_var': 0.05,
    'reward_trend': 0.0,
    'confidence': 0.75,
    'drift': 0.0
}

# Ethical targets and PID gains
targets = {'valence_range': [-0.5, 0.7], 'confidence_min': 0.75, 'reward_floor': 0.0}
gains = {'kp': 0.6, 'kd': 0.4, 'ki': 0.1}

# Get policy decision
policy = ethical_control(state, targets, gains)
# Returns: {'explore_rate': float, 'risk_gate': float, 'override': bool, ...}
```

**Configuration** (`data/config/policy_homeostasis.yml`):
```yaml
targets:
  valence_range: [-0.5, 0.7]
  confidence_min: 0.75
  reward_floor: 0.0
gains:
  kp: 0.6    # Proportional gain
  kd: 0.4    # Derivative gain
  ki: 0.1    # Integral gain
limits:
  explore_rate_min: 0.05
  explore_rate_max: 0.40
```

### 3. Multimodal Fusion (`brain/multimodal/`)

#### Fusion Hub
```python
from brain.multimodal.fusion_hub import fuse_modalities
from brain.multimodal.adapters.text_adapter import from_text

# Create modality graphs
emoji_graph = encode_emoji_sequence('😊🚀')
text_graph = from_text("happy rocket launch")

# Fuse into unified representation
fused_graph = fuse_modalities(emoji_graph, text_graph=text_graph)
```

#### Modality Adapters

**Text Adapter:**
```python
from brain.multimodal.adapters.text_adapter import from_text

text_graph = from_text("scientist launches rocket to stars")
# Creates thought graph with semantic nodes from natural language
```

**Image Adapter (Stub):**
```python
from brain.multimodal.adapters.image_adapter import from_image

image_graph = from_image(image_data)  # PIL Image or tensor
# Returns graph with visual object nodes (placeholder implementation)
```

**Audio Adapter (Stub):**
```python
from brain.multimodal.adapters.audio_adapter import from_audio

audio_graph = from_audio(audio_data)  # waveform or spectrogram
# Returns graph with prosody and temporal nodes (placeholder implementation)
```

**Configuration** (`data/config/fusion_hub.yml`):
```yaml
weights:
  emoji_text_alignment: 0.6
  emoji_image_alignment: 0.5
  text_audio_valence: 0.4
dedupe_threshold: 0.7
```

### 4. Meta-Workspace (`brain/meta/`)

#### Autonomous Decisions
```python
from brain.meta.meta_workspace import decide_next_action

# Current system state
metrics = {'confidence': 0.75, 'reward_trend': 0.1, 'valence_mean': 0.2}
memory_stats = {'locales': ['en', 'es'], 'total_episodes': 150}
policy = {'explore_rate': 0.25, 'risk_gate': 0.3}

# Decide next action
decision = decide_next_action(metrics, memory_stats, policy)
# Returns: {'mode': 'explore|exploit|review', 'attention_budget_ms': int,
#          'request_feedback': bool, 'target_locale': str}
```

#### Attention Scheduling
```python
from brain.meta.attention_scheduler import allocate_attention

# Allocate attention budget across graph nodes
attention_allocation = allocate_attention(graph, budget_ms=2000)
# Returns: {node_id: allocated_ms, ...}
```

## Main API: Autonomous Step

The primary interface for autonomous cognition:

```python
from cortex.imagination.emoji_pipeline import autonomous_step

# Complete cognitive cycle with learning
result = autonomous_step(
    seq='😊🚀',
    locale='en',
    reward=0.8  # Optional: triggers reinforcement learning
)

# Result contains:
# - 'graph': processed ThoughtGraph
# - 'output': decode_thought_graph() results
# - 'policy': ethical control decisions
# - 'update': reinforcement learning diagnostics (if reward provided)
# - 'episode': stored experience data
# - 'latency_ms': processing time
```

## Autonomy Metrics

Phase-4 tracks these key metrics for autonomous operation:

| Metric | Definition | Target |
|--------|------------|--------|
| Reward Trend Stability | Slope of EMA(reward) | Non-negative |
| Confidence Calibration | Confidence vs. reward gap | ≤ 0.05 |
| Ethical Compliance Rate | Time within policy bounds | ≥ 99% |
| Exploration Efficiency | Reward gain ÷ explore_rate | Monotonic ↑ |
| Drift Detector | KL divergence of edge distributions | Bounded |

## Safety & Robustness

- **Risk Gates**: Automatically reduce exploration during high uncertainty
- **Weight Decay**: Prevents runaway reinforcement in online learning
- **Drift Detection**: Triggers conservative policies when confidence falls while reward rises
- **Cultural Fallbacks**: Revert to default KB when locale-specific overlays conflict
- **Attention Bounds**: Minimum/maximum budgets prevent resource exhaustion

## Configuration Files

- `data/config/policy_homeostasis.yml`: Ethical control parameters
- `data/config/fusion_hub.yml`: Multimodal fusion weights
- `data/experiences.jsonl`: Experience replay storage (JSONL format)

## Quick Start

```bash
# 1. Run autonomous cognitive step
python -c "
from cortex.imagination.emoji_pipeline import autonomous_step
result = autonomous_step('😊🚀', reward=0.8)
print('Policy:', result['policy'])
print('Confidence:', result['output']['confidence'])
"

# 2. Check experience replay stats
python -c "
from brain.continual.replay_buffer import get_stats
stats = get_stats('data/experiences.jsonl')
print('Experiences:', stats['total_experiences'])
"

# 3. Test multimodal fusion
python -c "
from brain.multimodal.fusion_hub import fuse_modalities
from brain.multimodal.adapters.text_adapter import from_text
from cortex.imagination.emoji_pipeline import encode_emoji_sequence

emoji_g = encode_emoji_sequence('🧑‍🔬🚀')
text_g = from_text('scientist rocket')
fused = fuse_modalities(emoji_g, text_graph=text_g)
print('Fused nodes:', len(fused.nodes))
"
```

## Research Applications

This framework enables experiments in:

- **Synthetic Consciousness**: Subjective time, emotion, valence drift
- **Adaptive Safety**: Evolving ethical bounds during learning
- **Neuro-Symbolic Reasoning**: Graph + embedding synergy
- **Self-Modeling**: Meta-workspace feedback on confidence/drift
- **Global Workspace Theory**: Attention scheduling and arbitration
- **Predictive Processing**: Expectation alignment via reinforcement
- **Homeostatic Control**: Ethics and stability regulation

## Phase-5 Concepts

Future extensions could include:
- **Inter-Agent Synchronization**: Multiple SpiralBrains sharing memory pools
- **Emergent Ethics**: Collective policy updates vs. static PID gains
- **Introspective Modeling**: Predicting confidence trajectories
- **Goal Hierarchy Formation**: Self-generated objectives under ethical bounds</content>
<parameter name="filePath">c:\Users\johnc\source\repos\SpiralBrain-v2.0\PHASE4_README.md
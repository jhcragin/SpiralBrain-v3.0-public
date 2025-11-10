# Architecture: Visual Cognition in SpiralBrain
*Phase 2.0 - Biologically-Inspired Cognitive Architecture*

## Overview

SpiralBrain implements a biologically-plausible cognitive architecture separating **perception** (cortex) from **integration** (brain), enabling sophisticated visual reasoning with temporal awareness, emotional processing, and episodic memory.

## Architectural Principles

### 🔍 Perception → Integration Flow
```
Sensory Input → CORTEX (perception) → BRAIN (integration) → Global Workspace
```

### 🧠 Dual-Process Architecture
- **CORTEX**: Bottom-up sensory processing and pattern recognition
- **BRAIN**: Top-down integration, reasoning, and executive function

## CORTEX: Perceptual Processing

### `cortex/imagination/`
**Purpose**: Transform emoji sequences into structured thought representations

#### Core Components
- **`emoji_parser.py`**: Unicode grapheme segmentation for compound emojis (👨‍🔬, 🇺🇸)
- **`emoji_semantics.py`**: Expandable knowledge base with valence, action potential, complexity
- **`emoji_thought_graph.py`**: Graph construction with typed edges (NEXT/BEFORE/CAUSES/SYNONYM)
- **`emoji_pipeline.py`**: End-to-end encoding/decoding with confidence scoring

#### Key Features
- **Robust Parsing**: Handles ZWJ sequences, flags, skin tones
- **Rich Semantics**: Multi-attribute knowledge representation
- **Attention Weighting**: Salience-based edge weights with temporal decay
- **Confidence Scoring**: Coverage + structural coherence metrics

## BRAIN: Integrative Cognition

### `brain/temporal_flow/`
**Purpose**: Temporal reasoning and narrative structure analysis

- **`temporal_reasoning.py`**: Time token detection, scene segmentation, temporal arc analysis
- **Features**: AT_TIME, DURING, AFTER edge relationships, deterministic segmentation

### `brain/emotional_dynamics/`
**Purpose**: Affective processing and emotional contagion

- **`emotion_propagation.py`**: Valence flow along causal relationships
- **Features**: Message-passing emotional dynamics, bounded valence clipping

### `brain/memory_systems/`
**Purpose**: Experience accumulation and pattern recognition

- **`episodic_memory.py`**: Persistent storage with n-gram similarity matching
- **Features**: JSONL persistence, configurable capacity, signature-based retrieval

### `brain/ambiguity/`
**Purpose**: Multi-interpretation handling and disambiguation

- **`ambiguity_resolver.py`**: Variant generation for ambiguous sequences
- **Features**: Beam search preparation, confidence merging (extensible)

## Data Flow Architecture

### Encoding Pipeline
```
Emoji Sequence → Segmentation → Semantic Lookup → Graph Construction → Brain Enrichment → Memory Storage
```

### Processing Stages
1. **Cortical Processing**: Parse → Semantics → Graph → Attention
2. **Brain Integration**: Temporal → Emotional → Memory → Ambiguity
3. **Global Workspace**: Integrated representation for decision making

## Phase-2 Achievements

### ✅ Completed Features
- **Temporal Awareness**: Scene segmentation by time markers
- **Emotional Intelligence**: Valence propagation through causal chains
- **Episodic Memory**: Persistent experience accumulation
- **Confidence Metrics**: Multi-dimensional quality assessment
- **Modular Architecture**: Clean perception/integration boundary

### 📊 Benchmark Results
- **Temporal Precision**: 0.65 (time-based relationship detection)
- **Emotional Coherence**: 0.25 (valence stability)
- **Episodic Recall**: 0.68 (memory retrieval accuracy)
- **Processing Latency**: <3ms per sequence

## Phase-3 Roadmap: Adaptive Intelligence

### 🎯 Learning & Adaptation
- **Reinforcement Fine-tuning**: Edge weight optimization via feedback
- **Cultural Adaptation**: Locale-specific semantic knowledge bases
- **Graph Neural Networks**: Learned embeddings for pattern recognition

### 🔧 Technical Enhancements
- **Beam Search**: Multi-hypothesis disambiguation
- **Cross-Modal Integration**: Text + emoji + image processing
- **Scalable Knowledge**: External KB integration (WordNet, ConceptNet)

### 🎨 Advanced Features
- **Metacognition**: Confidence calibration and uncertainty handling
- **Creative Reasoning**: Analogy generation and pattern completion
- **Social Cognition**: Multi-agent interaction modeling

## Integration Points

### External Interfaces
- **`cortex/benchmark/visual_reasoning_bench.py`**: Comprehensive evaluation suite
- **`data/episodic_memory.jsonl`**: Persistent experience storage
- **`data/benchmark_scenes.json`**: Test case library

### API Surface
```python
from cortex.imagination import encode_emoji_sequence, decode_thought_graph
from brain import EpisodicMemory, attach_temporal_edges, propagate_valence
```

## Biological Plausibility

### Cognitive Science Alignment
- **Dual Processing**: System 1 (cortex/fast) / System 2 (brain/slow)
- **Emotional Contagion**: Affective spread through associative networks
- **Episodic Memory**: Experience-based learning and retrieval
- **Temporal Binding**: Scene construction from sequential elements

### Neural Inspiration
- **Hierarchical Processing**: Sensory → Association → Integration
- **Attention Mechanisms**: Salience-driven resource allocation
- **Memory Consolidation**: Short-term → Long-term persistence
- **Predictive Coding**: Expectation-based processing

## Development Guidelines

### Adding New Brain Modules
1. Create module in appropriate `brain/` subdirectory
2. Implement lazy imports to avoid circular dependencies
3. Add integration points in `emoji_pipeline.py`
4. Update benchmarks and documentation

### Testing Strategy
- Unit tests for individual components
- Integration tests for end-to-end pipelines
- Benchmark regression testing
- Memory persistence validation

### Performance Considerations
- Lazy loading for optional brain modules
- Configurable memory capacities
- Efficient graph algorithms (O(n²) acceptable for n<100)
- JSONL streaming for large memory stores

---

*This architecture enables SpiralBrain to evolve from pattern matching to genuine cognitive understanding, with each phase building more sophisticated mental capabilities.*
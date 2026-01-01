# SpiralBrain v3.0 - Public Repository

This repository contains the public materials for SpiralBrain v3.0, corresponding to the manuscript "Measuring Cognitive Integrity Under Uncertainty: A Non-Learning Synthetic Architecture".

## Overview

SpiralBrain v3.0 implements a non-learning cognitive architecture designed to preserve internal cognitive integrity under uncertainty. This public repository provides the complete publication package, reproducibility scripts, and essential data for the reported experiments.

## Learning Model Definition

SpiralBrain v3.0 is a **non-learning cognitive architecture**. For a precise operational definition of what "learning" means (and does not mean) in SpiralBrain, including explicit boundaries and exclusions, see [`docs/SPIRALBRAIN_LEARNING_MODEL.md`](docs/SPIRALBRAIN_LEARNING_MODEL.md).

This document provides the normative definition referenced in the manuscript and prevents misinterpretation of SpiralBrain's regulatory mechanisms as traditional AI learning.

## Repository Contents

This public repository contains:

- **`publication_package/`**: Complete journal submission materials including manuscript, figures, metadata, and cover letter
- **`scripts/`**: Reproducibility scripts for figure generation and analysis
- **`results/`**: Essential experimental data, trajectory measurements, and correspondence validation benchmarks
- **`docs/`**: Formal definitions, learning model boundaries, cognitive integrity research paper, adaptation paper, emotional foundation paper, and full scientific paper

## Key Features

- Four-lobe cognitive architecture (Cortex, Codex, Nexus, Sensus)
- Reflective homeostasis for internal coherence monitoring
- Elastic coupling dynamics with spiral coherence manifolds
- Emotional-symbolic calibration (SEC) layers
- Non-learning regulatory mechanisms

## Reproducibility

The repository is structured for complete reproducibility of the manuscript's findings.

**Dependencies:** numpy, matplotlib, scipy, seaborn

**To regenerate publication figures:**
```bash
python scripts/generate_publication_figures.py
```

**Publication Package:** The [`publication_package/`](publication_package/) directory contains the complete manuscript, all figures, and submission materials.

**Data:** Experimental results are in [`results/`](results/) with trajectory data in JSONL format. Correspondence validation benchmarks demonstrating regulatory integrity against established AI standards are available in [`results/cognitive_integrity_benchmarks.json`](results/cognitive_integrity_benchmarks.json), with all referenced experimental data files included for full reproducibility.

**Scripts:** Figure generation and analysis code is in [`scripts/`](scripts/). Note that some benchmark scripts (e.g., `run_emotional_benchmarks.py`, `core_emotional_foundation_benchmark.py`) are included for transparency but require the full SpiralBrain-v3.0 system to execute. The provided experimental results in [`results/`](results/) are pre-computed and can be tested by:

- Inspecting the JSON files directly to verify metrics against manuscript claims.
- Running `scripts/generate_publication_figures.py` to reproduce figures from the data.
- Analyzing trajectory data in JSONL format for custom validations using standard Python tools.

For full system execution and additional benchmarking, access to the complete SpiralBrain-v3.0 repository is required.

## Manuscript

The main manuscript is available at: [`publication_package/manuscript/spiralbrain_aij.tex`](publication_package/manuscript/spiralbrain_aij.tex)

## Full Research Papers

Additional research papers providing theoretical foundations, experimental validation, and regulatory compliance definitions are available in [`docs/`](docs/):

- [`docs/SPIRALBRAIN_COGNITIVE_INTEGRITY_PAPER.md`](docs/SPIRALBRAIN_COGNITIVE_INTEGRITY_PAPER.md): Detailed analysis of cognitive integrity, SEC validation, and regulatory learning.
- [`docs/SPIRALBRAIN_ADAPTATION_PAPER.md`](docs/SPIRALBRAIN_ADAPTATION_PAPER.md): Dynamical systems analysis, stability guarantees, and organic adaptation.
- [`docs/CORE_EMOTIONAL_FOUNDATION_SCIENTIFIC_PAPER.md`](docs/CORE_EMOTIONAL_FOUNDATION_SCIENTIFIC_PAPER.md): Emotion as a core computational substrate for cognition.
- [`docs/SPIRALBRAIN_V3_FULL_SCIENTIFIC_PAPER.md`](docs/SPIRALBRAIN_V3_FULL_SCIENTIFIC_PAPER.md): Unified architecture with metacognitive control and dynamical signatures.

## License

Apache 2.0 - See LICENSE file for details.

## Contact

For questions or research inquiries: john.cragin@outlook.com
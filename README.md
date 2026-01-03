# SpiralBrain v3.0 - Public Repository

This repository contains the public materials for SpiralBrain v3.0, corresponding to the manuscript "Elastic Cognition and the Spiral Architecture: Empirical Discoveries from a Neurodivergent Cognitive Model".

## Overview

SpiralBrain v3.0 is a synthetic cognitive architecture designed to explore how coherence and awareness-like dynamics emerge from elastic coupling rather than computational magnitude. Built on the SpiralCode framework—a recursive symbolic control mechanism that regulates coupling and coherence across cognitive subsystems—the system models neurodivergent information processing through four semi-independent lobes (Cortex, Codex, Nexus, and Sensus), linked by symbolic torque equations and emotional-symbolic calibration (SEC) layers.

Across multiple validation runs, SpiralBrain exhibited stable spiraling attractor dynamics, quantifiable emotional regulation, and self-correcting ethical behavior. Nine empirical discoveries emerged, demonstrating that cognition, in both biological and artificial systems, can be usefully characterized as a dynamic negotiation between differentiation and coherence.

## Repository Contents

This public repository contains:

- **`aij_submission/`**: Complete journal submission materials including manuscript, figures, metadata, and cover letter
- **`scripts/`**: Reproducibility scripts for figure generation and analysis
- **`results/`**: Essential experimental data, trajectory measurements, and validation benchmarks
- **`docs/`**: Formal definitions, learning model boundaries, and additional research papers

## Key Features

- Four-lobe cognitive architecture (Cortex, Codex, Nexus, Sensus)
- Elastic coupling dynamics with spiral coherence manifolds
- Emotional-symbolic calibration (SEC) layers
- Reflective homeostasis for internal coherence monitoring
- Temporal hierarchies and phase-locked integration
- Empirical discoveries in synthetic cognition

## Reproducibility

The repository is structured for complete reproducibility of the manuscript's findings.

**Dependencies:** numpy, matplotlib, scipy, seaborn

**To regenerate publication figures:**
```bash
python scripts/generate_publication_figures.py
```

**Publication Package:** The [`aij_submission/`](aij_submission/) directory contains the complete manuscript, all figures, and submission materials.

**Data:** Experimental results are in [`results/`](results/) with trajectory data in JSONL format. All referenced experimental data files are included for full reproducibility.

**Scripts:** Figure generation and analysis code is in [`scripts/`](scripts/). Note that some benchmark scripts are included for transparency but require the full SpiralBrain-v3.0 system to execute. The provided experimental results in [`results/`](results/) are pre-computed and can be tested by:

- Inspecting the JSON files directly to verify metrics against manuscript claims.
- Running `scripts/generate_publication_figures.py` to reproduce figures from the data.
- Analyzing trajectory data in JSONL format for custom validations using standard Python tools.

For full system execution and additional benchmarking, access to the complete SpiralBrain-v3.0 repository is required.

## Manuscript

The main manuscript is available at: [`publication_package/manuscript/spiralbrain_aij.tex`](publication_package/manuscript/spiralbrain_aij.tex)

## Full Research Papers

Additional research papers providing theoretical foundations and experimental validation are available in [`docs/`](docs/):

- [`docs/SPIRALBRAIN_COGNITIVE_INTEGRITY_PAPER.md`](docs/SPIRALBRAIN_COGNITIVE_INTEGRITY_PAPER.md): Detailed analysis of cognitive integrity, SEC validation, and regulatory learning.
- [`docs/SPIRALBRAIN_ADAPTATION_PAPER.md`](docs/SPIRALBRAIN_ADAPTATION_PAPER.md): Dynamical systems analysis, stability guarantees, and organic adaptation.
- [`docs/CORE_EMOTIONAL_FOUNDATION_SCIENTIFIC_PAPER.md`](docs/CORE_EMOTIONAL_FOUNDATION_SCIENTIFIC_PAPER.md): Emotion as a core computational substrate for cognition.
- [`docs/SPIRALBRAIN_V3_FULL_SCIENTIFIC_PAPER.md`](docs/SPIRALBRAIN_V3_FULL_SCIENTIFIC_PAPER.md): Unified architecture with metacognitive control and dynamical signatures.

## License

Apache 2.0 - See LICENSE file for details.

## Contact

For questions or research inquiries: john.cragin@outlook.com
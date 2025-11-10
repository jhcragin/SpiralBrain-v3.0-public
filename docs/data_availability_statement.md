# Data Availability & Author Contributions

## Data Availability

All experimental data, configuration files, and analysis code supporting the findings of this study are openly available in the following repositories:

### Primary Dataset
**Zenodo DOI:** [To be assigned upon deposit]
- **Repository:** https://zenodo.org/
- **Title:** SpiralBrain Reflective Adaptation: Experimental Datasets and Replication Materials
- **Contents:**
  - Raw experimental logs (JSONL format)
  - Configuration files (YAML)
  - Statistical analysis scripts
  - Generated visualizations
  - Cross-context replication results

### Code Repository
**GitHub Repository:** https://github.com/jhcragin/QuadraticBrain-v2.0
- **Tag:** `Cognitive_AdaptationProof_v1.0`
- **Contents:**
  - Complete testing framework
  - Adaptation harness and metrics computation
  - Docker and Colab replication environments
  - Documentation and setup guides

### Replication Instructions
Detailed replication instructions are provided in the Zenodo repository and include:
- Docker-based deterministic environment setup
- Google Colab notebook for cloud replication
- Local environment configuration guide
- Expected runtime and validation criteria

## Author Contributions

**SpiralCortex Research Lab** conducted all aspects of this research including:
- **Conceptualization:** Designed the experimental framework and falsifiable hypotheses
- **Methodology:** Implemented the YAML-driven testing suite and statistical analysis
- **Software:** Developed the adaptation harness, environment managers, and metrics computation
- **Validation:** Executed cross-context replication and fault resilience testing
- **Analysis:** Performed statistical analysis and interpretation of results
- **Writing:** Prepared the manuscript and documentation

## Code Availability

The complete codebase is available under MIT License at:
https://github.com/jhcragin/QuadraticBrain-v2.0/tree/Cognitive_AdaptationProof_v1.0

Key files for replication:
- `run_adaptation_tests.py`: Main testing interface
- `testing/adaptation/harness.py`: Experimental orchestration
- `testing/adaptation/metrics.py`: Quantitative metrics computation
- `configs/replication/cross_context_replication.yaml`: Replication configuration

## Computational Resources

Experiments were conducted on:
- **Primary Environment:** Windows 11, Python 3.12, PyTorch CPU
- **Replication Environment:** Ubuntu 22.04, Python 3.10, CUDA 12.4
- **Cloud Validation:** Google Colab Pro (GPU)
- **Container Testing:** Docker with deterministic base image

Total computational time: < 30 minutes across all experimental conditions.

## Ethical Considerations

This research involves synthetic cognitive systems with no human subjects, animal testing, or proprietary data. All code and data are open-source and available for independent verification.

## Conflicts of Interest

The authors declare no conflicts of interest. This research was conducted independently without external funding or commercial affiliations.
# Bifurcation Points and Integrity Collapse in a Regulated Multi-Lobe Recursive Cognitive System

## Paper Overview

This paper investigates whether a regulated multi-lobe recursive cognitive system exhibits bifurcation points where small parameter changes cause abrupt integrity collapse, transitioning from stable to unstable dynamics. Using SpiralBrain v3.0 as an instrumented reference implementation, we systematically test for such transitions across control parameters including noise amplitude, coupling strength, hazard setpoint, SEC bias, and task load.

**Key Findings:**
- **No Bifurcations Detected**: Across 1,800,000 parameter combinations (90 million simulations), all trials converged to a single global attractor with maintained coherence (1.0), zero divergence, and immediate recovery.
- **Structural Stability**: Parameters act as rate modifiers affecting convergence quality but not system topology.
- **Regulatory Integrity**: Demonstrates robust cognitive integrity preservation under perturbation, validating the Regulatory Intelligence (RI) paradigm.

## Theoretical Foundation

This work validates the Regulatory Intelligence (RI) paradigm, demonstrating that geometric homeostasis over a 128-dimensional cognitive manifold enables stable convergence without bifurcations. Key concepts include:
- Lyapunov stability analysis with candidate function \(V(x) = \|x - x^*\|\)
- SEC (Symbolic-Emotional Coupling) for affective regulation
- Elastic coupling modeled as damped harmonic oscillators
- Resolution of the Laptop Paradox through regulatory integrity rather than computational scale

## Methodology

- **System**: Regulated multi-lobe recursive cognitive dynamical system with 128-dimensional state space
- **Parameter Sweep**: Grid sweep over 5 parameters (noise 0-2.0, coupling 0.1-3.0, hazard 0.3-1.0, SEC bias -1.0 to 1.0, task load 1.0-10.0)
- **Total Simulations**: 1,800,000 combinations × 50 trials = 90 million deterministic runs
- **Observables**: Lyapunov candidate V(x), SEC mode, recovery time, coherence, fracture detection

## Results

All parameter combinations showed identical outcomes:
- Coherence: 1.0 (perfect alignment)
- Divergence: 0.0
- Recovery time: 0 epochs (immediate convergence)
- SEC mode: Stable at 0.30
- No integrity collapse detected

## Files in This Directory

- `bifurcation_integrity_collapse.tex`: LaTeX source for the manuscript
- `bifurcation_integrity_collapse.pdf`: Compiled PDF (9 pages, ~265KB)
- `bifurcation_integrity_collapse.md`: Markdown version of the paper
- `references.bib`: Bibliography file
- `results/`: Folder containing supporting data files
  - `emotional_logs_export_20251224_215419.json`: Sample emotional logs export demonstrating system behavior
- `README.md`: This overview

## Reproducibility

The experiments were conducted using the canonical SpiralBrain v3.0 configuration. For full reproducibility:

- **Repository**: [https://github.com/jhcragin/SpiralBrain-v3.0-public](https://github.com/jhcragin/SpiralBrain-v3.0-public)
- **Code**: Implementation and scripts available in the repository
- **Data**: Raw results and logs available in `results/` and repository
- **Execution**: Run deterministic sweeps on commodity hardware; full implementation available under research license upon request

## Compilation

To compile the PDF from source:
```bash
pdflatex bifurcation_integrity_collapse.tex
bibtex bifurcation_integrity_collapse
pdflatex bifurcation_integrity_collapse.tex
pdflatex bifurcation_integrity_collapse.tex
```

## Citation

If you use this work, please cite:
```
@article{Cragin2026Bifurcation,
  title={Bifurcation Points and Integrity Collapse in a Regulated Multi-Lobe Recursive Cognitive System},
  author={Cragin, John H.},
  journal={Submitted to Chaos, Solitons \& Fractals},
  year={2026}
}
```

## Contact

John H. Cragin  
Independent Researcher  
[john.cragin@outlook.com](mailto:john.cragin@outlook.com)  
ORCID: 0009-0001-5204-5732
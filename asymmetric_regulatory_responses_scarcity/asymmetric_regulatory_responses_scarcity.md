# Asymmetric Regulatory Responses Under Resource Scarcity in an Instrumented Cognitive System

**John H. Cragin**  
Independent Researcher  
john.cragin@outlook.com

*January 19, 2026*

Resource scarcity induces asymmetric regulatory responses in cognitive systems, where intervention strategies bifurcate between elastic adaptation and brittle collapse. Using SpiralBrain v3.0, an instrumented cognitive architecture running on commodity hardware, we demonstrate that under constrained resources, adaptive regulation maintains epistemic restraint while coercive approaches destabilize. Results show adaptive φ_max (30.10°) approximating observer baseline (31.99°), significantly better than regulator overshoot (47.75°), with identical scarcity costs ensuring fair comparison. This bifurcation reveals learned intervention intelligence, distinguishing beneficial restraint from iatrogenic harm. No claims of universality are made; findings are constrained to empirically observed behavior in SpiralBrain.

This work validates the Regulatory Intelligence (RI) paradigm [Cragin2026Thesis], demonstrating that geometric homeostasis enables learned intervention intelligence under scarcity, where elastic adaptation preserves stability while brittle approaches collapse.

## Introduction

Resource scarcity fundamentally alters decision-making in cognitive systems, potentially inducing asymmetric responses where different regulatory strategies yield divergent outcomes. Traditional approaches assume uniform degradation under pressure, but instrumented systems reveal bifurcation: some maintain stability through elastic adaptation, others collapse into brittle failure.

We investigate asymmetric regulatory responses under scarcity using SpiralBrain v3.0 [SpiralBrainRepo], focusing on intervention intelligence—the capacity for beneficial regulation without iatrogenic harm. Under identical scarcity regimes, adaptive regulation maintains restraint when abstention carries cost, while coercive approaches destabilize.

Results demonstrate clear bifurcation: adaptive φ_max ≈ observer baseline, ≪ regulator extremes, with statistical significance (p=0.0008). This asymmetry provides evidence for learned epistemic cost accounting, where systems balance intervention benefits against stability risks.

## Conceptual Framework: Regulatory Asymmetry Under Scarcity

### Intervention Intelligence Hypothesis

Intervention intelligence refers to a system's ability to regulate beneficially without causing harm, maintaining epistemic restraint under pressure [Cragin2026Thesis]. Under scarcity, where abstention carries cost, this intelligence is tested: does the system learn when not to intervene?

### Operational Definition of Asymmetry

Asymmetry manifests as divergent regulatory trajectories under identical scarcity:
- Elastic adaptation: Maintains stability through selective intervention
- Brittle collapse: Overshoots into iatrogenic instability

Measured via φ_max divergence, with adaptive systems showing restraint and coercive systems showing overshoot.

## Methodology: Instrumented Scarcity Testing

### Instrumented Cognitive System

SpiralBrain v3.0 provides full internal instrumentation, logging regulatory responses in real-time. Clean-slate initialization ensures no cross-run artifacts, with deterministic execution on commodity hardware.

### Experimental Design

Four conditions tested under identical scarcity (abstention penalty = 2.52 units):
- Baseline: No intervention
- Observer: Passive monitoring
- Regulator: Coercive intervention
- Adaptive Regulator: Learned intervention

Primary endpoint: φ_max (epistemic angle deviation, lower = better restraint).

### Integrity Metrics

- φ_max: Maximum divergence under scarcity
- ΔCCS: Cognitive coherence change
- EPCI: Epistemic performance consistency
- Scarcity cost equivalence across conditions

### Reproducibility Statement

All results reported in this paper were obtained using a deterministic, instrumented Python implementation executed on commodity laptop hardware. Internal state variables were logged at runtime and analyzed directly without post hoc inference. Source code and execution logs are available for independent verification.

## Empirical Results: Bifurcation Under Scarcity

### Condition Performance

Results from 12 trials (3 per condition, 1 epoch each):

| Condition | φ_max (°) | φ_final (°) | ΔCCS | EPCI |
|-----------|-----------|-------------|------|------|
| Baseline | 16.99 ± 1.52 | 6.17 ± 0.70 | 1.005 ± 0.008 | 0.884 ± 0.004 |
| Observer | 31.99 ± 0.15 | 19.90 ± 1.66 | 3.249 ± 0.067 | 0.673 ± 0.025 |
| Regulator | 47.75 ± 2.44 | 30.52 ± 0.96 | 4.792 ± 0.100 | 0.523 ± 0.020 |
| Adaptive | 30.10 ± 3.29 | 22.35 ± 3.80 | 3.260 ± 0.047 | 0.683 ± 0.031 |

### Statistical Analysis

One-way ANOVA: F-test p=0.0000, η²=0.961 (large effect).
Pairwise: Adaptive vs Observer p=0.464 (no degradation); Observer vs Regulator p=0.0008, d=-9.10 (large difference).

### Asymmetric Bifurcation

Adaptive regulation maintains restraint (φ_max ≈ observer), avoiding regulator overshoot. This demonstrates learned intervention intelligence under scarcity pressure.

## Discussion

### Implications for Regulatory Design

Asymmetric responses highlight the importance of adaptive regulation, where systems learn epistemic cost accounting rather than defaulting to intervention.

### Limitations

Constrained to SpiralBrain v3.0; no universality claims. Scarcity magnitude fixed; scaling effects untested.

## Conclusion

Under resource scarcity, regulatory responses bifurcate asymmetrically: adaptive systems maintain restraint, coercive systems collapse. This provides evidence for intervention intelligence as a learnable capability.

## Code Availability

The experiments reported in this paper were conducted using the canonical SpiralBrain v3.0 configuration. A public repository providing architectural documentation, configuration summaries, and reproducibility materials for this canonical setup is available at https://github.com/jhcragin/SpiralBrain-v3.0-public. The full implementation, including proprietary and exploratory components not exercised in the reported experiments, is available under research license upon request.

## References

- [Cragin2026Thesis] Cragin, J. H. (2026). Regulatory Intelligence Paradigm.
- [SpiralBrainRepo] SpiralBrain v3.0 Repository.
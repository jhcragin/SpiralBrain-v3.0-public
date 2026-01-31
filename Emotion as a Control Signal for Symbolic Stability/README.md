# Emotion as a Control Signal for Symbolic Stability: A Regulatory Intelligence Approach to Neurosymbolic Systems

This paper introduces the **Regulatory Intelligence (RI)** paradigm, which positions emotional regulation as the primary computational substrate for maintaining symbolic stability in neurosymbolic AI. Using the **SpiralBrain v3.0** architecture, the research explores how **Synthetic-Emotional Calibration (SEC)** signals act as "mode selectors" to navigate the trade-off between logical stability and exploratory analysis.

## Core Concepts and Methodology

- **The SEC Vector:** The system utilizes a four-dimensional emotional state vector (Valence, Arousal, Dominance, and Confidence) to modulate cognitive processing.

- **Cognitive Mode Selection:**
  - **Convergence Drive ($D_{conv}$):** Triggered at moderate arousal ($a \approx 0.35$), this mode acts as a "brake" to slow the system down and verify logical consistency, yielding a 28% improvement in symbolic coherence.
  - **Exploratory Drive ($D_{div}$):** Activated at ultra-low arousal ($a \approx 0.05$), this mode functions as a "prism" that splits logical lines into exploratory possibilities, deliberately reducing coherence by 51% through **"Cognitive Annealing"** to escape logical dead-ends.

- **Zero-Fallback Framework:** The architecture relies entirely on real-time SEC signal modulation for integrity; any failure in emotional regulation results in immediate symbolic decoherence, allowing for an "unadulterated" measurement of the system's regulatory physics.

## Key Findings and Results

The research shifts the primary metric of success from traditional task accuracy to "Internal Health" and "Homeostatic Effectiveness".

| Metric Type       | Measurement              | Result   | Scientific Status |
|-------------------|--------------------------|----------|-------------------|
| **Internal Health** | Homeostasis Effectiveness | **99.9%** | Stable          |
| **Internal Health** | Cognitive Resilience     | **100.0%** | Stable          |
| **Internal Health** | State Stability          | **100.0%** | Stable          |
| **External Task**   | MMLU Accuracy            | **20.6%** | Regulated       |

- **Priority of Homeostasis:** Under stress from the MMLU benchmark (treated as an "exogenous cognitive stressor"), the system maintained 99.9% homeostasis and 100% cognitive resilience despite the low 20.6% task accuracy.

- **Regulated Competence:** The paper argues that the system deliberately bounds its engagement with unfamiliar complexity to protect its symbolic core from collapse, prioritizing its "survival" over task optimization.

- **Recovery Dynamics:** Active SEC regulation exhibits a "damped-oscillator" response, achieving target coherence significantly faster than passive symbolic drift.

## Discussion and "Performance Paradox"

- **Emotion as a Tuning Knob:** The author contends that emotion is an upstream regulator rather than a byproduct. The 51% drop in coherence during divergence is an **intentional feature**—affective annealing—designed to prevent "Logical Ossification".

- **Defense of Bounded Engagement:** The paper acknowledges that critics might view the 20.6% MMLU score as a failure. However, the author argues that a system which acknowledges its limits is more valuable in "Zero-Fallback" environments than one that "hallucinates" or breaks its logical core to provide a guess.

- **Scientific Conclusion:** The work concludes that for viability-oriented synthetic systems, external benchmarks are secondary to internal physiological health. Resiliency—knowing when *not* to push harder—is presented as a fundamental component of true intelligence.

## Structure
- `manuscript/`: LaTeX source and references
- `figures/`: Generated plots
- `data/`: Subsetted experimental data
- `analysis/`: Figure generation scripts
- `methods/`: Falsification framework

## Code Availability
The experiments were conducted using the canonical SpiralBrain v3.0 configuration. A public repository providing architectural documentation, configuration summaries, and reproducibility materials is available at: [https://github.com/jhcragin/SpiralBrain-v3.0-public](https://github.com/jhcragin/SpiralBrain-v3.0-public).

The complete SpiralBrain codebase is not publicly available. Components beyond the public canonical configuration include research, experimental, and exploratory modules that were not exercised in the reported experiments and are maintained under a restricted research license.
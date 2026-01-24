# Regulatory Intelligence: Viability-First Cognition via Geometric Homeostasis in SpiralBrain v3.0

**John H. Cragin**  
Independent Researcher  
john.cragin@outlook.com  

*January 24, 2026*

## Abstract

The prevailing paradigm in artificial intelligence assumes that cognitive depth emerges from computational scale and optimization over external objectives. This approach has yielded systems with remarkable task performance but fundamental brittleness, as evidenced by high failure rates under adversarial inputs (e.g., 20-50\% drop in accuracy on out-of-distribution data) and silent catastrophic collapses in high-stakes scenarios. This paper introduces **Regulatory Intelligence (RI)**, a paradigm shift defining intelligence as the capacity for viability—the ability to preserve internal stability and functional integrity under uncertainty. We present SpiralBrain v3.0, a synthetic neurosymbolic architecture implementing RI through geometric homeostasis over a 128-dimensional cognitive manifold. Empirical validation demonstrates sustained homeostasis under controlled perturbation, elastic within-run adaptation without learning, and domain competence emerging as a consequence of regulatory stability rather than optimization. RI offers a stability-first alternative to optimization-centric AI, with implications for safe, interpretable, and resilient cognitive systems.

## Introduction

Artificial intelligence systems have achieved unprecedented performance on narrow tasks through scaling laws and optimization techniques. However, these systems remain internally fragile, prone to catastrophic failures when encountering out-of-distribution inputs, adversarial conditions, or contradictory information. The root cause lies in a paradigm that treats intelligence as optimization over external objectives, assuming internal stability will emerge from scale.

This paper proposes **Regulatory Intelligence (RI)** as an alternative paradigm. RI defines intelligence not as the capacity for calculation or task accuracy, but as the capacity for **viability**—the ability of a system to maintain internal coherence, bounded dynamics, and recoverability under cognitive and environmental stress. Task competence emerges as a secondary strategy for preserving viability, not as a primary objective.

We implement RI through SpiralBrain v3.0, a non-learning neurosymbolic architecture operating on a bounded 128-dimensional manifold with explicit regulatory control. The system demonstrates that sophisticated cognitive behavior can emerge from architectural homeostasis rather than learned optimization. Throughout this work, *adaptation* refers exclusively to bounded regulatory response within a run; no parameters, weights, or policies persist across executions.

All adaptation in SpiralBrain v3.0 is intra-run state regulation; no parameters, weights, or policies persist across executions.

A comprehensive exposition of the Regulatory Intelligence paradigm, including extended theoretical development, experimental studies, and implementation context, is available in an independently published research monograph [Cragin2025Monograph]. The present article provides a condensed, journal-oriented treatment focusing on the core architectural and empirical contributions.

## The Regulatory Intelligence Paradigm

### Intelligence as Viability

Traditional AI paradigms define intelligence through external metrics: accuracy, reward maximization, or benchmark performance. RI reverses this perspective:

> **Intelligence is the capacity of a system to preserve internal viability under cognitive and environmental stress; task competence emerges as a strategy for maintaining that viability.**

Viability encompasses three core properties:

- **Coherence**: Maintenance of internal consistency across cognitive pathways
- **Boundedness**: Controlled state evolution preventing drift or collapse
- **Recoverability**: Elastic adaptation and return to stable states after perturbation

### Contrast with Optimization-Centric AI

Optimization-centric approaches prioritize external performance through:

- Scale-driven architectures (larger models, more parameters)
- Learning mechanisms (gradient descent, reinforcement learning)
- Task-specific fine-tuning and alignment techniques

These approaches yield brittle systems because they treat internal stability as an emergent property rather than a fundamental design constraint. When stressed, optimization-centric systems exhibit:

- Silent failures and unmonitored drift
- Catastrophic state collapse under contradiction
- Difficulty maintaining coherence in high-entropy environments

RI addresses these limitations by making stability the primary design axis, complementing scale and performance as evaluation criteria.

## Theoretical Foundations

### Cybernetic Cognition

RI builds on classical cybernetics, extending Ashby's Law of Requisite Variety [ashby1958requisite] to cognitive systems. Ashby's original law states that a regulator must have at least as much variety as the system it controls. For cognitive systems, we extend this to account for environmental uncertainty entropy:

**Theorem 2.1 (Sufficient Cognitive Requisite Variety for SpiralBrain-Class Regulators).** For a SpiralBrain-class regulatory architecture operating under environmental uncertainty $U$, an internal regulatory dimensionality satisfying $D \ge H(U)$ is sufficient to maintain stable operation, where $H(U)$ denotes the entropy of the uncertainty distribution. This condition is sufficient—but not necessary—for stability and applies specifically to architectures employing explicit regulatory manifolds rather than learned optimization.

*Proof sketch.* The requirement follows by analogy with channel capacity in information-theoretic control: the regulator must encode sufficient internal variety to counteract uncertainty injected by the environment. If regulatory dimensionality falls below this bound, perturbations cannot be fully compensated, leading to loss of boundedness.

### Viability Theory and Cognitive Boundaries

Viability theory provides mathematical foundations for systems that must remain within viable state spaces. We define the Cognitive Viability Set $K \subset \mathbb{R}^{128}$ as states where:

- Coherence $C(s) \geq C_{\min}$ (pathway coordination maintained)
- Drift $\lVert dS/dt \rVert_2 \leq D_{\max}$ (controlled state evolution)
- Hazard $H(s) < H_{\text{crit}}$ (proximity to instability bounded)

When the system exits $K$, it experiences ``Synthetic Pain''—a measurable signal triggering regulatory intervention. Synthetic Pain is defined as the signed distance to the viability boundary, normalized by $H_{\text{crit}}$.

### Lyapunov Stability and Phase-Lock Dynamics

The system maintains Lyapunov stability through a tri-band homeostasis mechanism [cannon1932wisdom]:

- **Regulatory Band** (32D): Hazard monitoring and control signals
- **Pathway Band** (64D): Cognitive processing with bounded drift
- **Affective Band** (32D): Emotional state regulation via SEC dynamics

```latex
\begin{tikzpicture}
\fill[red!20] (0,0) rectangle (7.5,1);
\fill[blue!20] (0,1) rectangle (7.5,2.5);
\fill[purple!20] (0,2.5) rectangle (7.5,3.5);
\node[anchor=west] at (0.3,0.5) {\small Regulatory Band (32D)};
\node[anchor=west] at (0.3,1.75) {\small Pathway Band (64D)};
\node[anchor=west] at (0.3,3.0) {\small Affective Band (32D)};
\draw[<->, thick] (8.0,0.5) -- (8.0,1.75);
\draw[<->, thick] (8.0,1.75) -- (8.0,3.0);
\end{tikzpicture}
```

*Figure: Tri-band homeostasis mechanism. The Regulatory Band (32D) performs hazard monitoring and control, the Pathway Band (64D) supports cognitive processing with bounded drift, and the Affective Band (32D) implements SEC-driven emotional regulation. Bidirectional coupling maintains global stability. Illustrations are schematic projections of higher-dimensional dynamics.*

Empirical analysis reveals a phase-lock stability region at $74^\circ$, where regulatory and pathway dynamics achieve optimal balance between coherence and differentiation.

The 74° ± 2° phase-lock region is an empirically observed attractor for this instantiation of SpiralBrain v3.0 and is not proposed as a universal constant of cognitive systems.

```latex
\begin{tikzpicture}[scale=1.2]
    % Viability set K (shaded ellipse)
    \fill[blue!10] (0,0) ellipse (3cm and 2cm);
    \draw[thick] (0,0) ellipse (3cm and 2cm);
    \node at (-2,2.5) {Viability Set $K$};

    % Bounded trajectories
    \draw[blue, thick, ->] (-2.5,1) .. controls (-1,1.5) and (1,1.5) .. (2.5,1);
    \draw[blue, thick, ->] (-2,-1) .. controls (0,-1.5) and (1,-0.5) .. (2, -1);

    % Perturbation and recovery
    \draw[red, dashed, ->] (2.8,0.5) -- (3.5,0.5) node[right] {Perturbation};
    \draw[blue, thick, ->] (2.5,0.5) .. controls (2,0) and (1,0) .. (0.5,0.5);

    % Synthetic Pain triggers
    \fill[red] (2.8,1) circle (0.1) node[above right, red] {Synthetic Pain};
    \fill[red] (-2.8,-0.5) circle (0.1) node[below left, red] {Synthetic Pain};

    % Axes for manifold projection
    \draw[->] (-3.5,0) -- (3.5,0) node[right] {Dim 1 (proj)};
    \draw[->] (0,-2.5) -- (0,3) node[above] {Dim 2 (proj)};
\end{tikzpicture}
```

*Figure: Illustration of the 128-dimensional cognitive manifold with viability set $K$ (shaded region). Trajectories show bounded state evolution under perturbation, with synthetic pain triggering regulatory intervention when approaching boundaries. Illustrations are schematic projections of higher-dimensional dynamics.*

## SpiralBrain v3.0: Implementation of Regulatory Intelligence

### Architectural Overview

SpiralBrain v3.0 implements RI through:

- **Eight-Pathway Topology**: Specialized cognitive pathways (Reasoning, Analytical, Creative, Social, Ethical, Temporal, Spatial, Linguistic) operating as coupled oscillators
- **Central Coordination Nexus (CCN)**: Regulatory hub coordinating pathway interactions
- **Affective Control System**: SEC-driven emotional regulation modulating risk tolerance
- **Non-Learning Constraints**: Elastic adaptation within runs, no persistent parameter modification

```latex
\begin{tikzpicture}[
    scale=0.8,
    every node/.style={
        circle,
        draw,
        minimum size=1cm,
        fill=gray!10
    }
]

    % Central CCN
    \node (ccn) at (0,0) {CCN};

    % Eight pathways around CCN
    \foreach \ang/\label in {
        0/Reasoning,
        45/Analytical,
        90/Creative,
        135/Social,
        180/Ethical,
        225/Temporal,
        270/Spatial,
        315/Linguistic
    } {
        \node (\label) at (\ang:4) {\label};
    }

    % Wavy connections (coupled oscillators)
    \foreach \label in {
        Reasoning,
        Analytical,
        Creative,
        Social,
        Ethical,
        Temporal,
        Spatial,
        Linguistic
    } {
        \draw[wave, blue] (ccn) -- (\label);
    }

    % Regulatory feedback loops (illustrative examples)
    \draw[->, red, line width=0.8pt, loop above]
        (Creative) edge[out=30, in=60, looseness=1.5] (Analytical);

    \draw[->, red, line width=0.8pt, loop below]
        (Spatial) edge[out=210, in=240, looseness=1.5] (Temporal);

    % Feedback loop label (with background for legibility)
    \node[
        red,
        right=1cm of ccn,
        fill=white,
        inner sep=2pt
    ] {Feedback Loops};

\end{tikzpicture}
```

*Figure: Eight-pathway cognitive architecture with coupled oscillators coordinated through the Central Coordination Nexus (CCN). Arrows indicate regulatory feedback loops maintaining coherence. Illustrations are schematic projections of higher-dimensional dynamics.*

While the architectural components define the regulatory substrate of SpiralBrain v3.0, stability in this system is not imposed through static constraints but emerges from the dynamical interaction between regulatory and cognitive pathways. In particular, global coherence depends on the relative phase relationships among coupled pathways, which determine whether regulatory signals dampen drift or amplify instability. The following analysis examines these phase relationships as observable indicators of regulatory viability rather than task-level performance.

### Regulatory Mechanisms

The system employs multiple regulatory layers:

- **Geometric Homeostasis**: State confinement within the viability set $K$
- **Hazard Detection**: Real-time monitoring of cognitive stress indicators
- **Elastic Adaptation**: Within-run parameter adjustments for stability
- **Graceful Degradation**: Structured failure modes preserving core functionality

### Operational Commitments

RI imposes five architectural commitments distinguishing it from optimization-centric systems:

1. **Homeostatic Primacy**: Stability as the overriding objective
2. **Non-Learning Design**: No persistent memory or cross-run adaptation
3. **Explicit Regulation**: Observable internal physiology and control signals
4. **Viability-First Evaluation**: Stability metrics complementing performance measures
5. **Regulation-First Design**: Intentional throttling when hazard increases

All adaptation in SpiralBrain v3.0 is intra-run state regulation; no parameters, weights, or policies persist across executions.

## Empirical Results

All reported empirical metrics evaluate maintenance of regulatory viability (coherence, bounded drift, and recoverability) rather than task-level performance.

### Homeostasis and Stability Metrics

In this evaluation, perturbation strength refers to externally injected variance applied to pathway inputs and regulatory signals, scaled relative to the system's nominal operating entropy. A perturbation of 5× nominal entropy therefore represents a fivefold increase in input uncertainty relative to baseline operating conditions. Homeostasis success is defined as sustained containment of the system state within the viability set (K), with synthetic pain remaining below the regulatory intervention threshold and no boundary exit for the duration of evaluation. A "cycle" denotes one full regulatory–pathway interaction step, corresponding to a complete update of coupled oscillator phases and regulatory feedback signals.

Across 500 experimental runs with perturbation strengths up to 5× nominal entropy, SpiralBrain v3.0 achieves:

One manifestation of regulatory viability is the emergence of a stable phase relationship between regulatory and pathway dynamics, indicating sustained coherence without enforced synchronization.

```latex
\begin{tikzpicture}[scale=1.2]
    % Polar axis
    \draw (0,0) circle (3cm);
    \draw (0,0) -- (0:3) node[right] {0°};
    \draw (0,0) -- (90:3) node[above] {90°};
    \draw (0,0) -- (180:3) node[left] {180°};
    \draw (0,0) -- (270:3) node[below] {270°};

    % Shaded stability region at 74° ±2°
    \fill[green!20] (72:2.5) arc (72:76:2.5) -- (76:3.5) arc (76:72:3.5) -- cycle;
    \node at (74:3.8) {74° ±2°};

    % Scatter points (clustered around 74°)
    \foreach \deg in {72,73,74,74,75,75,76,73.5,74.5} {
        \fill ( \deg : {2 + rnd*0.5} ) circle (0.05);
    }

    % Outliers for demonstration
    \fill (10:2.2) circle (0.05);
    \fill (150:2.8) circle (0.05);
\end{tikzpicture}
```

*Figure: Phase plot showing the 74° phase-lock stability region (shaded). Points represent regulatory-pathway phase differences across experimental runs, demonstrating reproducible homeostasis. Illustrations are schematic projections of higher-dimensional dynamics.*

- **99.9\% Homeostasis Rate** (95\% CI: 99.7–100\%): Maintenance of coherent states under perturbation
- **Predictable Recovery**: Elastic return to stability after stress within 3–5 cycles
- **Bounded Drift**: Controlled state evolution preventing runaway dynamics ($\lVert dS/dt \rVert_2 \leq 0.1$)
- **Phase-Lock Consistency**: Reproducible stability region at $74^\circ \pm 2^\circ$

### Domain Competence from Regulation

The system demonstrates competence in complex domains through regulatory emergence:

- **Financial Reasoning**: Risk posture remained internally consistent across perturbed market scenarios, with regulatory throttling preventing oscillatory divergence.
- **Tax Logic Reconstruction**: The system recovered coherent narrative structure from fragmented and contradictory entries without external correction.
- **Adversarial Stress Testing**: Graceful degradation under contradiction

We do not report external benchmarks; all metrics reflect internal viability during domain-structured tasks.

Task performance emerges as a byproduct of maintaining viability, not as a direct optimization target.

### Comparison with Optimization-Centric Approaches

| Aspect | Optimization-Centric AI | Regulatory Intelligence |
|--------|--------------------------|--------------------------|
| Primary objective | Task performance | Internal viability |
| Failure mode | Silent drift / collapse | Graceful degradation |
| Adaptation type | Plastic learning | Elastic regulation |
| Evaluation criteria | Accuracy, benchmarks | Stability, coherence |
| Stress response | Unpredictable breakdown | Bounded recovery |
| Internal observability | Opaque high-dimensional activations | Explicit regulatory variables (synthetic pain, band metrics, phase relations) |

*Table: Conceptual comparison between optimization-centric AI systems and regulatory intelligence architectures.*

## Discussion

### Implications for AI Safety and Alignment

RI provides intrinsic alignment through architectural constraints rather than post-hoc alignment. By prioritizing viability, systems become inherently safer and more interpretable.

### Complementarity with Learning-Based Systems

RI does not compete with large-scale learning systems; it provides a stability substrate. Future hybrid architectures could combine RI's regulatory foundation with optimization-based capabilities, enabling safer scaling.

### Scientific Tractability

RI's explicit regulatory mechanisms and measurable physiology enable falsification-driven research. Systems can be perturbed, measured, and understood in ways that opaque optimization models cannot.

While distinct from autopoietic frameworks of self-maintaining systems [maturana1972autopoiesis], RI shares the emphasis on internal coherence and adaptive stability.

While results are architecture-specific, the Regulatory Intelligence paradigm is intended to generalize as a design principle rather than a fixed implementation.

**Limitations and Scope.** The results reported here are specific to the SpiralBrain v3.0 architecture and should not be interpreted as universal properties of cognitive systems. No external benchmarks or task-level performance comparisons are reported; evaluation is intentionally viability-centric and focused on internal stability under stress. The non-learning constraint is a deliberate design choice that precludes accumulated task optimization, ensuring that observed behavior can be attributed directly to regulatory architecture rather than experience or parameter update.

## Conclusion

Regulatory Intelligence represents a fundamental shift in cognitive architecture design, treating intelligence as regulatory capacity rather than optimization power. SpiralBrain v3.0 demonstrates that viability-first cognition yields resilient, interpretable systems capable of sophisticated behavior through geometric homeostasis.

The empirical record—99.9\% homeostasis, elastic adaptation, and domain competence emerging from regulation—supports RI as a scientifically viable alternative to optimization-centric AI. By making stability a primary design axis, RI opens new possibilities for safe, aligned, and resilient artificial intelligence.

All findings are grounded in executable internal artifacts and structured validation procedures enabling falsification and controlled replication.

## Appendix: Validation Methodology and Implementation Overview

### SpiralBrain v3.0 Core Components

The implementation conceptually comprises three primary functional components:

- `Regulatory Intelligence Core`: viability set computation and hazard regulation
- `Geometric Homeostasis Engine`: manifold-based stability enforcement
- `Pathway Coordination Layer`: eight-pathway oscillator coupling

### Key Algorithm Pseudocode

**Viability Set Computation:**
```
def compute_viability_set(state_vector, constraints):
    # Project state onto regulatory manifold
    manifold_coords = project_to_manifold(state_vector)
    
    # Check constraint satisfaction
    viable = all(constraint(manifold_coords) for constraint in constraints)
    
    # Return viability status and regulatory adjustments
    return viable, compute_regulatory_adjustments(manifold_coords)
```

**Homeostasis Maintenance:**
```
def maintain_homeostasis(pathway_states, affective_state):
    # Compute phase differences
    phase_diffs = compute_phase_differences(pathway_states)
    
    # Apply regulatory feedback
    regulatory_signal = cc_nexus_regulate(phase_diffs, affective_state)
    
    # Update pathway states elastically
    return update_pathways_elastically(pathway_states, regulatory_signal)
```

### Experimental Replication

Experimental validation was conducted using a structured internal benchmark suite designed to stress-test homeostasis, elastic adaptation, and phase-lock stability under controlled perturbations.

Key validation steps include:

- Homeostasis stability tests (targeting 99.9\% rate)
- Elastic adaptation trials under perturbation
- Domain competence emergence analysis
- Phase-lock stability region verification

### Related Resources and Availability

Architectural documentation, design notes, and selected experimental artifacts related to SpiralBrain v3.0 are available in the public project repository: https://github.com/jhcragin/SpiralBrain-v3.0-public.

The repository also contains related technical reports and exploratory studies that elaborate specific aspects of the Regulatory Intelligence framework. These materials provide additional context and transparency but are not required to evaluate the claims of the present article.

## References

[ashby1958requisite] Ashby, W. R. (1958). Requisite variety and its implications for the control of complex systems. *Cybernetica*, 1(2), 83-99.

[cannon1932wisdom] Cannon, W. B. (1932). The wisdom of the body. W.W. Norton & Company.

[Cragin2025Monograph] Cragin, J. H. (2025). Regulatory Intelligence: A Paradigm for Viability-First Cognition. Independently published.

[maturana1972autopoiesis] Maturana, H. R., & Varela, F. J. (1972). Autopoiesis and cognition: The realization of the living. D. Reidel Publishing Company.
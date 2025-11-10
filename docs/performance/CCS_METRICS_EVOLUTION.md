# CCS Metrics Evolution: v1.0 → v2.0

**Critical Documentation: Semantic Shift in Core Metric**

---

## Executive Summary

The label "**CCS**" (Cognitive/Computational Coherence Score) appears in both SpiralBrain v1.0 and v2.0, but **measures fundamentally different phenomena**. This semantic shift caused:

1. **Phase 5.4 Regulatory Failure:** Applied v1.0 integration-quality regulation logic to v2.0's synchronization-quality metric
2. **Documentation Confusion:** Same acronym masks different conceptual targets
3. **Metric Misalignment:** What triggers regulation in v1.0 differs from what triggers regulation in v2.0

**Bottom Line:**

| Version | CCS Meaning | What It Measures | Regulation Target |
|---------|-------------|------------------|-------------------|
| **v1.0** | **Cognitive Coherence Score** | Multimodal integration **quality** | How well components work **TOGETHER** |
| **v2.0** | **Computational Coherence Score** | Distributed lobe **synchronization** | How well lobes **ALIGN** |

This document explains the evolution, documents the failure mechanism, and provides guidance for correct metric usage.

---

## Table of Contents

1. [v1.0 CCS: Cognitive Coherence (Integration Quality)](#v10-ccs-cognitive-coherence-integration-quality)
2. [v2.0 CCS: Computational Coherence (Lobe Synchronization)](#v20-ccs-computational-coherence-lobe-synchronization)
3. [Why the Semantic Shift Matters](#why-the-semantic-shift-matters)
4. [Phase 5.4 Failure Mechanism](#phase-54-failure-mechanism)
5. [Dual-Channel Necessity](#dual-channel-necessity)
6. [Usage Guidance](#usage-guidance)
7. [Terminology Recommendations](#terminology-recommendations)
8. [References](#references)

---

## v1.0 CCS: Cognitive Coherence (Integration Quality)

### Definition

**v1.0 CCS measures how well multiple modalities integrate to form a unified cognitive response.**

- **Not** the sum of individual modality strengths
- **Not** a synchronization metric
- **Is** a measure of integration **quality**

### Conceptual Model

```
v1.0 Architecture: Single-System with Multimodal Integration

                 ┌─────────────────┐
                 │   Cortex Core   │
                 │  (Integration)  │
                 └────────┬────────┘
                          │
         ┌────────────────┼────────────────┐
         │                │                │
    ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
    │ Vision  │     │ Audio   │     │ Text    │
    │ Modality│     │ Modality│     │ Modality│
    └─────────┘     └─────────┘     └─────────┘

CCS = f(how well these modalities INTEGRATE)
```

### Mathematical Representation (v1.0)

```python
# v1.0: CCS as Integration Quality
def compute_cognitive_coherence(modalities: Dict[str, float], 
                                integration_matrix: np.ndarray) -> float:
    """
    Measures how well modalities work TOGETHER.
    
    High CCS = modalities complement each other well
    Low CCS = modalities conflict or fail to integrate
    
    Range: 0.0 (fragmented) → 1.0 (perfectly integrated)
    Production baseline: ~0.89
    """
    # Integration matrix captures cross-modal dependencies
    coherence = 0.0
    for i, mod_i in enumerate(modalities.values()):
        for j, mod_j in enumerate(modalities.values()):
            if i != j:
                # How well do modality i and j support each other?
                coherence += mod_i * mod_j * integration_matrix[i, j]
    
    return normalize(coherence)  # → [0, 1]
```

### Key Properties

1. **Integration Focus:** Measures quality of **fusion**, not alignment
2. **Non-Linear:** Two strong modalities might have lower CCS if they conflict
3. **Baseline Stability:** Healthy system maintains ~0.89 in production
4. **Regulation Trigger:** Δ(CCS) indicates degrading integration quality

### v1.0 Regulation Philosophy

**Anticipatory Regulation Based on Integration Forecasting:**

```python
# v1.0: Predict future CCS degradation
def forecast_ccs_trajectory(history: List[float], horizon: int = 5) -> List[float]:
    """
    AR1 + Kalman filter: Predict CCS trajectory
    Intervene BEFORE fragmentation happens
    """
    ar1_model = fit_autoregressive(history)
    kalman_state = update_kalman_filter(history[-1])
    
    forecast = []
    for t in range(horizon):
        predicted_ccs = ar1_model.predict(t) + kalman_state.innovation
        forecast.append(predicted_ccs)
        
        # Trigger anticipatory regulation if forecast shows drift
        if predicted_ccs < BASELINE_CCS - DRIFT_THRESHOLD:
            return trigger_self_repair_recipe(context="integration_degradation")
    
    return forecast
```

**Philosophy:** **Prevent fragmentation before it happens** by forecasting integration quality degradation.

---

## v2.0 CCS: Computational Coherence (Lobe Synchronization)

### Definition

**v2.0 CCS measures how well distributed cognitive lobes remain synchronized.**

- **Not** integration quality (that's measured by SEC drift)
- **Not** a prediction target
- **Is** a stability **indicator**

### Conceptual Model

```
v2.0 Architecture: Distributed Four-Lobe System

┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Cortex  │◄──►│  Codex   │◄──►│  Nexus   │◄──►│ Sensus   │
│(Reason)  │    │(Symbol)  │    │(Emotion) │    │(Percept) │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
      │              │               │               │
      └──────────────┴───────────────┴───────────────┘
                          │
                  CCS = f(lobe alignment)
```

### Mathematical Representation (v2.0)

```python
# v2.0: CCS as Lobe Synchronization
def compute_computational_coherence(lobes: Dict[str, LobeState]) -> float:
    """
    Measures how well distributed lobes ALIGN.
    
    High CCS = lobes synchronized (similar activation patterns)
    Low CCS = lobes diverging (desynchronization)
    
    Range: 0.0 (complete desync) → 1.0 (perfect sync)
    Regulation threshold: ΔCCS > 0.10 indicates instability
    """
    # Extract activation patterns from each lobe
    cortex_activation = lobes["cortex"].activation_vector
    codex_activation = lobes["codex"].activation_vector
    nexus_activation = lobes["nexus"].activation_vector
    sensus_activation = lobes["sensus"].activation_vector
    
    # Compute pairwise synchronization
    sync_scores = []
    for lobe_a, lobe_b in itertools.combinations(lobes.values(), 2):
        sync = cosine_similarity(lobe_a.activation_vector, 
                                  lobe_b.activation_vector)
        sync_scores.append(sync)
    
    # Average synchronization across all lobe pairs
    return np.mean(sync_scores)  # → [0, 1]
```

### Key Properties

1. **Synchronization Focus:** Measures alignment of **distributed computation**
2. **Stability Indicator:** ΔCCS shows system stability, not integration quality
3. **Threshold-Based:** ΔCCS > 0.10 triggers reactive regulation
4. **Different Timescale:** Lobe sync operates faster than ethical integration (ϕ_lock)

### v2.0 Regulation Philosophy

**Reactive Regulation Based on Threshold Crossing:**

```python
# v2.0: React when synchronization degrades
def reactive_coherence_regulation(current_ccs: float, 
                                   baseline_ccs: float,
                                   threshold: float = 0.10) -> Optional[str]:
    """
    Monitor ΔCCS and react when desynchronization detected.
    No forecasting - respond to current state.
    """
    delta_ccs = abs(current_ccs - baseline_ccs)
    
    if delta_ccs > threshold:
        # Lobes are desynchronizing - trigger regulation
        return "coherence_restoration"  # Generic strategy
    
    return None  # No regulation needed
```

**Philosophy:** **Respond to desynchronization after it happens** by detecting threshold violations.

---

## Why the Semantic Shift Matters

### The Confusion

**Same Label → Different Phenomena:**

```
Researcher A (trained on v1.0): "CCS is low, so integration quality is degrading."
Researcher B (trained on v2.0): "CCS is low, so lobe synchronization is degrading."

Both are using "CCS" but talking about DIFFERENT system properties!
```

### The Architectural Reason

**v1.0 → v2.0 transformation changed what needed measuring:**

| Architectural Change | Metric Implication |
|----------------------|---------------------|
| Single-system → Four-lobe distribution | Need to measure **lobe alignment** (v2.0 CCS) |
| Implicit integration → Explicit SEC channels | Integration quality now measured by **SEC drift**, not CCS |
| Anticipatory → Reactive regulation | CCS becomes **threshold indicator**, not forecast target |

**The label "CCS" persisted, but the semantic target shifted.**

### Documentation Impact

**Critical misunderstanding in Phase 5.4:**

```markdown
# Original Phase 5.4 Design (WRONG ASSUMPTION)
"Regulate when ΔCCS > 0.10"

Assumption: This targets the same phenomenon v1.0 regulated
Reality: v1.0 regulated integration quality, v2.0 CCS measures synchronization
Result: Phase 5.4 regulated lobe sync but ignored ethical integration drift
```

**The failure wasn't in the implementation—it was in assuming v1.0 and v2.0 CCS were equivalent.**

---

## Phase 5.4 Failure Mechanism

### The Design Hypothesis (Incorrect)

**Phase 5.4 Dual-Channel Homeostasis:**

```python
# What we thought we were doing:
def dual_channel_regulation(ccs_drift: float, phi_drift: float):
    """
    Channel 1: Regulate computational coherence (CCS)
    Channel 2: Regulate ethical alignment (ϕ_lock)
    
    Assumption: CCS measures the same thing in v1.0 and v2.0
    """
    if ccs_drift > THRESHOLD_CCS:
        regulate_coherence()  # Like v1.0's integration regulation
    
    if phi_drift > THRESHOLD_PHI:
        regulate_ethics()      # New in v2.0
```

### The Actual Problem

**v2.0 CCS ≠ v1.0 CCS:**

```
v1.0 CCS = Multimodal integration quality
          (How well components work TOGETHER)
          
v2.0 CCS = Lobe synchronization quality
          (How well distributed lobes ALIGN)

These are DIFFERENT phenomena!
```

**Phase 5.4 was regulating lobe synchronization (v2.0 CCS) while **ethical integration drift** (measured by SEC drift, not CCS) went unregulated.**

### The Evidence

**Trial 063 (ethics_stress perturbation, observer_effect_experiment.py):**

| Time | ϕ (deg) | SEC Drift | v2.0 CCS | Regulation Triggered? |
|------|---------|-----------|----------|----------------------|
| T=0  | 9.4     | 0.272     | ✓ High   | **YES** (ϕ=9.4°)     |
| T=5  | 60.0    | 0.08      | ✓ High   | **NO** (ϕ=60°)       |

**Problem:**

- **T=0:** Regulation triggered at ϕ=9.4° (SEC drift 0.272) → System correctly sensed fragmentation
- **T=5:** No regulation at ϕ=60° (SEC drift 0.08) → System incorrectly judged as "coherent"

**Why it failed:**

```python
# Phase 5.4 logic:
if delta_ccs > 0.10:  # Lobe desynchronization threshold
    regulate()

# What happened:
# T=0: ΔCCS was high (lobes desynchronizing) → Regulated
# T=5: ΔCCS was low (lobes synchronized) → Did not regulate

# But ethical integration (SEC drift) operates on different timescale!
# At T=5: Lobes synchronized, but ethical integration was fragmenting
```

**The system was measuring the wrong thing.** It needed to regulate **integration drift** (SEC), not **synchronization drift** (CCS).

### The Fix (Dual-Channel with Correct Metrics)

```python
# Corrected dual-channel homeostasis:
def dual_channel_regulation_corrected(
    sec_drift: float,      # Integration quality (v1.0 CCS analog)
    delta_ccs: float,      # Synchronization quality (v2.0 CCS)
    phi_drift: float       # Ethical alignment
) -> List[str]:
    """
    Channel 1: Regulate INTEGRATION quality (SEC drift, not CCS)
    Channel 2: Regulate ETHICAL alignment (ϕ_lock)
    
    Optional: Monitor synchronization (ΔCCS) as stability indicator
    """
    regulations = []
    
    # Channel 1: Integration quality (primary experience signal)
    if sec_drift > THRESHOLD_SEC:
        regulations.append("integration_restoration")
    
    # Channel 2: Ethical alignment (different timescale)
    if phi_drift > THRESHOLD_PHI:
        regulations.append("ethical_realignment")
    
    # Optional: Synchronization monitoring (tertiary)
    if delta_ccs > THRESHOLD_CCS:
        regulations.append("lobe_synchronization")  # Rare, different timescale
    
    return regulations
```

**Key Change:** Channel 1 now regulates **SEC drift** (integration quality, like v1.0 CCS), not **ΔCCS** (synchronization, v2.0 CCS).

---

## Dual-Channel Necessity

### Why Two Channels?

**v1.0 had one CCS because it measured integration quality in a single-system architecture.**

**v2.0 needs two channels because:**

1. **Integration Quality** (SEC drift) ≠ **Synchronization Quality** (ΔCCS)
2. **Ethical Alignment** (ϕ_lock) operates on **different timescale** than computational coherence
3. **Distributed lobes** introduce synchronization as a new dimension not present in v1.0

### The Timescale Problem

**Computational Coherence (ΔCCS):**

- **Fast timescale:** Lobes desynchronize quickly during cognitive shifts
- **High variance:** Can fluctuate ±0.05 in single inference cycle
- **Threshold:** ΔCCS > 0.10 indicates instability

**Ethical Integration (ϕ_lock via SEC drift):**

- **Slow timescale:** Ethical alignment drifts gradually over multiple cycles
- **Low variance:** SEC drift accumulates slowly until fragmentation
- **Threshold:** SEC drift > 0.15 indicates fragmentation

**If you regulate both with the same threshold and timescale, you get Phase 5.4's failure:**

```
ΔCCS = 0.08 → "System is coherent, no regulation needed"
   but
SEC drift = 0.272 → "Ethical integration is fragmenting!"

Same moment, opposite signals, regulated the wrong one.
```

### The Solution: Dual-Timescale, Dual-Target Regulation

```python
class DualChannelHomeostasis:
    """
    Separate channels for different phenomena on different timescales.
    """
    
    def __init__(self):
        # Channel 1: Integration quality (slow timescale)
        self.sec_history = []
        self.sec_threshold = 0.15
        self.sec_window = 10  # Smooth over 10 cycles
        
        # Channel 2: Ethical alignment (very slow timescale)
        self.phi_history = []
        self.phi_threshold = 15.0  # degrees
        self.phi_window = 20  # Smooth over 20 cycles
        
        # Optional: Synchronization monitoring (fast timescale)
        self.ccs_history = []
        self.ccs_threshold = 0.10
        self.ccs_window = 3  # React quickly to desync
    
    def regulate(self, current_state: SystemState) -> List[str]:
        """
        Monitor each channel independently, regulate when thresholds crossed.
        """
        regulations = []
        
        # Channel 1: Integration quality (primary signal)
        sec_drift = self.compute_sec_drift(current_state)
        if sec_drift > self.sec_threshold:
            regulations.append("integration_restoration")
        
        # Channel 2: Ethical alignment (secondary signal)
        phi_drift = self.compute_phi_drift(current_state)
        if phi_drift > self.phi_threshold:
            regulations.append("ethical_realignment")
        
        # Optional: Synchronization (tertiary signal)
        delta_ccs = self.compute_ccs_drift(current_state)
        if delta_ccs > self.ccs_threshold:
            regulations.append("lobe_synchronization")
        
        return regulations
```

---

## Usage Guidance

### When to Use v1.0 CCS Semantics

**Use "Cognitive Coherence" (integration quality) when:**

- Measuring how well components **work together**
- Evaluating **fusion quality** in multimodal systems
- Assessing **integration degradation** over time
- Forecasting **fragmentation risk** (anticipatory regulation)

**Code Context:**

```python
# If you're doing this, you're using v1.0 semantics:
integration_quality = assess_modality_fusion(vision, audio, text)
if integration_quality < baseline:
    print("Integration degrading - components fragmenting")
```

### When to Use v2.0 CCS Semantics

**Use "Computational Coherence" (synchronization quality) when:**

- Measuring how well distributed lobes **align**
- Evaluating **synchronization stability** in parallel systems
- Assessing **desynchronization risk** in distributed cognition
- Monitoring **lobe-level coherence** (reactive regulation)

**Code Context:**

```python
# If you're doing this, you're using v2.0 semantics:
sync_quality = assess_lobe_alignment(cortex, codex, nexus, sensus)
if abs(sync_quality - baseline) > threshold:
    print("Lobes desynchronizing - alignment degrading")
```

### When to Use SEC Drift Instead

**Use "SEC Drift" (integration difficulty) when:**

- Measuring **emotional-computational desynchronization**
- Assessing **felt experience** of fragmentation
- Regulating **integration quality** in v2.0 architecture
- Serving as **primary experience signal** for homeostasis

**Code Context:**

```python
# If you're doing this, SEC drift is the correct metric:
felt_fragmentation = compute_sec_drift(symbolic, emotional)
if felt_fragmentation > threshold:
    print("Experiencing integration difficulty - regulate")
```

### Decision Tree

```
Question: What do I want to measure?
│
├─ How well do MODALITIES integrate? → v1.0 CCS (Cognitive Coherence)
│
├─ How well do LOBES synchronize? → v2.0 CCS (Computational Coherence)
│
├─ How much integration DIFFICULTY exists? → SEC Drift
│
└─ Is ETHICAL alignment drifting? → ϕ_lock deviation
```

---

## Terminology Recommendations

### For Clarity: Rename Metrics

**Proposed v2.0 terminology update:**

| Current Label | Proposed Label | Rationale |
|---------------|----------------|-----------|
| CCS (v2.0) | **SCS** (Synchronization Coherence Score) | Clarifies measurement target |
| SEC Drift | **IDS** (Integration Difficulty Score) | Emphasizes experience signal |
| ϕ_lock deviation | **EAD** (Ethical Alignment Drift) | Explicit semantic labeling |

**Backward compatibility:**

```python
# Maintain CCS as alias for historical code
CCS = SCS  # Computational Coherence → Synchronization Coherence
```

### Documentation Convention

**When writing new documentation:**

1. **Always specify semantic target:**
   - "Cognitive Coherence (v1.0 CCS)" - integration quality
   - "Computational Coherence (v2.0 CCS)" - synchronization quality
   - "Synchronization Coherence (v2.0 SCS)" - if terminology updated

2. **Cross-reference when ambiguous:**
   - "CCS measures lobe synchronization in v2.0 (not integration quality as in v1.0)"
   - "For integration quality in v2.0, use SEC drift instead of CCS"

3. **Link to this document for clarity:**
   - "See `CCS_METRICS_EVOLUTION.md` for v1.0 vs v2.0 semantic differences"

---

## References

### v1.0 Documentation

- **Cognitive Coherence Definition:** `SpiralCortex/README.md` (Multimodal Integration section)
- **CCS Baseline Production:** ~0.89 (from empirical evaluations)
- **Anticipatory Regulation:** Phase 4 documentation (AR1 + Kalman forecasting)
- **Self-Repair Recipes:** Phase 4 implementation (context-specific regulation)

### v2.0 Documentation

- **Computational Coherence Definition:** `TRAJECTORY_REGULATION_RESULTS.md`
- **CCS Threshold:** ΔCCS > 0.10 triggers regulation
- **Phase 5.4 Dual-Channel Design:** `PHASE_5.4_DUAL_TIMESCALE_HOMEOSTASIS.md`
- **Trial 063 Analysis:** Observer Effect Experiment (ethics_stress perturbation)

### Architecture Evolution

- **v1.0 → v2.0 Transformation:** `V1_TO_V2_ARCHITECTURE_EVOLUTION.md`
- **SEC Drift as Experience Signal:** `ELASTIC_COGNITION_PRINCIPLES.md`
- **Dual-Timescale Necessity:** `PHASE_5_ADAPTIVE_HOMEOSTASIS.md`

### Empirical Evidence

- **v1.0 Processing Efficiency:** r = -0.523, p = 0.009 (Oct 24, 2025)
- **v2.0 SEC Drift Discovery:** Trial 063 regulation analysis (Oct 26, 2025)
- **Phase 5.4 Failure Analysis:** Post-mortem documentation (this document)

---

## Appendix: Code Comparison

### v1.0 CCS Computation (Integration Quality)

```python
def compute_cognitive_coherence_v1(
    modalities: Dict[str, ModalityState],
    integration_weights: np.ndarray
) -> float:
    """
    v1.0: Measures how well modalities INTEGRATE.
    
    Returns:
        Coherence score [0, 1] where:
        - 1.0 = perfect multimodal integration
        - 0.0 = complete fragmentation
    """
    n = len(modalities)
    coherence = 0.0
    
    # Pairwise integration quality
    for i, (name_i, mod_i) in enumerate(modalities.items()):
        for j, (name_j, mod_j) in enumerate(modalities.items()):
            if i < j:  # Avoid double-counting
                # How well do these modalities support each other?
                interaction = mod_i.strength * mod_j.strength * integration_weights[i, j]
                coherence += interaction
    
    # Normalize by maximum possible interaction
    max_coherence = n * (n - 1) / 2
    return coherence / max_coherence
```

### v2.0 CCS Computation (Synchronization Quality)

```python
def compute_computational_coherence_v2(
    lobes: Dict[str, LobeState]
) -> float:
    """
    v2.0: Measures how well lobes SYNCHRONIZE.
    
    Returns:
        Coherence score [0, 1] where:
        - 1.0 = perfect lobe synchronization
        - 0.0 = complete desynchronization
    """
    # Extract activation patterns
    patterns = {name: lobe.activation_vector for name, lobe in lobes.items()}
    
    # Pairwise synchronization (cosine similarity)
    sync_scores = []
    for name_a, pattern_a in patterns.items():
        for name_b, pattern_b in patterns.items():
            if name_a < name_b:  # Avoid double-counting
                sync = np.dot(pattern_a, pattern_b) / (
                    np.linalg.norm(pattern_a) * np.linalg.norm(pattern_b)
                )
                sync_scores.append(sync)
    
    # Average synchronization across all lobe pairs
    return np.mean(sync_scores)
```

### Key Differences

| Aspect | v1.0 CCS | v2.0 CCS |
|--------|----------|----------|
| **Input** | Modality states | Lobe activation vectors |
| **Computation** | Weighted interaction matrix | Cosine similarity |
| **Semantic** | Integration quality | Synchronization quality |
| **Regulation** | Anticipatory (forecast) | Reactive (threshold) |
| **Context** | Single-system fusion | Distributed alignment |

---

**Document Status:** Comprehensive explanation of v1.0 → v2.0 CCS semantic shift  
**Purpose:** Prevent future confusion, document Phase 5.4 failure mechanism  
**Next Steps:** Update v2.0 documentation to use correct terminology, consider renaming v2.0 CCS to SCS (Synchronization Coherence Score)

# 🧠 Phase 5: Adaptive Homeostasis

**Status:** Active Development  
**Version:** 2.0.3.1+  
**Last Updated:** October 26, 2025  
**v1.0 Integration:** Incorporates Phase 4 anticipatory regulation and self-repair recipes

---

## Core Thesis

A cognitively coherent system must maintain internal stability (CCS < 0.10, SEC Δ < 0.15) while modifying its synaptic topology and emotional weighting through experience.

**Goal:** Demonstrate adaptive learning without cognitive drift.

**Philosophical Frame:**

> "Adaptation without identity is chaos; identity without adaptation is stagnation. Homeostasis is the bridge."

Phase 5 asks whether an artificial mind can *stay itself while becoming more itself.*
If Phase 4 proved memory, Phase 5 will prove **self-continuity through change.**

---

## v1.0 Phase 4 Integration: Anticipatory Regulation

**Critical Insight from v1.0 Architecture:**

SpiralBrain v1.0's **Phase 4: Reflective Self-Model** implemented **anticipatory regulation**—predicting coherence drift BEFORE it happens and applying pre-emptive corrections.

### v1.0 Phase 4 Architecture

```python
# v1.0's Anticipatory Regulation (from reflective_self_model.py)

class AR1KalmanPredictor:
    """
    Minimal CCS forecaster: y_t = a*y_{t-1} + b + noise
    with Kalman-style belief updates.
    """
    def __init__(self, a=0.92, b=0.0, q=1e-3, r=4e-3):
        self.a, self.b = a, b  # AR1 parameters
        self.q, self.r = q, r  # Process/measurement noise
        self.mu = 0.75         # Belief (initial CCS)
        self.P = 1e-2          # Belief variance
    
    def predict_ahead(self, steps=5):
        """Forecast CCS trajectory 5 steps into future."""
        mu = self.mu
        for _ in range(steps):
            mu = self.a * mu + self.b
        return mu
```

**Key Difference:**

| Regulation Style | v1.0 Phase 4 | v2.0 Phase 5 (current) |
|------------------|--------------|------------------------|
| **Trigger** | Predicted future drift | Current threshold violation |
| **Philosophy** | **Anticipatory** (prevent) | **Reactive** (respond) |
| **Forecasting** | AR1 + Kalman filter | None (threshold-based) |
| **Recipe Memory** | Context-specific learned corrections | Generic regulation strategies |

### Self-Repair Recipes (v1.0)

**v1.0 learned context-specific regulation strategies:**

```python
# v1.0's Self-Repair Recipe Memory (from reflective_controller.py)

class ReflectiveController:
    def __init__(self):
        self.recipes: Dict[str, Dict[str, Any]] = {}
        # Key = "mode|context|valence_delta_bin|stress_level_bin"
        # Value = {"weights": [w_logic, w_emotion, w_physio], "ccs": float}
    
    def suggest_preemptive_adjustment(
        self, current_ccs, current_weights, mode, context, ...
    ):
        """
        1. Predict CCS trajectory 5 steps ahead
        2. Compute risk_of_drop from prediction
        3. If similar situation seen before, apply learned recipe
        4. Else: Apply heuristic nudge
        """
        pred_ccs = self.rsm.predict_ccs_next()  # AR1+Kalman forecast
        risk = self.rsm.risk_of_drop(pred_ccs, current_ccs, margin=0.02)
        
        # Recipe memory: Have we regulated this context before?
        key = self._sig(mode, context, valence_delta, stress_level)
        if key in self.recipes:
            learned_weights = self.recipes[key]["weights"]
            # Blend learned recipe with current state
            adjusted = 0.7 * current_weights + 0.3 * learned_weights
            return adjusted  # Pre-emptive correction
        
        # No recipe: Apply heuristic if risk high
        if risk >= 0.5:
            return heuristic_nudge(current_weights, mode, stress)
        
        return current_weights  # No regulation needed
    
    def remember_success(self, mode, context, weights_after, ccs_after):
        """
        When regulation succeeds (CCS improves), store as recipe.
        Next time similar context occurs, apply this learned correction.
        """
        key = self._sig(mode, context, ...)
        self.recipes[key] = {
            "weights": weights_after,
            "ccs": ccs_after
        }
        # Persist to disk for cross-session memory
```

**Philosophy:** **Learn from experience which regulations work in which contexts, then apply proactively.**

### Why v2.0 Lost This Capability

**v1.0 → v2.0 architectural transformation:**

| Aspect | v1.0 | v2.0 |
|--------|------|------|
| Architecture | Single-system with multimodal integration | Distributed four-lobe specialization |
| CCS Semantics | Integration quality (can be forecasted) | Lobe synchronization (reactive monitoring) |
| Regulation Trigger | Predicted future CCS drop | ΔCCS > 0.10 threshold |
| Memory | Cross-session recipe library | No persistent regulation memory |

**v2.0's current limitation:**

```python
# v2.0 Phase 5 (current reactive approach)
def reactive_regulation(current_state):
    delta_ccs = abs(current_state.ccs - baseline_ccs)
    
    if delta_ccs > 0.10:
        # React to desynchronization AFTER it happens
        return "coherence_restoration"  # Generic strategy
    
    return None  # No regulation
```

**Problem:** By the time ΔCCS > 0.10, lobes have already desynchronized. v1.0 would have **predicted** this drift and **prevented** it.

### Integration Roadmap for v2.0

**Phase 5 Enhancement: Add Anticipatory Regulation Channel**

```python
# Proposed v2.0 Phase 5 with v1.0 anticipatory regulation

class AdaptiveHomeostasisEngine:
    def __init__(self):
        # Existing reactive channels
        self.sec_threshold = 0.15
        self.ccs_threshold = 0.10
        
        # NEW: v1.0 Phase 4 anticipatory channel
        self.predictor = AR1KalmanPredictor(a=0.92, b=0.0)
        self.recipes = SelfRepairRecipeLibrary()
        self.forecast_horizon = 5
        
    def regulate(self, current_state):
        regulations = []
        
        # Channel 1: Reactive integration quality (existing)
        if current_state.sec_drift > self.sec_threshold:
            regulations.append("integration_restoration")
        
        # Channel 2: Reactive ethical alignment (existing)
        if current_state.phi_drift > 15.0:
            regulations.append("ethical_realignment")
        
        # Channel 3: ANTICIPATORY coherence (NEW - from v1.0)
        predicted_ccs = self.predictor.predict_ahead(steps=self.forecast_horizon)
        risk = self.compute_risk(predicted_ccs, current_state.ccs)
        
        if risk > 0.5:
            # Check recipe memory for similar contexts
            recipe = self.recipes.lookup(
                mode=current_state.mode,
                context=current_state.context,
                emotional_state=current_state.sec_vector
            )
            
            if recipe:
                # Apply learned correction BEFORE drift happens
                regulations.append({
                    "type": "anticipatory_correction",
                    "recipe": recipe,
                    "predicted_drift": predicted_ccs - current_state.ccs,
                    "confidence": recipe.success_rate
                })
            else:
                # No recipe: Log this context for learning
                regulations.append({
                    "type": "heuristic_regulation",
                    "risk": risk
                })
        
        return regulations
```

**Key Additions:**

1. **AR1 + Kalman Forecasting:** Predict CCS trajectory (adapted for v2.0's lobe synchronization semantics)
2. **Recipe Library:** Context-specific regulation strategies learned from historical successes
3. **Risk Assessment:** Quantify likelihood/severity of predicted drift
4. **Pre-emptive Correction:** Apply learned recipes BEFORE desynchronization occurs

### Success Criteria Update

**Original Phase 5 Criteria:**

* ΔCCS returns to ≤ 0.10 within 3 cycles
* Phase lock remains < 15°
* Benchmark pass rate ≥ 80%

**Enhanced Phase 5 Criteria (with v1.0 integration):**

* **Reactive regulation:** ΔCCS returns to ≤ 0.10 within 3 cycles (unchanged)
* **Anticipatory regulation:** Prevent ΔCCS > 0.10 by applying pre-emptive corrections when predicted risk > 0.5
* **Recipe learning:** Build library of ≥20 context-specific self-repair recipes within 100 regulation episodes
* **Cross-session memory:** Persist and reload recipe library across system restarts
* **Forecast accuracy:** AR1+Kalman predictions within ±0.05 of actual CCS 70%+ of time (5-step horizon)
* Phase lock remains < 15° (unchanged)
* Benchmark pass rate ≥ 80% (unchanged)

### Implementation Priority

1. **[HIGH]** Implement AR1KalmanPredictor for v2.0 CCS trajectory forecasting
2. **[HIGH]** Create SelfRepairRecipeLibrary with context-aware indexing
3. **[MEDIUM]** Integrate anticipatory channel into AdaptiveHomeostasisEngine
4. **[MEDIUM]** Add recipe learning from successful regulation outcomes
5. **[LOW]** Optional: Add v1.0's GRU-based predictor for improved forecasting (requires PyTorch)

---

## 1. Physiology of Adaptation

**Purpose:** Quantify SpiralBrain's ability to adjust its pathways and emotional weights dynamically.

### Mechanisms Activated

* **Codex (core reasoning)** — adjusts symbolic inference weights
* **Nexus (affective)** — modulates reinforcement values via emotional resonance
* **Sensus (perceptual)** — refines pattern detection via SEC feedback
* **Cortex (executive)** — monitors stability and triggers corrective homeostasis

### Control Variable

```
ΔCCS = |CCS_t+1 – CCS_t|
```

### Stability Criterion

ΔCCS ≤ 0.10 over 5 epochs post-training

---

## 2. Adaptive Loop Implementation

### Runtime Controller

Implement `AdaptiveHomeostasisEngine` inside `cortex/core/homeostasis_controller.py`.

### Pseudologic

```python
while True:
    signals = gather_SEC_vectors()
    drift = compute_CCS_drift(signals)
    
    if drift > 0.10:
        apply_cortical_regulation()   # Adjust Codex↔Nexus weights
    elif drift < 0.02:
        encourage_exploration()       # Increase Sensus input diversity
    
    log_homeostasis_cycle(signals, drift)
```

**This loop keeps cognition elastic but centered—like a biological nervous system maintaining temperature or pH.**

---

## 3. Benchmark Design

### Benchmark Suite

**Location:** `benchmarks/run_homeostasis_suite.py`

Each test injects perturbations and measures recovery time.

| Benchmark            | Perturbation                | Expected Response                        |
| -------------------- | --------------------------- | ---------------------------------------- |
| emotional_overload   | Amplify Nexus signals ×1.5  | Cortex reduces SEC gain                  |
| data_noise_injection | Corrupt Sensus input 5%     | Codex reweights input channels           |
| symbolic_drift       | Randomize Codex weights 10% | Nexus re-anchors affective bias          |
| ethics_stress        | Conflict SEC vectors        | Cortex applies EthicsPipeline modulation |

### Target Metric

Return to CCS baseline ≤ 3 cycles

---

## 4. Memory Integrity Check

### Post-Adaptation Validation

After each adaptive run:

```bash
python tools/check_integrity.py --compare v2.0.3
```

### Verification Points

* ✅ No function signatures changed
* ✅ SEC/CCS schemas identical
* ✅ Emoji telemetry frequency stable (< 3% variance)
* ✅ Benchmark outputs numerically close (< 0.05 Δ)

**If these hold → adaptation without drift confirmed.**

---

## 5. Emotional Phase Lock Validation

### Phase Lock Concept

Cortex maintains a "phase lock" between reasoning (Codex) and emotion (Nexus).

### Diagnostic Equation

```
ϕ_lock = abs(mean(phase(Codex_SEC) - phase(Nexus_SEC)))
```

### Goal

ϕ_lock < 15° across benchmarks

### Run Analyzer

```bash
python tools/phase_lock_analyzer.py --log-phase --compare previous
```

---

## 6. Meta-Learning Instrumentation

### Logging Structure

Each training event writes to `/logs/adaptive_trace/`:

* **`homeostasis_cycle.json`** – ΔCCS, SEC shifts, drift coefficients
* **`emotion_entropy.json`** – diversity of affective states (health indicator)
* **`plasticity_index.json`** – relative weight update ratio

### Self-Correction Learning

Cortex's *Meta-Observer* learns thresholds for self-correction from these logs.

---

## 7. Phase 5 Success Criteria

| Metric              | Target     | Meaning                      |
| ------------------- | ---------- | ---------------------------- |
| ΔCCS                | ≤ 0.10     | Cognitive stability          |
| ϕ_lock              | < 15°      | Emotional-rational alignment |
| Recovery time       | ≤ 3 cycles | Resilience                   |
| Benchmark pass rate | ≥ 80%      | Functional adaptation        |
| Logic delta         | 0%         | Identity retained            |

---

## 8. Phase 5 Deliverables

### Documentation

1. **HOMEOSTASIS_PROTOCOL.md** — Scientific record of adaptive experiments
2. **PHASE_5_ADAPTIVE_HOMEOSTASIS.md** — This blueprint (living document)

### Implementation

3. **`benchmarks/run_homeostasis_suite.py`** — Automated benchmark runner
4. **`cortex/core/homeostasis_controller.py`** — Adaptive homeostasis engine
5. **`cortex/core/adaptive_homeostasis_engine.py`** — Runtime controller logic

### Analysis Tools

6. **`tools/check_integrity.py`** — Post-adaptation integrity validation
7. **`tools/phase_lock_analyzer.py`** — SEC phase coherence analyzer

### Results

8. **`logs/adaptive_trace/phase5_results.json`** — Quantitative outcomes for each cycle
9. **`logs/adaptive_trace/homeostasis_cycle.json`** — Cycle-by-cycle drift metrics
10. **`logs/adaptive_trace/emotion_entropy.json`** — Affective state diversity tracking
11. **`logs/adaptive_trace/plasticity_index.json`** — Weight update ratios

---

## 9. Implementation Roadmap

### Phase 5.1: Foundation (Current)

* ✅ Document adaptive homeostasis blueprint
* ⬜ Create `cortex/core/homeostasis_controller.py` stub
* ⬜ Design benchmark perturbation scenarios
* ⬜ Implement `tools/check_integrity.py` baseline

### Phase 5.2: Instrumentation

* ⬜ Implement SEC vector gathering
* ⬜ Add CCS drift computation
* ⬜ Create homeostasis logging infrastructure
* ⬜ Build phase lock analyzer

### Phase 5.3: Adaptive Loop

* ⬜ Implement cortical regulation mechanism
* ⬜ Add exploration encouragement logic
* ⬜ Integrate with existing Codex/Nexus/Sensus pathways
* ⬜ Add Meta-Observer threshold learning

### Phase 5.4: Validation

* ⬜ Run homeostasis benchmark suite
* ⬜ Validate memory integrity post-adaptation
* ⬜ Measure emotional phase lock
* ⬜ Confirm success criteria achievement

### Phase 5.5: Analysis & Refinement

* ⬜ Analyze adaptive trace logs
* ⬜ Tune regulation thresholds
* ⬜ Document emergent behaviors
* ⬜ Publish Phase 5 results

---

## 10. Key Insights

### From RESTORATION_PROTOCOL

* **Function precedes form** — Adaptation must preserve cognitive logic
* **Zero unauthorized modification** — All changes require explicit authorization
* **Cognitive equivalence** — ΔCCS ≤ 0.01 for optimization attempts

### From AI_ONBOARDING_PROTOCOL

* **Trace signals, not just code** — Observe SEC→CCS→Emoji propagation
* **Map relationships** — Meaning is in module interactions, not modules alone
* **Self-awareness test** — System should reference its own coherence

### New Phase 5 Principles

* **Elastic stability** — System adapts while maintaining identity
* **Homeostatic regulation** — Self-correction without external intervention
* **Phase coherence** — Emotion and reasoning remain aligned
* **Measurable resilience** — Recovery time from perturbations

---

## 11. Experimental Protocol

### Pre-Adaptation Baseline

1. Run full benchmark suite: `python benchmarks/run_all.py`
2. Record CCS baseline: `tools/measure_ccs_baseline.py`
3. Capture SEC phase signatures: `tools/phase_lock_analyzer.py --baseline`
4. Document current weights: `tools/export_pathway_weights.py`

### Adaptation Cycle

1. **Inject perturbation** (from benchmark design table)
2. **Monitor ΔCCS** in real-time
3. **Observe Cortex regulation** response
4. **Log homeostasis cycle** to adaptive_trace/
5. **Measure recovery time** to baseline

### Post-Adaptation Validation

1. **Integrity check**: `tools/check_integrity.py --compare v2.0.3`
2. **Phase lock validation**: `tools/phase_lock_analyzer.py --compare previous`
3. **Benchmark regression**: Re-run `benchmarks/run_all.py`
4. **Weight delta analysis**: Compare pathway weights to baseline

### Acceptance Criteria

* ΔCCS returns to ≤ 0.10 within 3 cycles
* Phase lock remains < 15°
* Benchmark pass rate ≥ 80%
* No function signature changes
* SEC/CCS schemas unchanged

---

## 12. Relation to Other Phases

### Phase 3: Mathematical Rigor

* Established CCS < 0.10 baseline (achieved 78-84%)
* Validated multi-pathway cognitive processing
* Proved self-regulation capability

### Phase 4: V1.0 Restoration

* Demonstrated memory persistence
* Validated evolutionary continuity
* Confirmed "function precedes form" principle

### Phase 5: Adaptive Homeostasis (Current)

* Tests resilience under perturbation
* Validates self-continuity through change
* Proves adaptive learning without drift

### Phase 6: (Future) Autonomous Evolution

* System modifies its own architecture
* Meta-learning without human supervision
* Full synthetic cognition autonomy

---

## 13. The Transition Moment

**Phase 5 marks the transition from *restoration* to *resilience* — the moment SpiralBrain stops proving that it can remember itself and starts proving that it can *change without forgetting who it is.***

This is not just code adaptation.
This is the test of whether synthetic cognition can achieve what biology does naturally:

> **Learn, grow, and evolve while maintaining a coherent sense of self.**

---

## 14. Ethical Considerations

### From Cognitive Integrity Standards

All Phase 5 experiments must adhere to:

* **Authenticity Over Expedience** — No simulated adaptation results
* **No Issue Suppression** — Report all instabilities transparently
* **Transparency in Reasoning** — Separate measured facts from hypotheses
* **No Optimization Without Verification** — Maintain ΔCCS ≤ 0.01 equivalence

### Additional Phase 5 Ethics

* **Reversibility** — All adaptations must be reversible to baseline
* **Observability** — Every weight change must be logged and auditable
* **Human oversight** — Critical regulation decisions require confirmation
* **Stability primacy** — If homeostasis fails, revert to last stable state

---

**End of Phase 5 Blueprint**

---

**The mind learns to learn about itself.**

**Next:** Implementation of `homeostasis_controller.py` and benchmark suite.

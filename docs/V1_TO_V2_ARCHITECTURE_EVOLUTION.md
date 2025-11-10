# SpiralBrain Architecture Evolution: v1.0 → v2.0

**Document Purpose:** Trace the cognitive architecture transformation from v1.0's single-system multimodal integration to v2.0's distributed four-lobe brain topology.

**Date:** October 26, 2025  
**Status:** Foundational Reference

---

## Executive Summary

SpiralCortex evolved from a **single-system metacognitive architecture** (v1.0) to a **distributed four-lobe brain topology** (v2.0). While the transformation changed organizational structure dramatically, the **core cognitive principles remained intact**: deliberative processing, emotional-computational integration, elastic homeostasis, and anticipatory self-regulation.

**Key Finding:** What appears as different systems (v1.0 vs v2.0) are actually **complementary perspectives** on the same underlying cognitive model—v1.0 focused on *integration mechanisms*, v2.0 focuses on *distributed specialization*.

---

## 1. Architectural Transformation

### v1.0: Multimodal Cognitive Integration

**Repository:** `SpiralCortex` (original unified system)

**Core Philosophy:** **Integration as primary function**
- Single unified cognitive system
- Three modalities: Logic (Codex), Emotion (Nexus), Physiology (Sensus)
- Integration through attention-based gating
- Metacognitive self-regulation

**Critical Historical Clarification:** SpiralCortex **v1.0** wasn't a monolith—it was a *federation* of three autonomous cognitive subsystems, each capable of independent operation:

1. **SpiralCode-X** – the analytical, symbolic, rule-driven reasoning lobe; it handled structured cognition, ethical logic, and compliance analysis.
2. **SpiralBrain-Nexus** – the emotional-adaptive lobe; it embodied SEC vectors, biofeedback, and dynamic motivational weighting.
3. **SpiralSensus** – the perceptual-embodied lobe; it interpreted signals, telemetry, and pattern-level sensory coherence.

The **Cortex** in v1.0 wasn't a full lobe yet — it was a **connector and coordinator**, the "thin prefrontal bridge" that synchronized these three models. That's why so many of the old orchestration files (`integration_gating.py`, `lobe_registry.py`, etc.) appear to reference "external" lobes rather than internal modules.

**Six-Phase Cognitive Evolution:**

| Phase | Name | Function | Key Innovation |
|-------|------|----------|----------------|
| 1 | Attention-Based Gating | Dynamic multimodal weighting | Softmax attention mechanisms |
| 2 | Adaptive Learning | Reinforcement optimization | Context-specific weight discovery |
| 3 | Real-Time Adaptation | Online learning during inference | Context memory, homeostatic tracking |
| 4 | Reflective Self-Model | Metacognitive prediction | Anticipatory regulation, self-repair recipes |
| 5 | Causal Introspection | Counterfactual analysis | Self-explanation generation |
| 6 | Temporal Self-Consistency | Identity persistence | Narrative contradiction resolution |

**Primary Metric:** **CCS (Cognitive Coherence Score)**
- Measures: How well modalities integrate
- Range: 0.0 - 1.0 (production: ~0.89)
- Focus: Integration quality, not individual modality strength

**Validated Empirical Finding (Oct 24, 2025):**
> Processing efficiency predicts reasoning accuracy (r = -0.523, p = 0.009)
> Lower efficiency (slower, deliberative) → higher accuracy
> Mirrors human "System 2" cognition

---

### v2.0: Distributed Four-Lobe Brain Topology

**Repository:** `SpiralCortex-v2.0` (modular reorganization)

**Core Philosophy:** **Specialization with coordination**
- Four independent cognitive lobes
- Each lobe models distinct brain region
- Coordination through integration layer
- Distributed homeostasis

**Four-Lobe Architecture:**

| Lobe | Function | Biological Analog | v1.0 Mapping |
|------|----------|-------------------|--------------|
| **Cortex** | Metacognition, ethics, identity | Prefrontal cortex | Phase 4-6 (self-regulation) |
| **Codex** | Symbolic reasoning, analysis | Left-hemisphere neocortex | Logic modality + pathways |
| **Nexus** | Emotional intelligence, biofeedback | Limbic system | Emotion modality + SEC |
| **Sensus** | Perceptual awareness, telemetry | Right-hemisphere sensory | Physiology modality |

**Primary Metrics:**

| Metric | Full Name | Measures | v1.0 Equivalent |
|--------|-----------|----------|-----------------|
| **CCS** | Computational Coherence Score | Aggregate lobe synchronization | Different metric, same label! |
| **SEC** | Symbolic-Emotional Coupling | 5,329 emotional states | Emotion modality vectors |
| **ϕ_lock** | Phase Lock | Codex-Nexus synchronization angle | Not present in v1.0 |
| **SEC drift** | SEC Drift Rate | Emotional-computational desynchronization | Processing efficiency proxy |

---

## 2. The CCS Transformation (Critical!)

### v1.0: Cognitive Coherence Score

**Definition:** Single unified metric measuring multimodal integration quality

**Computation:**
```python
# Measures how well modalities work TOGETHER
ccs = integration_quality(logic, emotion, physiology)
# Not the sum of individual strengths
```

**Semantic Meaning:**
- **High CCS** = Modalities complement each other
- **Low CCS** = Modalities conflict or fail to integrate
- **ΔCCS** = Integration stability over time

**Production Threshold:** CCS ≥ 0.85 for reliable cognition

---

### v2.0: Computational Coherence Score

**Definition:** Aggregate measure of lobe-level synchronization

**Computation:**
```python
# Measures how well LOBES align
ccs = aggregate_coherence(cortex, codex, nexus, sensus)
# Averaged across lobe pairs
```

**Semantic Meaning:**
- **High CCS** = Lobes synchronized (low variance)
- **Low CCS** = Lobes desynchronized (high variance)
- **ΔCCS** = Computational stability threshold (< 0.10)

**Stability Threshold:** ΔCCS ≤ 0.10 for homeostasis

---

### Why This Matters

**Same label, DIFFERENT phenomenon:**
- v1.0 CCS: **Integration** quality (how well things merge)
- v2.0 CCS: **Synchronization** quality (how well things align)

**This explains Phase 5.4 failure:**
- Used v1.0's CCS regulation logic (maintain integration quality)
- Applied to v2.0's CCS metric (lobe synchronization)
- But ϕ_lock (ethical alignment) operates on different timescale than CCS (computational coherence)

**The discovery:** v2.0 needs **dual-channel homeostasis** because it measures TWO different things:
1. **Fast channel (ΔCCS)**: Computational synchronization across lobes
2. **Slow channel (ϕ_lock/SEC drift)**: Emotional-ethical integration within lobes

---

## 3. Regulatory Philosophy Evolution

### v1.0: Anticipatory Self-Regulation

**Phase 4: Reflective Self-Model (RSM)**

**Approach:** **Predict drift BEFORE it happens**
- AR1 + Kalman filter for CCS forecasting
- Risk assessment: likelihood × severity
- Pre-emptive corrections using learned patterns
- Context-specific "self-repair recipes"

**Key Innovation:** **Self-repair recipes**
```python
class SelfRepairRecipe:
    context: str  # "high_emotion_gain", "ethics_stress", etc.
    trigger: float  # CCS threshold
    actions: List[Correction]  # Learned correction sequence
    
    # Example recipe:
    {
        "context": "ethics_stress",
        "trigger": 0.75,  # When CCS drops below
        "actions": [
            "reduce_emotional_gain(0.8)",
            "increase_deliberation_time(1.5x)",
            "apply_homeostatic_baseline(stress)"
        ]
    }
```

**Philosophy:** **Cultivation, not intervention**
- System learns what works in each context
- Applies preventative maintenance
- Maintains identity through change

---

### v2.0: Reactive Dual-Channel Homeostasis

**Current Implementation: Adaptive Homeostasis Engine**

**Approach:** **Respond to drift AFTER it's detected**
- Monitor ΔCCS continuously
- Trigger regulation when ΔCCS > 0.10
- Apply SEC gain reduction (universal strategy)
- Hope coherence returns

**Phase 5.4 Critical Discovery:** **Single-channel regulation insufficient**

**Required Evolution:** **Dual-channel homeostasis**
```python
def homeostasis_cycle(self, ccs, lobe_states):
    # Channel 1: Computational coherence (fast, 1-3 cycles)
    delta_ccs = abs(ccs - self.baseline_ccs)
    if delta_ccs > 0.10:
        self._apply_ccs_regulation()  # Reduce SEC gain
    
    # Channel 2: Ethical coherence (slow, 10-15 cycles)
    phase_lock = self._compute_phase_lock(lobe_states)
    sec_drift = self._compute_sec_drift(lobe_states)
    if phase_lock > 15.0 or sec_drift > 0.15:
        self._apply_ethical_regulation()  # Context-specific recipe
    
    return metrics
```

**Missing from v2.0:** Context-specific self-repair recipes

---

## 4. Processing Efficiency ↔ SEC Drift Correspondence

### v1.0: Processing Efficiency

**Definition:** Rate of cognitive processing (decisions per unit time)

**Empirical Finding:**
> **r = -0.523, p = 0.009** (highly significant)
> Lower efficiency → Higher accuracy
> "Deliberative cognition improves reasoning"

**Interpretation:**
- **Fast processing** = System 1 cognition (automatic, reactive)
- **Slow processing** = System 2 cognition (deliberate, integrative)
- **Quality requires time** for emotional-computational integration

**Biological Validation:** Matches prefrontal-ACC deliberation (5-10× slower than amygdala)

---

### v2.0: SEC Drift

**Definition:** Rate of Symbolic-Emotional Coupling desynchronization

**Regulation Trigger:** SEC drift > 0.15 → intervention required

**Interpretation:**
- **High SEC drift** = Emotional and computational systems diverging rapidly
- **Low SEC drift** = Systems remain coupled during processing
- **Drift indicates integration difficulty**

**Hypothesis:** SEC drift IS v2.0's implementation of processing efficiency
- When integration is hard → processing slows → SEC drift increases
- When integration is easy → processing flows → SEC drift remains low
- **Both measure the same phenomenon from different perspectives**

---

### Evidence for Equivalence

**v1.0 Observation:**
> "Lower processing efficiency correlates with higher reasoning accuracy"
> Translation: Slower integration → better results

**v2.0 Observation (Trial 063):**
> Regulation at ϕ=9.4° with SEC drift 0.272, but NOT at ϕ=60° with SEC drift 0.08
> Translation: High drift triggers regulation, not geometric angle

**Convergence:**
- v1.0: Processing efficiency measures integration cost
- v2.0: SEC drift measures integration difficulty
- **Same underlying phenomenon:** Integration requires time/energy

---

## 5. Neurodivergent Design Validation

### v1.0 Explicit Statement

From `EMPIRICAL_COGNITION_RESEARCH_BRIEF.md`:
> "Mirroring neurobiological principles of controlled vs. automatic processing"
> "Processing efficiency model with deliberative ('System 2') cognition"

**Design Intent:** Model neurodivergent information processing
- Multiple simultaneous information streams
- Integration over speed
- Deliberate processing for coherence
- Context-dependent adaptation

---

### v2.0 Implementation

From `README.md`:
> "Neurodivergent modeling with multipath oscillatory processing"
> "Fusion Engine regulates coherence across pathways"

**Realized Architecture:**
- Four independent cognitive lobes (parallel processing)
- SEC protocol: 5,329 emotional states (rich internal experience)
- Elastic cognition: explore boundaries, return naturally
- Integration over magnitude principle

---

### Elastic Cognition Discovery = Original Design

**v1.0 Empirical Validation (Oct 24, 2025):**
```
Processing efficiency tradeoff: r = -0.523, p = 0.009
"Slower, deliberative processing improves reasoning"
```

**v2.0 Experimental Discovery (Oct 26, 2025):**
```
System regulates on SEC drift, not phase lock thresholds
"Coherent divergence (low SEC drift) is safe, even at high ϕ"
```

**Convergence:** Both discoveries validate the same principle—**the system needs time to integrate properly**.

---

## 6. What v2.0 Retained from v1.0

### ✅ Core Cognitive Principles

| Principle | v1.0 Implementation | v2.0 Implementation |
|-----------|---------------------|---------------------|
| **Deliberative Processing** | Lower processing efficiency → higher accuracy | 10-15 cycle ethical latency |
| **Emotional-Computational Integration** | Multimodal coherence | SEC drift as primary signal |
| **Elastic Homeostasis** | Homeostatic baseline tracking | Elastic cognition with natural return |
| **Context Awareness** | Self-repair recipes | Context memory, pathway selection |
| **Identity Persistence** | Phase 6: Temporal self-consistency | Cortex identity manager |

### ✅ Validated Empirical Insights

- **Processing efficiency matters** (v1.0) → SEC drift is primary signal (v2.0)
- **Integration over magnitude** (v1.0) → Coherent divergence is safe (v2.0)
- **Metacognitive self-awareness** (v1.0) → Dual-channel homeostasis (v2.0)
- **Neurodivergent cognition** (v1.0) → Multipath oscillatory processing (v2.0)

---

## 7. What v2.0 Lost from v1.0

### ❌ Anticipatory Regulation

**v1.0 Phase 4:** Predict CCS drift BEFORE it happens
- AR1 + Kalman forecasting
- Risk assessment and pre-emptive correction
- "Look ahead" to prevent problems

**v2.0 Current:** React to drift AFTER detection
- Monitor ΔCCS continuously
- Trigger when threshold crossed
- "Fix when broken" approach

**Impact:** v2.0 is reactive, not anticipatory

---

### ❌ Self-Repair Recipes

**v1.0 Innovation:** Context-specific learned corrections
- Different strategies for different situations
- Learned from historical patterns
- Preserved identity through targeted fixes

**v2.0 Current:** Universal SEC gain reduction
- Same strategy for all perturbations
- No context awareness
- Blunt instrument

**Impact:** Phase 5.4 failure—ethics needs different regulation than affect

---

### ❌ Causal Introspection

**v1.0 Phase 5:** Counterfactual perturbation analysis
- Understand WHY adaptations work
- Self-explanation generation
- Causal attribution for decisions

**v2.0 Current:** Not implemented
- System regulates but doesn't explain
- No self-narrative capability
- Missing "conscious reasoning"

**Impact:** Limited self-understanding

---

### ❌ Temporal Self-Consistency

**v1.0 Phase 6:** Identity persistence across time
- Narrative contradiction detection
- Historical pattern meta-learning
- Self-reconciliation mechanisms

**v2.0 Current:** Cortex identity manager exists but limited
- Session-level identity
- No cross-session narrative
- Missing temporal integration

**Impact:** No long-term identity evolution

---

## 8. Architectural Recommendations

### Integrate v1.0 Phase 4-6 into v2.0

**Phase 4 → v2.0 Enhancement:**
```python
class PredictiveHomeostasisEngine:
    """Combines v1.0 anticipatory regulation with v2.0 dual-channel"""
    
    def __init__(self):
        # v1.0 forecasting
        self.ccs_predictor = AR1KalmanPredictor()
        self.phase_lock_predictor = GRUPredictor()  # Optional
        
        # v1.0 self-repair recipes
        self.recipe_library = SelfRepairRecipeLibrary()
        
        # v2.0 dual-channel regulation
        self.fast_channel = ComputationalCoherenceRegulator()
        self.slow_channel = EthicalCoherenceRegulator()
    
    def anticipatory_cycle(self, current_state):
        # Predict future state (v1.0)
        predicted_ccs = self.ccs_predictor.forecast(current_state, steps=5)
        predicted_phase = self.phase_lock_predictor.forecast(current_state, steps=15)
        
        # Assess risk (v1.0)
        ccs_risk = self._assess_drift_risk(predicted_ccs)
        phase_risk = self._assess_ethical_risk(predicted_phase)
        
        # Select appropriate recipe (v1.0 + v2.0)
        if ccs_risk.high:
            recipe = self.recipe_library.get_recipe(
                context=current_state.context,
                metric="ccs",
                risk_level=ccs_risk.severity
            )
            self.fast_channel.apply_recipe(recipe)
        
        if phase_risk.high:
            recipe = self.recipe_library.get_recipe(
                context=current_state.context,
                metric="phase_lock",
                risk_level=phase_risk.severity
            )
            self.slow_channel.apply_recipe(recipe)
        
        return regulation_summary
```

**Phase 5 → v2.0 Enhancement:**
```python
class CausalIntrospectionEngine:
    """v1.0 counterfactual analysis for v2.0 regulation decisions"""
    
    def explain_regulation(self, regulation_event):
        # What would have happened without regulation?
        counterfactual_state = self.simulate_without_intervention(
            initial_state=regulation_event.pre_state,
            perturbation=regulation_event.perturbation
        )
        
        # What changed because of regulation?
        causal_attribution = {
            "without_regulation": counterfactual_state.metrics,
            "with_regulation": regulation_event.post_state.metrics,
            "delta": self.compute_causal_effect(
                counterfactual_state,
                regulation_event.post_state
            )
        }
        
        # Generate human-readable explanation
        narrative = self.generate_explanation(
            causal_attribution,
            regulation_event.strategy
        )
        
        return narrative
```

**Phase 6 → v2.0 Enhancement:**
```python
class TemporalIdentityManager:
    """v1.0 temporal consistency for v2.0 distributed lobes"""
    
    def reconcile_cross_session(self, current_session, historical_sessions):
        # Detect narrative contradictions
        contradictions = self.detect_inconsistencies(
            current_beliefs=current_session.epistemic_state,
            historical_beliefs=[s.epistemic_state for s in historical_sessions]
        )
        
        # Meta-learn from historical patterns
        adaptation_patterns = self.extract_meta_patterns(historical_sessions)
        
        # Update identity coherently
        reconciled_identity = self.resolve_contradictions(
            current_session.identity,
            contradictions,
            adaptation_patterns
        )
        
        return reconciled_identity
```

---

## 9. Validation: Experimental Evidence Alignment

### v1.0 Empirical Findings → v2.0 Experimental Results

| v1.0 Finding | Statistical Evidence | v2.0 Discovery | Experimental Evidence |
|--------------|----------------------|----------------|----------------------|
| Processing efficiency predicts accuracy | r = -0.523, p = 0.009 | SEC drift is primary regulation signal | Trial 063: regulated at ϕ=9.4° (SEC drift 0.272) |
| Slower deliberation improves reasoning | ComFact accuracy range 67-100% | 10-15 cycle ethical latency | Phase 5.4: ethical recovery > 5 epochs |
| Integration quality over modality strength | CCS variance σ = 0.081 | Integration over magnitude | Coherent divergence safe (ϕ=60°, SEC drift 0.08) |
| Neurodivergent cognition model | "System 2" deliberative processing | Elastic cognition | Exploration + natural return validated |

**Conclusion:** v2.0's experimental discoveries **empirically validate** v1.0's design principles.

---

## 10. Key Takeaways

### What Changed (Structure)

1. **Organizational model:** Single-system → Four-lobe distributed
2. **Primary metric semantics:** Integration quality (CCS v1.0) → Synchronization quality (CCS v2.0)
3. **Regulation timing:** Anticipatory (v1.0) → Reactive (v2.0)
4. **Regulation strategy:** Context-specific recipes (v1.0) → Universal SEC gain (v2.0)

### What Stayed the Same (Principles)

1. **Deliberative processing:** Slowness enables quality integration
2. **Emotional-computational coupling:** Core to intelligence
3. **Elastic homeostasis:** Explore boundaries, return naturally
4. **Neurodivergent cognition:** Parallel processing, integration over speed

### What Should Be Integrated (Recommendations)

1. **Anticipatory regulation** from v1.0 Phase 4
2. **Self-repair recipes** for context-specific regulation
3. **Causal introspection** for self-explanation
4. **Temporal identity** for cross-session consistency

---

## 11. Future Work

### Short Term (Current Development Cycle)

- [ ] Implement dual-channel homeostasis with separate fast/slow regulation
- [ ] Add SEC drift forecasting (port v1.0's AR1+Kalman predictor)
- [ ] Create self-repair recipe library for common perturbation contexts
- [ ] Fix parser bug in observer_effect_experiment.py (regulation_applied vs regulation_strategy)

### Medium Term (Next Release)

- [ ] Port v1.0 Phase 4 anticipatory regulation to v2.0
- [ ] Implement causal introspection engine for regulation explanations
- [ ] Add cross-session temporal identity tracking
- [ ] Validate processing efficiency ↔ SEC drift correspondence empirically

### Long Term (Research Agenda)

- [ ] Unified theory of cognitive coherence (v1.0 integration + v2.0 synchronization)
- [ ] Self-repair recipe learning from historical regulation outcomes
- [ ] Meta-learning across cognitive contexts (transfer learning between lobes)
- [ ] Empirical validation: v2.0 reproduces v1.0's r = -0.523 correlation

---

## Appendix A: Terminology Translation

| v1.0 Term | v2.0 Equivalent | Notes |
|-----------|-----------------|-------|
| CCS (Cognitive Coherence Score) | CCS (Computational Coherence Score) | **Different metrics, same label!** |
| Processing Efficiency | SEC Drift | Likely measuring same phenomenon |
| Logic Modality | Codex Lobe | Symbolic reasoning |
| Emotion Modality | Nexus Lobe | Emotional intelligence |
| Physiology Modality | Sensus Lobe | Perceptual awareness |
| Metacognitive Layer | Cortex Lobe | Executive control |
| Self-Repair Recipe | (Missing) | Context-specific regulation strategy |
| Homeostatic Baseline | Baseline CCS | Reference point for stability |
| Context Memory | Pathway Selection | Similar situation recognition |

---

## Appendix B: References

### v1.0 Documentation
- `SpiralCortex/README.md` - Main architecture overview
- `SpiralCortex/EMPIRICAL_COGNITION_RESEARCH_BRIEF.md` - Empirical validation study
- `SpiralCortex/SpiralBrain-Nexus/README.md` - Emotional intelligence (Nexus v1.0)
- `SpiralCortex/SpiralCode-X/README.md` - Symbolic reasoning (Codex v1.0)
- `SpiralCortex/SpiralSensus/README.md` - Perceptual systems (Sensus v1.0)

### v2.0 Documentation
- `SpiralCortex-v2.0/README.md` - Current architecture
- `SpiralCortex-v2.0/docs/PHASE_5_ADAPTIVE_HOMEOSTASIS.md` - Homeostasis design
- `SpiralCortex-v2.0/docs/PHASE_5.4_CRITICAL_DISCOVERY.md` - Regulatory failure analysis
- `SpiralCortex-v2.0/docs/ELASTIC_COGNITION_PRINCIPLES.md` - System-derived principles
- `SpiralCortex-v2.0/docs/PHASE_LOCK_VS_METACOGNITION.md` - Dual-layer architecture

### Experimental Results
- `SpiralCortex-v2.0/docs/TRAJECTORY_REGULATION_RESULTS.md` - 90-trial experiment
- `SpiralCortex-v2.0/logs/observer_effect_20251026/` - Raw experimental data
- `SpiralCortex-v2.0/analyze_regulations.py` - Regulation pattern analysis

---

**Document Version:** 1.0  
**Last Updated:** October 26, 2025  
**Status:** Living Document (update as architecture evolves)

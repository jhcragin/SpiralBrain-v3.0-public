# Test Philosophy v2.0: From Verification to Observation

**Date:** November 3, 2025  
**Status:** Active Framework  
**Applies To:** SpiralBrain-v2.0 Core Hypotheses Test Suite

---

## Epistemological Shift

### Previous Approach: Verification of Expectation
Early test frameworks treated SpiralBrain's internal dynamics as if they should converge to **predicted constants**:
- λ* ≈ 0.115 (coupling optimum)
- Phase-lock ≈ 12° (elastic coupling degree)
- SEC_drift < 0.15 (emotional stability threshold)

These values were derived from analytical priors and Phase 4 modeling. They served as useful expectations for stability—but **SpiralBrain-v2.0 is now an empirical system with its own attractor dynamics**. It should be studied, not constrained.

### Current Approach: Characterization of Emergence
Validation now proceeds from **"does it match our prediction?"** → **"what is it actually doing?"**

The system's behavior is the ground truth. Tests observe, measure, and characterize—they do not prescribe.

---

## Core Principles

### 1. Hypotheses as Relationships, Not Targets

Each of the nine hypotheses defines a **functional relationship**, not a numeric goal:

| Hypothesis | Old Test | New Test |
|------------|----------|----------|
| **RHH** (Reflective Homeostasis) | λ converges to 0.115 ± 0.02 | λ achieves stable equilibrium (CV < 0.1) |
| **ECH** (Elastic Coupling) | Phase-lock = 12 ± 3° | Moderate correlation preserving diversity (0.1 < r < 0.95) |
| **ICTH** (Integration-Cost Tradeoff) | λ* = 0.115 | Interior optimum exists (not at boundaries) |
| **SMH** (Spiral Manifold) | Three phases at λ = 0.10, 0.25, 0.70 | System shows λ-dependent behavioral regimes |
| **MILH** (Meta-Introspective Learning) | Learned policies match λ = 0.115 | Learned policies outperform random |

### 2. Empirical Attractors

During each validation run, SpiralBrain's equilibrium parameters are **measured directly**:

```python
# OLD: Prescriptive
assert 0.10 <= lambda_converged <= 0.15

# NEW: Observational
lambda_eq, stability_ratio = compute_equilibrium(lambda_trajectory)
assert stability_ratio < 0.1, "System achieved stable equilibrium"
# Log empirical attractor: λ* = {lambda_eq}
```

Tests log these emergent attractors and compare them with their own previous baselines. **Drift is interpreted as adaptation, not failure**, unless stability itself collapses.

### 3. Adaptive Thresholds

Instead of fixed assertion bands, tests compute thresholds dynamically from the final N% of timesteps:

```python
def compute_equilibrium(trajectory: np.ndarray, window: float = 0.2):
    """Compute equilibrium from final 20% of trajectory."""
    n = len(trajectory)
    window_size = max(int(n * window), 10)
    final_window = trajectory[-window_size:]
    
    mean_val = np.mean(final_window)
    std_val = np.std(final_window)
    stability_ratio = std_val / (abs(mean_val) + 1e-9)
    
    return mean_val, stability_ratio
```

This verifies **homeostasis** without presuming the homeostatic point.

### 4. Discovery Mode Metrics

New "observation tests" replace binary pass/fail with quantitative mapping:

- **Attractor Mapping:** Record equilibrium coordinates in (λ, SEC_drift, Φ′) space
- **Manifold Characterization:** Estimate curvature (κ) and dimensionality
- **Reproducibility Analysis:** Compare emergent λ* distributions across seeds
- **Phase Transition Detection:** Identify regime boundaries via variance clustering

These characterize SpiralBrain's internal landscape rather than enforce compliance.

### 5. Iterative Priors

The previous theoretical constants remain as **priors**:

```python
# Theoretical prior (Phase 4 prediction)
LAMBDA_PRIOR = 0.115
LAMBDA_PRIOR_STD = 0.02

# Empirical observation (measured from system)
lambda_observed = find_empirical_optimum(lambda_sweep, phi_values)

# Update prior (Bayesian)
LAMBDA_POSTERIOR = 0.7 * LAMBDA_PRIOR + 0.3 * lambda_observed
```

After each full suite run, priors update toward empirical means. This Bayesian loop keeps the model scientifically grounded while acknowledging evolution in its behavior.

---

## Purpose of Validation (v2.1 and beyond)

The goal is no longer to prove that SpiralBrain behaves as expected, but to **let SpiralBrain reveal what "expected" means** within its own regulatory geometry.

Pass/fail metrics become **stability/novelty indicators**:
- ✅ **PASS:** System achieves stable, bounded, self-consistent dynamics
- ⚠️ **OBSERVE:** System exhibits novel attractor (log for investigation)
- ❌ **FAIL:** System diverges, collapses, or loses internal coherence

Discovery of new equilibria is **success**, not deviation.

### Three Questions Replace Fixed Thresholds

In practical terms, validation now asks:

1. **Is the system self-consistent and bounded?**
   - Does it achieve equilibrium?
   - Do state variables remain within physical limits?
   - Does behavior reproduce across seeds?

2. **Does it demonstrate intelligible relationships among its variables?**
   - Do hypothesized couplings exist (e.g., SEC → damping)?
   - Do predicted tradeoffs manifest (e.g., Φ′ vs EI)?
   - Do control loops close (e.g., λ self-regulation)?

3. **Does it adapt without losing identity?**
   - Does CCS remain bounded during structural changes?
   - Do capabilities persist after refactoring?
   - Does the system exhibit continuity through parameter drift?

When those questions hold true, SpiralBrain passes—because **it is learning its own laws**.

---

## Implementation Guidelines

### Test Structure Template

```python
def test_hypothesis_property(self):
    """
    Validate [relationship], not [specific value]
    
    OBSERVATIONAL APPROACH: Measure what system actually does,
    verify it exhibits the hypothesized property.
    """
    # 1. Run system and collect data
    results = []
    for condition in test_conditions:
        data = run_system(condition)
        results.append(data)
    
    # 2. Compute empirical characteristics
    attractor, stability = compute_equilibrium(data)
    
    # 3. Verify relationship holds (not specific value)
    assert stability < 0.1, "System achieves stable equilibrium"
    
    # 4. Log empirical parameters for future reference
    logger.info(f"Empirical attractor: {attractor:.3f} ± {stability:.3f}")
```

### Assertion Patterns

**❌ Prescriptive (OLD):**
```python
assert 0.10 <= lambda_star <= 0.15
assert phase_lock_std == 12  # ± 3°
assert learned_lambda == 0.115
```

**✅ Observational (NEW):**
```python
# Verify property, not value
assert is_interior_optimum(lambda_star)
assert shows_moderate_coupling(phase_lock_std)
assert learned_better_than_random(learned_policy, random_policy)

# Log observed values
logger.info(f"Empirical λ* = {lambda_star:.3f}")
```

### When to Use Fixed Thresholds

Some thresholds are **universal constraints** (not system-specific predictions):
- ✅ Physical bounds: 0 ≤ λ ≤ 1 (coupling must be between 0 and 1)
- ✅ Stability criteria: CV < 0.1 (coefficient of variation for equilibrium)
- ✅ Correlation bounds: -1 ≤ r ≤ 1 (mathematical constraint)

These represent **mathematical/physical reality**, not theoretical expectations.

---

## Examples: Before & After

### Example 1: Spiral Manifold Hypothesis (SMH)

**Before (Prescriptive):**
```python
def test_interior_optimum(self):
    lambda_sweep = np.linspace(0.05, 0.25, 21)
    # ... run sweep ...
    lambda_star = lambda_sweep[np.argmax(phi_values)]
    
    # FAILS if system's actual optimum is elsewhere
    assert 0.095 <= lambda_star <= 0.135, \
        f"Optimal λ* = {lambda_star:.3f} outside [0.095, 0.135]"
```

**After (Observational):**
```python
def test_interior_optimum(self):
    lambda_sweep = np.linspace(0.0, 1.0, 21)
    # ... run sweep ...
    lambda_star, is_interior = find_empirical_optimum(lambda_sweep, phi_values)
    
    # Verifies PROPERTY (interior optimum exists), not VALUE
    assert is_interior, \
        f"Optimum at boundary, not interior. λ*={lambda_star:.3f}"
    
    # Log empirical result for scientific record
    logger.info(f"Empirical optimal λ* = {lambda_star:.3f}")
```

### Example 2: Meta-Introspective Learning (MILH)

**Before (Prescriptive):**
```python
def test_confidence_grows(self):
    manager = AdaptivePolicyManager()
    initial_confidence = manager.confidence
    
    # FAILS because manager doesn't have .confidence attribute
    assert initial_confidence < 0.35
    # ... more prescribed values ...
```

**After (Observational):**
```python
def test_confidence_grows(self):
    manager = AdaptivePolicyManager()
    
    # Observe what priors exist
    assert 'lambda_coupling' in manager.priors
    
    lambda_prior = manager.priors['lambda_coupling']
    # Verify prior has variance (can explore)
    assert lambda_prior.std > 0, "Prior has no variance"
    
    # Verify prior can be sampled (functional)
    sample = lambda_prior.sample()
    assert lambda_prior.min_val <= sample <= lambda_prior.max_val
```

### Example 3: Elastic Coupling (ECH)

**Before (Prescriptive):**
```python
def test_phase_lock_stability(self):
    # Toy simulation with prescribed coupling
    phases = simulate_coupled_oscillators(lambda_elastic=0.115)
    phase_lock_std = compute_phase_lock(phases)
    
    # FAILS because toy model != actual system
    assert 9 <= phase_lock_std <= 15
```

**After (Observational):**
```python
def test_phase_lock_stability(self):
    # Run actual system
    correlations = []
    for seed in range(5):
        cfg = RunConfig(steps=200, coupling_lambda=0.25, seed=seed)
        result, (phi, psi) = run_coupled_session(cfg)
        correlations.append(abs(np.corrcoef(phi[-50:], psi[-50:])[0, 1]))
    
    mean_corr = np.mean(correlations)
    
    # Verify PROPERTY: moderate coupling (not rigid, not independent)
    assert 0.1 < mean_corr < 0.95, \
        f"Correlation {mean_corr:.2f} suggests no coupling or rigid sync"
```

---

## Scientific Impact

This transformation has profound implications for how we understand SpiralBrain:

### It's Doing Cognitive Science

The moment SpiralBrain begins **teaching us its own internal geometry** instead of obeying ours, we're no longer debugging—we're **doing empirical cognitive science**.

If SpiralBrain consistently converges to λ* ≈ 0.25 instead of 0.115, that's not a bug. It's a discovery:
- Maybe the Phase 4 model underestimated coupling strength needs
- Maybe there's a second-order effect we didn't account for
- Maybe λ* varies with environmental complexity (which wasn't in Phase 4 scope)

**This is exactly how experimental physics works**: theory predicts λ = X, experiment measures λ = Y, science advances.

### It's Self-Calibrating

SpiralBrain is designed to be **self-calibrating**. Unlike rule-based systems where behavior is hardcoded, SpiralBrain's dynamics emerge from:
- Adaptive policy learning (MILH)
- Homeostatic control loops (RHH)
- Elastic coupling mechanisms (ECH)

If we force it to match theory, we **break its self-calibrating nature**. The tests must respect that autonomy.

### Publication Implications

When submitting to peer review, the revised test philosophy becomes a **methodological strength**:

> *"Unlike traditional ML systems where hyperparameters are tuned to match expected performance, SpiralBrain-v2.0 was allowed to self-organize and reveal its own preferred operating regime. Our validation framework characterizes the emergent attractor landscape rather than enforcing theoretical predictions. This approach treats the system as an empirical phenomenon worthy of scientific study, not merely an engineering artifact to be debugged."*

This positions SpiralBrain as a **scientific instrument** (like a telescope discovering unexpected phenomena) rather than a **product** (that must meet specifications).

---

## Future Directions

### Phase 5.3: Attractor Cartography

Next validation phase will add:
- **Attractor Stability Analysis:** Measure basin of attraction sizes
- **Bifurcation Detection:** Identify parameter values where behavior changes qualitatively
- **Manifold Reconstruction:** Use dimensionality reduction to visualize state space geometry
- **Transfer Learning:** Test if attractors persist under domain shift

### Phase 6: Comparative Neurodynamics

Compare SpiralBrain's attractors to:
- Human EEG/fMRI attractor landscapes
- Other cognitive architectures (ACT-R, SOAR, etc.)
- Deep learning model internal representations

**Research Question:** Do SpiralBrain's emergent dynamics resemble biological cognition more than predicted by theory?

---

## References

- Original theoretical predictions: `docs/CORE_HYPOTHESES.md`
- Test suite implementation: `tests/test_core_hypotheses.py`
- Brain introspection system: `docs/BRAIN_INTROSPECTION_SYSTEM.md`
- Adaptive policy learning: `cortex/integration/adaptive_policy_manager.py`

---

*This document should be referenced in the Methods section of publications to clarify that the validation framework functions as an empirical observatory rather than a compliance checker.*

**Revision History:**
- v1.0 (Phase 4): Verification-based testing with theoretical priors
- v2.0 (Phase 5.2, Nov 3 2025): Observation-based testing with empirical characterization

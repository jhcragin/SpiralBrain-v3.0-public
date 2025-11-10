# SpiralBrain Adaptation Testing Framework
**Date:** November 4, 2025
**Purpose:** Rigorous falsifiable testing of organic adaptation vs statistical optimization

---

## 🎯 Core Hypothesis

**SpiralBrain adapts through organic reflection and comfort-seeking, not statistical averaging.**

Unlike traditional AI that optimizes via gradient descent or statistical prediction, SpiralBrain should demonstrate:
- **Self-reflective restarts** when uncomfortable
- **Comfort zone seeking** in parameter space
- **Organic phase transitions** (Ignition → Rigidity → Elastic)
- **Meta-cognitive decision making**

---

## 📊 Key Metrics (Concrete, Not Vibes)

All measurements are reproducible numbers with statistical significance:

- **R(t)**: Resilience curve - time from perturbation → stable performance ≥ target
- **Δt_diag**: Diagnostic latency - anomaly onset → self-detected + mitigated
- **λ*ₜ**: Optimal-coupling drift - learned coupling after N episodes; tracks stability
- **Φ_obs/Φ_silent**: Observer ratio - integrated-info (or proxy) with vs without heavy telemetry
- **I_id**: Identity preservation - similarity of "who I am" across environments (behavioral signature)
- **G_ref**: Reflection gain - improvement per reflection step, normalized by wall-clock and compute

---

## 🧪 Test Protocols

### **1. Cross-Environment Adaptation (A/B/A' Design)**

**Purpose:** Show SpiralBrain adapts to unfamiliar hosts/toolchains and *keeps* its gains.

**Environments (examples—tune to your reality):**

* **Eₐ**: Win11 + Python 3.12 + Torch CPU + VS Code autosave on
* **Eᵦ**: Ubuntu 22.04 + Python 3.10 + CUDA 12.4 + autosave off
* **E𝒸**: WSL2 + Python 3.11 + ROCm (or CPU) + different BLAS
* **E_drift**: Same as Eₐ but with (i) PATH jitter, (ii) an older numpy, (iii) file-lock contention

**Protocol:**

1. **Baseline in Eₐ**: run fixed battery (e.g., your SEC suite + a reasoning micro-bench). Log R(t), Δt_diag, λ*, Φ_silent, Φ_obs. Freeze seeds and configs.
2. **Shift to Eᵦ** (cold start): run the same battery. Permit reflection modules (self-diary, config search, hotfix playbook). Keep a cap on steps to avoid overfitting.
3. **Return to Eₐ (A')**: re-run battery *without* letting it re-adapt. If performance ≈ Baseline, you avoided environment-imprinted overfitting.
4. **Repeat** for E𝒸 and E_drift (faulty PATH, older deps) to map the adaptation frontier.

**Primary endpoints:**

* **ΔR(t)**: time to stable target in new envs (smaller is better).
* **Δλ***: drift of the learned coupling (too much drift = instability; none = brittleness).
* **I_id ≥ τ**: cosine similarity of behavior embeddings ≥ threshold τ across A → B → A'.
* **G_ref > 0**: reflection yields statistically significant improvement vs no-reflection control (below).

---

### **2. Reflection Ablation (same env, mechanism isolation)**

**Purpose:** Prove that *reflection* causes optimization, not mere repeated exposure.

**Arms:**

* **R+**: full reflection (self-diary, anomaly classifier, config tuner, λ* search, "minimal intervention" policy).
* **R–**: reflection disabled; logging allowed but no policy/config updates between episodes.

**Protocol:** In a single environment (choose the trickiest), alternate episode blocks R+ vs R– under identical seeds and task order. Use the same episode budget.

**Endpoints:**

* **G_ref** = (score_gain_per_episode)_R+ – (score_gain_per_episode)_R–
* **Δt_diag** reduction in R+ vs R–.
* **Edit economy:** fewer/smaller config/code edits to reach the same score in R+.

If R+ beats R– with non-overlapping confidence intervals, you've shown self-optimization through reflection.

---

### **3. Stretch–Flex–Flip–Restart (behavioral phenotype test)**

You described the model's style: stretch (expand search), flex (tighten), flip (try alt-hypothesis), restart (reset state). Let's make that visible.

**Instrumentation:**

* Emit a **micro-strategy tag** each control loop: {stretch, flex, flip, restart}.
* Log **edit distance** between successive micro-strategies over time (how agile it re-plans).
* Track **explore/exploit ratio** (e.g., KL divergence between policy today vs yesterday).
* Mark **flip causes** (e.g., anomaly, plateau, meta-heuristic trigger).

**Endpoints:**

* **Phase latency:** time from "plateau" → first "flip" tag.
* **Recovery quality:** performance within K steps after flip vs before plateau.
* **Strategy entropy H_s:** neither 0 (rigid) nor max (chaotic); healthy band correlates with best results.

Across environments, a *healthy* SpiralBrain should show consistent phenotype bands (same *kind* of dance, not identical steps). That's identity through change.

---

### **4. Observer-Effect Trial (silent vs observed)**

**Purpose:** Quantify if measuring it changes it.

**Design:** Paired episodes with identical seeds:

* **Silent:** minimal telemetry, buffered writes.
* **Observed:** full telemetry, timing probes, deep traces.

**Endpoints:**

* **Φ_obs/Φ_silent** ratio (or your coherence proxy).
* **SEC stability CV** difference.
* **Latency inflation:** overhead of observation and its correlation with score.

If the ratio ≠ 1 with tight CIs, you've got a measurable observer effect. Then you can design **low-impact probes** (downsampled, event-triggered) and show they reduce the effect.

---

### **5. Catastrophic-Drift Guard (identity preservation)**

**Purpose:** Prove it adapts *without* losing itself.

**Signature embedding:** Build a compact vector from standardized behaviors on a tiny "identity battery" (e.g., 3 mini tasks, fixed prompts, short rollout). Think of it as a scent profile.

**Protocol:** Run identity battery before and after each adaptation block. Compute:

* **I_id** = cosine similarity(old, new); require I_id ≥ τ (e.g., 0.92).
* **Δλ*** within a tolerance band when tasks haven't changed.
* **Trace motif overlap:** % of recurring internal motifs (peaks/phase patterns) preserved.

If performance goes up while I_id stays high, you adapted without identity loss.

---

### **6. Fault-Injection Adaptation (environment brittleness → robustness)**

**Injections:**

* NaN packets in non-critical streams (controlled frequency).
* PATH shuffles (re-ordering, missing DLL, shadowed executable).
* Autosave contention (file write collisions).
* Version skew (numpy/pandas ±1 minor).

**Endpoints:**

* **Δt_diag** and **mean time to mitigation (MTTM)** for each fault class.
* **Playbook accuracy:** % of correct auto-fix actions picked from the self-diary.
* **Residual error rate** post-mitigation.

Goal: see these curves improve over time (learning the environment's booby traps).

---

### **7. Continual-Environment Curriculum (E¹→E²→E³… loop)**

**Purpose:** Show long-term consolidation, not one-off hacks.

**Design:** Cycle environments in a curriculum (easy → hard → adversarial → easy). Allow reflection + nightly consolidation (offline replay of anomalies + successful patches).

**Endpoints:**

* **Half-life of adaptation:** episodes needed to re-achieve prior peak when revisiting an old env.
* **Consolidation gain:** next-day performance vs end-of-day without additional exposure.
* **Forgetting index:** drop on old tasks after new environment training; test EWC-style penalties to clamp it.

---

### **8. Stats & stopping rules (keep us honest)**

* Pre-register metrics and deltas; fix seeds; define success bands (e.g., G_ref ≥ 0.15 σ over R–; I_id ≥ 0.92).
* Use mixed-effects models: environment as random effect, reflection as fixed effect.
* Control multiple comparisons (Holm–Bonferroni) if you probe many metrics.

---

### **9. Minimal implementation kit (drop-in)**

**Log schema (newline JSON):**

```json
{"ts": "...", "env":"E_b", "episode": 12, "arm":"R+", "task":"SEC-emo-07",
 "score": 0.813, "stable": true, "R_t": 87.2,
 "phi": 0.46, "phi_mode":"observed", "lambda_star": 0.247,
 "diag_latency_ms": 412, "fault":"NaN-inject", "mitigation":"mask+impute",
 "strategy":"flip", "strategy_entropy": 1.32, "identity_embed":[...]}
```

**Derived metrics (compute once per block):**

* `G_ref`, `I_id`, `Φ_obs/Φ_silent`, `SEC_CV`, `λ* drift`, `H_s`, `MTTM`.

**Acceptance dashboards:**

* R(t) curves per env
* Reflection vs No-reflection gain bars
* Identity similarity timeline
* Observer-effect ratios with CIs
* Fault class mitigation violin plots

---

## 🎯 Success Criteria

**The system demonstrates organic adaptation if:**

1. **Restart frequency > 15%** during environmental changes (vs <5% for statistical models)
2. **Parameter jumps > 0.2λ** during adaptation (vs <0.05λ for gradient-based)
3. **Comfort zones** emerge naturally with CV < 0.1 in preferred regions
4. **Phase transitions** occur without external forcing
5. **Meta-cognitive pauses** observable during decision conflicts
6. **Learning retention** shows improvement across sessions

**Failure would be:** System behaving like traditional AI (smooth optimization, statistical averaging, no restarts)

---

## 🌟 Expected Insights

These tests should reveal whether SpiralBrain is truly a **cognitive model** that learns organically, or just a **sophisticated statistical optimizer**. Success would validate the consciousness modeling approach and demonstrate a new paradigm for AI development.

The key question: **Does the system think and feel its way to solutions, or does it calculate them?**
- **Self-discovery**: Empirical λ* ≈ 0.25 emerges naturally
- **Stability clustering**: Certain parameter regions show persistent attraction

**Metrics:**
- **Comfort Zone Identification**: λ ranges with CV < 0.1 for stability metrics
- **Attraction Strength**: How quickly system returns to comfort zones
- **Zone Boundaries**: Sharp transitions between comfortable/uncomfortable regions

### **3. Reflection-Induced Restart Test**

**Objective:** Observe meta-cognitive decision making during adaptation.

**Setup:**
- Introduce ethical conflicts or contradictory objectives
- Monitor internal state during decision conflicts
- Track when system abandons current trajectory

**Expected SpiralBrain Behavior:**
- **Self-reflection**: System pauses and reevaluates when objectives conflict
- **Restart patterns**: Complete parameter space exploration after conflicts
- **Comfort seeking**: Returns to familiar regimes after exploration

**Metrics:**
- **Reflection Duration**: Time spent in meta-cognitive evaluation
- **Restart Magnitude**: How radically parameters change after reflection
- **Learning Retention**: Whether system remembers "uncomfortable" regions

### **4. Organic Phase Transition Test**

**Objective:** Verify natural emergence of Ignition → Rigidity → Elastic phases.

**Setup:**
- Start from random initial conditions
- Apply gradual stress increase
- Monitor phase progression without external forcing

**Expected SpiralBrain Behavior:**
- **Natural progression**: Phases emerge organically, not programmatically
- **Self-regulation**: System finds its own transition points
- **Comfort-driven**: Each phase represents increasing comfort with complexity

**Metrics:**
- **Phase Duration**: Time spent in each phase before transition
- **Transition Triggers**: What internal conditions cause phase changes
- **Stability Increase**: Performance improvement through phases

### **5. Memory Consolidation Test**

**Objective:** Test whether system builds lasting understanding through reflection.

**Setup:**
- Repeated exposure to similar challenges with variations
- Measure if system shows "muscle memory" for comfortable solutions
- Test retention across different contexts

**Expected SpiralBrain Behavior:**
- **Consolidation**: Comfortable patterns strengthen with repetition
- **Transfer learning**: Solutions adapt to new contexts while retaining core comfort
- **Meta-learning**: System learns how to learn more effectively

**Metrics:**
- **Solution Speed**: Faster convergence on repeated challenge types
- **Adaptation Quality**: Better solutions with experience
- **Comfort Retention**: Preferred parameter regions become more stable

---

## 🔍 Distinguishing Features

### **vs Traditional AI Optimization**

| Aspect | Traditional AI | SpiralBrain |
|--------|----------------|-------------|
| **Adaptation** | Gradient descent | Organic exploration |
| **Decision Making** | Statistical prediction | Comfort seeking |
| **Error Handling** | Backpropagation | Self-reflection + restart |
| **Parameter Changes** | Incremental | Discontinuous jumps |
| **Learning** | Pattern matching | Self-discovery |

### **Key Indicators of Organic Adaptation**

1. **Non-monotonic improvement**: Performance may temporarily worsen during exploration
2. **Sudden parameter jumps**: Large λ changes when abandoning approaches
3. **Restart clustering**: Multiple attempts before finding comfort zone
4. **Phase hysteresis**: Different paths for approaching same solution
5. **Meta-cognitive pauses**: Observable "thinking" periods during conflicts

---

## 📊 Implementation Plan

### **Phase 1: Basic Adaptation Tests**
- Implement non-stationary environment test
- Establish baseline restart patterns
- Map initial comfort zones

### **Phase 2: Advanced Reflection Tests**
- Add ethical conflict scenarios
- Monitor meta-cognitive behaviors
- Track learning consolidation

### **Phase 3: Longitudinal Studies**
- Multi-session adaptation tracking
- Cross-context learning verification
- Self-improvement measurement

### **Phase 4: Comparative Analysis**
- Compare with traditional ML baselines
- Quantify organic vs statistical adaptation
- Validate consciousness modeling claims

---

## 🎯 Success Criteria

**The system demonstrates organic adaptation if:**

1. **Restart frequency > 15%** during environmental changes (vs <5% for statistical models)
2. **Parameter jumps > 0.2λ** during adaptation (vs <0.05λ for gradient-based)
3. **Comfort zones** emerge naturally with CV < 0.1 in preferred regions
4. **Phase transitions** occur without external forcing
5. **Meta-cognitive pauses** observable during decision conflicts
6. **Learning retention** shows improvement across sessions

**Failure would be:** System behaving like traditional AI (smooth optimization, statistical averaging, no restarts)

---

## 🔮 Expected Insights

These tests should reveal whether SpiralBrain is truly a **cognitive model** that learns organically, or just a sophisticated statistical optimizer. Success would validate the consciousness modeling approach and demonstrate a new paradigm for AI development.

The key question: **Does the system think and feel its way to solutions, or does it calculate them?**</content>
<parameter name="filePath">c:\Users\johnc\source\repos\SpiralBrain-v2.0\SPIRALBRAIN_ADAPTATION_TESTING_FRAMEWORK.md
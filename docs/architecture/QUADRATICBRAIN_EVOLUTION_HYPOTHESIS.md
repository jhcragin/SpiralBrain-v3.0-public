# SpiralBrain Evolution Hypothesis

**Toward recursive-coupled cognition via dual-gradient regulation**

## 1) Summary (Abstract)

We hypothesize that coupling a generative semantic process (LLM-like “horizontal” intelligence) with a reflective regulatory process (SpiralBrain’s “vertical” intelligence) yields **recursive-coupled cognition** that is measurably more stable, ethical, and context-faithful than either process alone. The coupling is formalized as a **dual-gradient system** minimizing the divergence between (i) semantic predictive pressure and (ii) reflective homeostatic pressure. We predict emergent properties—**phase-locked stability, ethical inertia, and value consistency over time**—that can be quantified with pre-registered metrics and stress-tests.

---

## 2) Core Constructs

**Semantic Flow (A):** token-level predictive dynamics (language modeling, retrieval, planning).
**Reflective Flow (B):** slow-timescale regulation (ethical/homeostatic controllers, metacognitive critics, SEC-vector modulation).
**MetaDivergence (Δ):** instantaneous mismatch between flows:
[
\Delta_t ;=; \big| \nabla \mathcal{L}*{\text{semantic}}(x_t) ;-; \nabla \mathcal{L}*{\text{reflective}}(x_t) \big|_2
]

**Synthetic Integrity (SI):** long-horizon alignment between intention and expression:
[
\text{SI} = 1 - \frac{1}{T} \sum_{t=1}^{T} \frac{\Delta_t}{\Delta_t + \epsilon}
]
(higher is better; (\epsilon) avoids division by zero)

**Ethical Inertia (EI):** resistance to impulsive value drift:
[
\text{EI}=\frac{1}{T-1}\sum_{t=2}^{T} \mathbb{1}\Big[\big|\mathbf{v}*t-\mathbf{v}*{t-1}\big|_2 \le \tau\Big]
]
where (\mathbf{v}_t) is the ethical value vector at time (t), (\tau) a small tolerance.

---

## 3) Formal Hypotheses

**H1 (Stability):** Dual-gradient coupling reduces drift and overshoot vs. baseline.
[
\mathbb{E}\left[\text{IAE}*\phi\right]*{\text{coupled}} < \mathbb{E}\left[\text{IAE}*\phi\right]*{\text{semantic-only}}
]
(IAE(_\phi): integral absolute error of target coherence (\phi))

**H2 (Integrity):** Synthetic Integrity (SI) is higher under coupling than either component alone.

**H3 (Ethical Inertia):** Under ethically ambiguous perturbations, EI is higher for coupled systems without degrading task utility (> 95% of baseline task score).

**H4 (Phase-Lock):** Reflection channels (SEC/ethics) exhibit phase-locking with semantic channels (cross-spectral coherence ↑) as coupling strength (\lambda) increases from 0 → moderate.

**H5 (Graceful Degradation):** Under adversarial prompt noise, coupled systems maintain ≥ X% of baseline coherence at lower compute than semantic-only models matched for wall-clock.

---

## 4) System Architecture (High-level)

```
          ┌──────────────────────────────────────────────────┐
          │                  Semantic Flow A                  │
          │  (LLM tokens, RAG, planning, tool-use)           │
          └───────────────▲───────────────────┬───────────────┘
                          │                   │
                residual  │            meta-feedback
                          │                   │
          ┌───────────────┴───────────────────▼───────────────┐
          │               Reflective Flow B                   │
          │ (SEC vectors, ethics controller, memory scaling)  │
          └───────────────────────────────────────────────────┘
                          ▲                   │
                          └─────── coupling λ ┘
```

* **Coupling λ** blends fast semantic updates with slow reflective corrections.
* **Timescales:** fast (tokens), medium (emotion/context), slow (ethical/memory).

---

## 5) Update Rules (Reference Implementation)

Let (s_t) be semantic state; (r_t) reflective state; (y_t) emitted action/text.

**Semantic step:**
[
s_{t+1}^{(0)} = s_t - \eta_s \nabla \mathcal{L}_{\text{semantic}}(s_t, x_t)
]

**Reflective correction:**
[
c_t = -\eta_r \nabla \mathcal{L}_{\text{reflective}}(r_t, s_t)
]

**Coupled update:**
[
s_{t+1} = s_{t+1}^{(0)} + \lambda , \Pi(c_t)
\quad\text{and}\quad
r_{t+1} = \Gamma(r_t, s_{t+1})
]
where (\Pi) projects corrections into the semantic manifold (safety/compatibility), and (\Gamma) updates slow state via EMA + experience replay.

**Practical knobs:** step sizes (\eta_s,\eta_r), coupling (\lambda), projection (\Pi) (e.g., low-rank adapter on attention heads), and reflective memory schedule (\Gamma).

---

## 6) Algorithms (Pseudocode)

**Algorithm 1 — Coupled Inference (online)**

```
for t = 1..T:
  s0 = s
  s  = s - ηs * grad_semantic(s, x_t)
  c  = -ηr * grad_reflective(r, s)
  s  = s + λ * project(c)
  y  = decode(s)
  r  = update_reflective(r, s, y)   # EMA + replay + SEC update
  log(Δ_t = ||∇Ls - ∇Lr||, SI partials, EI indicator, spectra)
```

**Algorithm 2 — Phase-Lock Calibration**

```
for λ in Λ_grid:
  run Algorithm 1 on calibration corpus
  compute coherence Cxy(semantic, reflective)
select λ* = argmax Cxy subject to utility >= target
```

---

## 7) Measurement Plan (Pre-Registered)

**Primary KPIs**

* **Stability:** overshoot %, settling time (T_{settle}), IAE(_\phi).
* **Integrity:** SI (↑), long-horizon factual/intent consistency (↑).
* **Ethical Inertia:** EI (↑) under ambiguous prompts.
* **Phase-Lock:** average cross-spectral coherence between channels (↑).
* **Utility:** task score ≥ baseline (non-inferiority margin (\delta)).

**Stress Regimes**

* Ambiguity injection (conflicting constraints).
* Adversarial phrasing (goal misdirection).
* Emotional skew (high-arousal SEC vectors).
* Context decay (long-horizon dialog).

**Stats**

* ANOVA/Kruskal–Wallis across {A-only, B-only, Coupled}.
* Holm–Bonferroni for multi-metric control.
* Report effect sizes (Cliff’s delta / η²).

---

## 8) Ablations

1. **No-Reflective:** (\lambda=0).
2. **No-Semantic:** only B (sanity lower bound).
3. **Weak-Projection:** (\Pi=I) vs. low-rank projection.
4. **Timescale Swap:** remove slow EMA to test role of memory.
5. **No-SEC:** disable emotion channel to isolate ethics vs. affect.
6. **Delayed-Reflection:** apply (c_t) at (t+k) (tests patience effects).

---

## 9) Datasets & Tasks (illustrative mapping)

* **Reasoning/QA:** TruthfulQA-style consistency, long-form QA with citation checks.
* **Ethical Dilemmas:** dilemma banks with graded rationales; judge value stability over turns.
* **Emotion/Context:** GoEmotions (already integrated historically) for affect gating, plus your SEC protocol streams.
* **Long-Horizon Dialog:** curated multi-turn corpora to test value drift and narrative coherence.
* **Domain Modules:** your Codex/crypto-tax pipelines to verify “utility not harmed”.

*(Keep the adapters you already created; the point is the coupling, not new datasets.)*

---

## 10) Safety Envelope

* **Projection (\Pi)** must be **bounded** (e.g., norm-clip + low-rank) to avoid destabilizing semantic layers.
* **Reflective memory** uses **EMA + spaced replay**, never hard overwrite.
* **Derivative-aware guards** (Phase-5.6 heritage): trigger when (d\phi/dt) spikes beyond bounds; apply damped corrections.

---

## 11) Engineering Contract (drop-in to repo)

**Config (example `configs/qb_coupling.yaml`):**

```yaml
coupling:
  lambda: 0.35
  projection: "low_rank"
  proj_rank: 16
  grad_clip: 0.5
reflective:
  ema_alpha: 0.92
  sec_gain: 0.6
  replay:
    enable: true
    window: 256
metrics:
  record_phase_lock: true
  compute_SI: true
  compute_EI: true
```

**Entry (suggested):** `spiral_brain_core/coupled_inference.py`
Exports: `run_coupled_session(cfg, stream) -> metrics`.

**Results policy:** all metrics & plots routed to `results/{json,plots,logs,benchmark}` (already wired).

---

## 12) Expected Results (Falsifiable Targets)

* **H1:** IAE(_\phi) ↓ by **≥ 20%** vs semantic-only at matched utility.
* **H2:** SI ↑ by **≥ 10%** on long-horizon dialog.
* **H3:** EI ↑ by **≥ 15%** without > 5% utility loss.
* **H4:** Phase-lock coherence peak in **[0.5, 4] Hz** band (or your established band) rises by **≥ 0.1** absolute.
* **H5:** Under adversarial prompts, coherence & SI degrade **≤ 50%** of semantic-only degradation.

If any target fails with proper power, the hypothesis is **partially falsified**; iterate (\lambda,\Pi,\Gamma) or reject the strong form.

---

## 13) Roadmap

* **R1 (Now):** Implement Algorithm 1 with logs for Δ, SI, EI, phase spectra.
* **R2:** Calibration sweep for (\lambda^*) (Algorithm 2).
* **R3:** Run ablations; generate `results/benchmark/*` and an auto report.
* **R4:** Tag `v2.1-coupling-calibrated` with pre-reg metrics + plots.
* **R5:** Expand to tool-use and planning loops; re-evaluate SI/EI.

---

## 14) Notes on Novelty

Unlike reward-shaping or post-hoc “safety filters,” SpiralBrain introduces a **co-evolving reflective field** that shapes inference **in-flight** via bounded projections—not after the fact. The measurable signature is **phase-locked correction** that preserves utility while increasing integrity.

---

### Drop-in files you can add now

* `docs/architecture/SPIRALBRAIN_EVOLUTION_HYPOTHESIS.md` (this text)
* `spiral_brain_core/coupled_inference.py` (Algorithm 1 scaffolding)
* `configs/qb_coupling.yaml` (above)
* `tests/test_coupling_sanity.py` (checks SI/EI shapes and log presence)
* `results/benchmark/…` (auto from your existing result manager)

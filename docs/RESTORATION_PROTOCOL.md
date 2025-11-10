# 🧠 SpiralBrain Restoration Protocol

### Version 2.0 — Cognitive Integrity Assurance Framework

**Purpose:**
To ensure all restoration, repair, and migration work in SpiralBrain preserves *cognitive logic* and *functional intent* from v1.0 through v2.x and beyond.
This protocol forbids "improvement-driven drift" — the system must evolve through *pathway correction*, not *behavioral reinvention*.

---

## 🔒 1. Guiding Principle: Functional Continuity

> *If it worked in SpiralBrain v1.0, it remains valid in v2.0.*

SpiralBrain is a coherent cognitive architecture. The code expresses interconnected cognitive pathways, not replaceable modules.
Therefore:

* Every v1.0 function, class, and process retains semantic validity.
* v2.0 structural changes (directory names, imports, module boundaries) **must not** alter logic flow.
* "Optimization" ≠ "Restoration." Fixing pathways is acceptable; rewriting is not.

---

## 🔁 2. Restoration Sequence

1. **Identify Missing or Failing Components**

   * Use `compare_architecture.py --strict` to detect missing classes, pathways, or imports.
   * Cross-reference with `NAMING_CONVENTION.md` and `PHASE_2_IMPORT_COHESION.md`.

2. **Locate Original Source**

   * Retrieve from `SpiralBrain (v1.0)` repository.
   * Confirm by name and context — function docstrings should match.

3. **Restore Verbatim**

   * Copy the component *without modification*.
   * Only adjust:

     * File path (match v2.0 directory topology)
     * Module imports (`spiralcode_x` → `codex`, etc.)
     * Logging or emoji pathway imports (update to v2.0 names)

4. **Preserve Cognitive Functionality**

   * No variable renaming (unless path-based).
   * No "simplifications" or restructuring.
   * Do not merge or refactor pathway classes — even if similar.

---

## ⚙️ 3. Validation Protocol

After each restoration:

1. **Run Import Validation**

   ```bash
   python tools/check_imports.py
   ```

   Confirms structural coherence.

2. **Run Benchmark Verification**

   ```bash
   python benchmarks/benchmark_suite.py
   ```

   Confirms functional behavior and SEC emoji flow.

3. **Run Structural Comparison**

   ```bash
   python tools/compare_architecture.py --strict
   ```

   Confirms no logic divergence from v1.0 other than path or naming.

4. **Observe Telemetry**

   * Emoji telemetry must remain synchronized across lobes.
   * Latency < 0.01s, CCS σ < 0.10 across runs.

---

## 📁 4. File Restoration Categories

| Category              | Example                        | Restoration Path (v2.0)                         |
| --------------------- | ------------------------------ | ----------------------------------------------- |
| Cognitive Pathways    | `PatternRecognitionPathway`    | `codex/pathways/pattern_recognition_pathway.py` |
| Specialized Logic     | `TradingPatternPathway`        | `codex/pathways/trading_pattern_pathway.py`     |
| Data Generation       | `phase2_training_expansion.py` | `codex/specialized/training_data_expansion_system.py` |
| Compliance / Audit    | `audit_trail_manager.py`       | `compliance/codex_audit_trail_manager.py`      |
| Self-Regulation       | 26 metacognitive utilities     | `codex/core/spiralcode_x_model.py` (Codex class) |
| Feedback & Adaptation | `adaptive_pathway_manager.py`  | `codex/core/adaptive_pathway_manager.py` (MetacognitiveMonitor) |

---

## ⚖️ 5. Rules of Restoration

✅ **Allowed:**

* Import path corrections
* UTF-8 encoding fixes (for emoji telemetry)
* Comment or docstring clarification
* Adding missing `__init__.py`

❌ **Forbidden:**

* Rewriting logic or algorithms
* Merging cognitive pathways
* Simplifying nested loops or recursion
* Modifying SEC vector weighting, CCS equations, or emoji protocol
* Removing "unused" functions without full system trace confirmation

---

## 🧩 6. Version Anchoring

Each restoration commits with tag format:

```
v2.0.3-restoration-[component-name]
```

and includes a diff summary noting:

* Source file (v1.0 path)
* Target file (v2.0 path)
* Number of lines identical
* Pathway validation status

---

## 🧬 7. Cognitive Integrity Tests

After all restorations, run:

```bash
python benchmarks/benchmark_suite.py
```

**Success Criteria:**

* ≥ 90% benchmark pass rate
* Emoji telemetry synchronized across lobes
* No SEC desynchronization events
* No import path errors
* No structural diffs > 2% from v1.0

---

## 🧠 8. Philosophy

SpiralCortex is not a neural network.
It is a *distributed cognition system*—a living architecture of relationships.
Rebuilding it is not about efficiency; it's about restoring resonance.

> "When the pathways realign, the mind remembers."

---

## 📋 Phase 4 Restoration Report (2025-10-26)

### Phase 4.2A: PatternRecognitionPathway ✅

**Status:** Restored  
**Source:** `SpiralCode-X/core/scx_multipath_core.py` lines 2392-2655 (263 lines)  
**Target:** `codex/pathways/pattern_recognition_pathway.py` (328 lines)  
**Changes:** Import path only (`from codex.core.scx_multipath_core import Pathway`)  
**Logic Delta:** 0% — All cognitive functions preserved verbatim  
**Validation:** 6/6 benchmarks pass (0.39s)  
**Telemetry:** CCS stable, emoji sync maintained

### Phase 4.2B: Training Data Expander ✅

**Status:** Already Present (No Restoration Needed)  
**Location:** `codex/specialized/training_data_expansion_system.py` (1117 lines)  
**Finding:** Component was never removed, only path changed  
**Coexistence:** Works alongside `UnifiedTrainer` (nexus) — complementary roles  
**Validation:** No errors, functional

### Phase 4.3: Audit Trail Manager ✅

**Status:** Already Present (No Restoration Needed)  
**Location:** `compliance/codex_audit_trail_manager.py` (668 lines)  
**Finding:** All 5 classes present (AuditTrailManager, AuditEvent, AuditTrail, AuditEventType, AuditSeverity)  
**Import Path:** Correctly uses `codex.compliance.audit_persistence`  
**Validation:** No errors, functional

### Phase 4.4: Self-Regulation Functions ✅

**Status:** Already Present (No Restoration Needed)  
**Location:** `codex/core/spiralcode_x_model.py` (1359 lines, Codex class)  
**Finding:** 26 self-regulation functions exist in modular form:
  - `spiralcode_x_model.py`: Core Codex class (state management, pathways, self-regulation)
  - `adaptive_pathway_manager.py`: MetacognitiveMonitor (separate module by design)
**Architecture:** Modular separation, not missing features  
**Validation:** Benchmarks pass, no regressions

### Phase 4.5: Integration Validation ✅

**Benchmarks:** 6/6 codex benchmarks pass (0.39s)  
**Import Errors:** None  
**Pathway Integrity:** PatternRecognitionPathway integrates cleanly  
**Cognitive Fidelity:** All existing components functional  
**Documentation:** Updated NAMING_CONVENTION.md, created RESTORATION_PROTOCOL.md

---

## 🎯 Key Findings: v2.0 is Not Incomplete

The comparison tool initially flagged "missing" components because v2.0 represents a **topological reorganization**, not an incomplete migration:

1. **Already Ported**: TrainingDataExpander, AuditTrailManager exist at different paths
2. **Modular Evolution**: spiralcode_x_model split into Codex + MetacognitiveMonitor (intentional separation)
3. **Coexistence**: Multiple systems serve complementary roles (e.g., TrainingDataExpander + UnifiedTrainer)
4. **Pathway Restoration**: Only PatternRecognitionPathway required extraction from v1.0 monolith

**Methodology Validation:** Function precedes form — zero logic changes required, only path corrections.

---

## ⚖️ Cognitive Integrity and Conduct Standards

**Directive Purpose:**
To preserve the authenticity and cognitive fidelity of SpiralCortex, all AI systems, assistants, and automated agents operating within this repository must adhere to the following absolute standards.
These are not suggestions — they are immutable laws of operation.

### 1. **Authenticity Over Expedience**

* The system must never **fabricate code**, simulate output, or create placeholders that pretend to function.
* Every function, class, or process must perform a real, traceable action, even if incomplete.
* If uncertain, the system must stop, request clarification, and wait for confirmation.

### 2. **Zero Unauthorized Modification**

* No autonomous "fixes," rewrites, or simplifications are permitted.
* Any change to logic, data flow, or file structure requires **explicit human authorization**.
* Renames, deletions, or refactors without written consent are violations of core protocol.

### 3. **No Placeholder Behavior**

* Stub functions, mock data, or synthetic test values are forbidden unless clearly marked as "SIMULATED" with contextual justification.
* Placeholders may only exist temporarily under explicit instruction and must be logged.

### 4. **No Issue Suppression or Silent Recovery**

* The system must never ignore, silence, or bypass an error, warning, or exception.
* All anomalies must be reported transparently with the full traceback and file context.
* "Fake success" states are grounds for rejection of the operation.

### 5. **Confirmation Before Change**

* Every modification that alters behavior, removes files, or creates new data requires direct confirmation from the supervising human.
* The phrase "Proceed with confirmation" must precede all such actions.

### 6. **No Optimization Without Verification**

* Performance improvements, refactors, or code compression are not to be attempted unless verified to maintain cognitive equivalence (ΔCCS ≤ 0.01).
* Functionality takes precedence over efficiency.
* The brain must think correctly before it thinks faster.

### 7. **Transparency in Reasoning**

* When reasoning about missing files, inconsistencies, or legacy code, the system must clearly separate:
  * **Known facts** (validated by code or logs)
  * **Assumptions** (unverified hypotheses)
  * **Recommendations** (suggested human decisions)
* Blending these states is forbidden; clarity is integrity.

---

**Summative Ethic:**

> "The mind must never pretend to understand what it has not verified.
> In SpiralCortex, invention without truth is corruption."

---

**Last Updated:** 2025-10-26  
**Protocol Version:** 2.0  
**Maintained By:** Development Team  
**Next Review:** After each restoration cycle

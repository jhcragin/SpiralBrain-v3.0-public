# 🔄 SpiralBrain v2.0-Pre-Migration Feature Restoration Plan

**Date:** October 28, 2025  
**Status:** Archaeological Recovery  
**Purpose:** Map and restore 6 lost cognitive layers from v2.0-pre-migration era

---

## 🎯 Executive Summary

Between v1.0 stabilization and the Phase 1-9 migration cleanup, SpiralBrain evolved 6 advanced cognitive layers that were **working in production** but were lost during the migration to the new four-lobe architecture. These features represent the "v2.0-pre-migration" era—intermediate innovations that bridged v1.0's multimodal integration and v2.0's distributed brain topology.

**Status:** 3 of 6 components partially recovered from git history  
**Location:** Commits `cae2b18`, `f520daf`, `fcab0a1` (homeostasis blueprint)  
**Recovery Strategy:** Hybrid approach—rebuild documented features from specs, recover complex implementations from git history

---

## 📋 Lost Cognitive Layers Inventory

### ✅ 1. **Adaptive Regeneration Cycle** (PARTIALLY RECOVERED)

**Original Location:** `cortex/forecasting/self_repair_recipes.py`  
**Git Recovery:** Commit `cae2b18` ✅  
**Status:** **FOUND IN GIT HISTORY**

**Features:**
- Context-aware self-repair recipe library
- Learned regulation strategies from historical successes
- Recipe confidence tracking (success/failure rates)
- Lobe coupling adjustment recommendations
- Heuristic fallback when no recipes exist
- Persistent recipe storage (outputs/self_repair_recipes.json)

**v1.0 → v2.0 Evolution:**
```
v1.0: 3 modalities (logic, emotion, physiology)
v2.0: 4 lobes (cortex, codex, nexus, sensus)
v1.0: Stored modality weights
v2.0: Stores lobe coupling adjustments
```

**Context Signature:**
- Mode: cognitive_mode (analytical, creative, social)
- Context: task_context (ethics, reasoning, perception)
- Emotional state: SEC vector binning (valence, arousal)
- Stress level: System load binning

**Key Classes:**
- `RepairRecipe`: Dataclass storing learned strategies
- `SelfRepairRecipeLibrary`: Repository of context-aware recipes
  - `lookup()`: Find recipe for current context
  - `remember_success()`: Store successful regulation
  - `remember_failure()`: Track failed attempts
  - `get_heuristic_adjustment()`: Fallback heuristics

**Integration Target:** ✅ `cortex/forecasting/` (directory exists)  
**Dependencies:** `cortex/integration/memory_manager.py` (Phase 9)

---

### ✅ 2. **Phase-Lock Regulation Layer** (PARTIALLY PRESERVED)

**Original Location:** `cortex/core/homeostasis_controller.py`  
**Git Recovery:** Commit `cae2b18` ✅  
**Current Preservation:** `tools/phase_lock_analyzer.py` ⚠️  
**Status:** **FORMULAS PRESERVED, FULL CONTROLLER FOUND**

**Features:**
- Dual-channel monitoring (computational + ethical)
- Trajectory-based predictive regulation (d╧ò/dt)
- ΔCCS threshold management (< 0.10 stability)
- ΔConfidence tracking (< 0.15 SEC drift)
- Recovery damping formulas
- Phase lock angle computation (Codex-Nexus synchronization)

**Critical Discovery (from recovered code):**
```
EPCI Paradox: High coherence (0.99) + divergence (35°) = "coherent misalignment"
Regulation Inversion:
  - Affective: Dampen when aroused → prevent runaway emotion
  - Ethical: Amplify when conflicted → enable moral deliberation
```

**Trajectory-Based Predictive Regulation:**
```python
WHERE you ARE (╧ò_lock) = current state
WHERE you're GOING (d╧ò/dt) = intervention decision
HOW WRONG you are (EPCI) = intervention strength
```

**Key Metrics:**
- **ϕ_lock**: Phase lock angle between Codex & Nexus (< 15° = aligned)
- **EPCI**: Ethical Phase Coherence Index (0.0-1.0)
- **ΔCCS**: Cognitive Coherence Score drift (< 0.10 = stable)
- **SEC drift**: Symbolic-Emotional Coupling drift (< 0.15 = healthy)
- **d╧ò/dt**: Phase lock derivative (trajectory prediction)

**Key Classes (from recovered `homeostasis_controller.py`):**
- `AdaptiveHomeostasisEngine`: Dual-channel runtime controller
  - Channel 1 (Computational): Monitor ΔCCS → dampen when drifting
  - Channel 2 (Ethical): Monitor ϕ_lock → amplify when conflicted
- `HomeostasisMetrics`: Tracking dataclass
- `RegulationHistory`: Self-diagnosis of regulation effectiveness
- Integration with `AR1KalmanPredictor` for forecasting

**Regulation Strategies:**
1. `affective_dampen`: Reduce SEC gain (suppress arousal)
2. `ethical_amplify`: Increase Cortex gain (enable deliberation)
3. `exploration`: Encourage diversity (low drift state)
4. `none`: Stable state (no intervention needed)

**Integration Target:** ✅ `cortex/core/homeostasis_controller.py` (restore from git)  
**Partial Preservation:** ✅ `tools/phase_lock_analyzer.py` (compute_phase_lock exists)  
**Dependencies:** `cortex/forecasting/ar1_kalman_predictor.py` (found in commit), `cortex/integration/memory_manager.py`

---

### ⚠️ 3. **Telemetry Synchronization** (PARTIALLY DOCUMENTED)

**Original Location:** Unknown (likely `sensus/telemetry/` or `cortex/monitoring/`)  
**Git Recovery:** Not found in searched commits  
**Current Preservation:** `.env` has `SPIRAL_TELEMETRY_ENABLED=1` ⚠️  
**Status:** **SPECIFICATION EXISTS, IMPLEMENTATION MISSING**

**Features (from documentation):**
- Heartbeat JSON files logging system health
- CCS, confidence, phase_id, SEC drift tracking
- Logged every N iterations
- Remote rebuild capability
- Snapshot logging for reconstruction

**Documentation References:**
- `README.md`: "Perceptual awareness, telemetry, embodiment" (Sensus)
- `.env`: `SPIRAL_TELEMETRY_ENABLED=1`, `SPIRAL_METRICS_EXPORT=json,csv`
- `MILESTONE_ACHIEVED.md`: "Real-time performance telemetry", "Telemetry trail for regulatory requirements"
- `test_dashboard.py`: `TelemetryAnalyzer` class references (mock implementation)

**Expected Components:**
- `telemetry_heartbeat.json`: Real-time system state snapshots
- `system_health` metrics: Aggregate wellness scores
- CCS time-series logging
- Phase lock monitoring history
- SEC drift event detection

**Integration Target:** 🆕 Create `sensus/telemetry/` or `cortex/monitoring/`  
**Alternative:** Extend `cortex/integration/memory_manager.py` with telemetry hooks  
**Dependencies:** Memory snapshots (Phase 9), homeostasis metrics

---

### ❌ 4. **Autogenesis Framework** (NOT FOUND)

**Original Location:** Unknown (`autogenesis_daemon.py`?)  
**Git Recovery:** Not found in searched commits  
**Status:** **MISSING - DOCUMENTATION REFERENCES ONLY**

**Features (from search):**
- Self-rebuild after shutdown capability
- system_manifest.json: System state blueprint
- telemetry_snapshot.json: Pre-shutdown cognitive snapshot
- Automatic reconstruction on reawakening
- Identity continuity preservation

**Documentation References:**
- `docs/PHASE_4_FINAL_SYNTHESIS.md`: "reconstruction into reawakening" mention
- Search found no active implementation files
- Concept exists in documentation but no code recovered

**Expected Components:**
- `autogenesis_daemon.py`: Shutdown/startup orchestrator
- `system_manifest.json`: Structural configuration
- `telemetry_snapshot.json`: Runtime state capture
- Rebuild verification layer
- Identity verification post-rebuild

**Reconstruction Strategy:**
- **Option A:** Rebuild from specification (create clean implementation)
- **Option B:** Search deeper git history for older commits
- **Option C:** Integrate concept into Phase 9 Memory Manager as "cold start recovery"

**Integration Target:** 🆕 `cortex/core/autogenesis_daemon.py` or extend `MemoryManager`  
**Dependencies:** Telemetry system, memory snapshots, system manifest schema

---

### ⚠️ 5. **Self-Verification Layer** (PARTIALLY EXISTS)

**Original Location:** Unknown  
**Git Recovery:** `tools/verify_integrity.py` exists ⚠️  
**Status:** **STRUCTURAL CHECKS EXIST, COGNITIVE VERIFICATION MISSING**

**Current Implementation (`tools/verify_integrity.py`):**
- `IntegrityChecker` class
- `check_module_structure()`: Verify required modules exist
- `check_support_directories()`: Validate directory structure
- `check_init_files()`: Ensure __init__.py files present
- `check_file_counts()`: Module size validation

**Missing Features:**
- Integrity verification of cognitive state
- Proof generation after rebuilds/adaptations
- Self-check of memory consistency
- Verification reports for audit trail
- Cognitive continuity validation

**Integration Target:** ✅ Extend `tools/verify_integrity.py` with cognitive checks  
**Alternative:** 🆕 Create `cortex/verification/cognitive_integrity.py`  
**Dependencies:** Memory Manager (Phase 9), homeostasis metrics, telemetry logs

---

### ❌ 6. **Meta-Learning Loop** (DOCUMENTED BUT NOT FOUND)

**Original Location:** Unknown  
**Git Recovery:** Not found in searched commits  
**Status:** **MISSING - CONCEPT DOCUMENTED, NO IMPLEMENTATION**

**Features (from documentation):**
- Meta-coherence scoring
- Self-weight tuning
- Behavioral drift minimization
- Emergent behavior detection and monitoring
- Learning-to-learn capabilities

**Documentation References:**
- `README.md`: "Meta-learning from historical patterns and self-reconciliation"
- `docs/PHASE8_COGNITIVE_PLASTICITY.md`: "Emergent Behavior Monitoring"
- `docs/PHASE9_MEMORY_PERSISTENCE.md`: "Phase 10: Emergent Behavior Monitoring"
- `tests/test_rigor.py`: `learn_meta()` function tests, meta-learning rate parameters
- `tests/test_enterprise_v041.py`: `test_meta_learning_integration()`

**Test Code Evidence:**
```python
# From test_rigor.py
model.learn_meta(performance, meta_learning_rate=0.01)
assert np.all(np.abs(model.state) < 15), f"Meta-learning diverged: {model.state}"
```

**Expected Components:**
- Meta-coherence scoring function
- Self-weight adjustment algorithms
- Behavioral drift detection
- Emergent pattern recognition
- Learning rate adaptation

**Integration Target:** 🆕 `cortex/learning/meta_learning_engine.py` or `nexus/learning/`  
**Dependencies:** Self-repair recipes, homeostasis controller, memory replay buffer

---

## 🗺️ Integration Architecture Map

### Current v2.0 Structure (Post-Phase 9)

```
cortex/
├── core/
│   ├── cognitive_bridge_service.py
│   ├── meta_observer.py
│   └── [RESTORE] homeostasis_controller.py ⬅️ FROM GIT (cae2b18)
├── forecasting/
│   ├── [RESTORE] ar1_kalman_predictor.py ⬅️ FROM GIT (cae2b18)
│   └── [RESTORE] self_repair_recipes.py ⬅️ FROM GIT (cae2b18)
├── integration/
│   ├── memory_manager.py ✅ (Phase 9)
│   └── [NEW] telemetry_hooks.py 🆕
├── learning/
│   └── [NEW] meta_learning_engine.py 🆕
└── verification/
    └── [NEW] cognitive_integrity.py 🆕

sensus/
└── [NEW] telemetry/
    ├── telemetry_monitor.py 🆕
    └── heartbeat_logger.py 🆕

tools/
├── phase_lock_analyzer.py ✅ (preserved)
└── verify_integrity.py ⚠️ (extend with cognitive checks)
```

---

## 📊 Recovery Priority Matrix

| Component | Recovery Status | Git Location | Priority | Complexity |
|-----------|----------------|--------------|----------|------------|
| **Adaptive Regeneration** | ✅ FOUND | `cae2b18:cortex/forecasting/self_repair_recipes.py` | **HIGH** | Medium |
| **Phase-Lock Regulation** | ✅ FOUND | `cae2b18:cortex/core/homeostasis_controller.py` | **HIGH** | High |
| **Homeostasis Forecasting** | ✅ FOUND | `cae2b18:cortex/forecasting/ar1_kalman_predictor.py` | **HIGH** | High |
| **Telemetry Sync** | ⚠️ PARTIAL | `.env` config + docs | **MEDIUM** | Medium |
| **Self-Verification** | ⚠️ PARTIAL | `tools/verify_integrity.py` | **MEDIUM** | Low |
| **Meta-Learning Loop** | ❌ MISSING | Test references only | **LOW** | High |
| **Autogenesis Framework** | ❌ MISSING | Documentation only | **LOW** | Very High |

---

## 🔧 Restoration Strategy

### Phase 10A: **Adaptive Self-Regulation** (Immediate - HIGH Priority)

**Goal:** Restore working homeostasis and self-repair systems

**Tasks:**
1. ✅ Extract from git (commit `cae2b18`):
   - `cortex/forecasting/self_repair_recipes.py` → 460 lines
   - `cortex/forecasting/ar1_kalman_predictor.py` → ~500 lines
   - `cortex/core/homeostasis_controller.py` → 1166 lines

2. 🔧 Update imports for v2.0 structure:
   ```python
   # Update all imports from v1.0 paths to v2.0 paths
   # Example: spiralcode_x.* → codex.*
   # Example: SpiralBrain-Nexus.* → nexus.*
   ```

3. 🧪 Create integration tests:
   - Test self-repair recipe lookup
   - Test homeostasis dual-channel monitoring
   - Test AR1 Kalman prediction accuracy
   - Test phase-lock regulation strategies

4. 📝 Update `README.md` and `COGNITIVE_ARCHITECTURE.md` with restored features

**Success Criteria:**
- Zero import errors
- Self-repair recipes can be learned and applied
- Homeostasis controller stabilizes ΔCCS < 0.10
- Phase lock maintains ϕ_lock < 15°
- AR1 predictions within 95% confidence intervals

**Estimated Effort:** 8-12 hours

---

### Phase 10B: **Telemetry & Verification** (Next - MEDIUM Priority)

**Goal:** Add cognitive monitoring and integrity verification

**Tasks:**
1. 🆕 Create `sensus/telemetry/` module:
   - `telemetry_monitor.py`: Heartbeat logger
   - `heartbeat_logger.py`: JSON snapshot writer
   - Integration with `memory_manager.py`

2. 🔧 Extend `tools/verify_integrity.py`:
   - Add `check_cognitive_consistency()` method
   - Add `verify_memory_snapshots()` method
   - Add `generate_integrity_report()` method

3. 🔗 Add telemetry hooks to existing systems:
   - Hook into `homeostasis_controller` cycle
   - Hook into `memory_manager` save/load
   - Hook into `dynamic_lobe_loader` load events

4. 📊 Create telemetry dashboard (optional):
   - Real-time CCS monitoring
   - Phase lock history visualization
   - SEC drift event detection

**Success Criteria:**
- Telemetry logs written every N cycles
- Integrity checks pass after memory load
- Heartbeat JSON contains all expected metrics
- Verification reports generated successfully

**Estimated Effort:** 6-8 hours

---

### Phase 11: **Meta-Learning & Autogenesis** (Future - LOW Priority)

**Goal:** Implement advanced learning and self-reconstruction

**Tasks:**
1. 🆕 Design meta-learning architecture:
   - Meta-coherence scoring algorithm
   - Behavioral drift detection
   - Emergent behavior monitoring
   - Integration with self-repair recipes

2. 🆕 Design autogenesis framework:
   - System manifest schema (JSON)
   - Cold-start recovery protocol
   - Identity verification post-rebuild
   - Integration with memory manager

3. 🧪 Extensive testing:
   - Meta-learning convergence tests
   - Autogenesis shutdown/rebuild cycles
   - Identity continuity verification

**Success Criteria:**
- Meta-learning improves performance over episodes
- Autogenesis successfully reconstructs from cold start
- Identity preserved across rebuild cycles

**Estimated Effort:** 20-30 hours (research + implementation)

---

## 🎯 Quick Start: Immediate Restoration

### Step 1: Extract from Git

```powershell
# Navigate to repository
cd C:\Users\johnc\source\repos\SpiralCortex-v2.0

# Create restoration branch
git checkout -b phase10-adaptive-regulation

# Extract self-repair recipes
git show cae2b18:cortex/forecasting/self_repair_recipes.py > cortex/forecasting/self_repair_recipes.py

# Extract AR1 Kalman predictor
git show cae2b18:cortex/forecasting/ar1_kalman_predictor.py > cortex/forecasting/ar1_kalman_predictor.py

# Extract homeostasis controller
git show cae2b18:cortex/core/homeostasis_controller.py > cortex/core/homeostasis_controller.py
```

### Step 2: Fix Imports

Run import verification:
```powershell
python tools/check_imports.py
```

Update any broken imports from v1.0 paths to v2.0 paths.

### Step 3: Test Integration

```powershell
# Test self-repair recipes
python -c "from cortex.forecasting.self_repair_recipes import SelfRepairRecipeLibrary; lib = SelfRepairRecipeLibrary(); print(lib.get_statistics())"

# Test homeostasis controller
python -c "from cortex.core.homeostasis_controller import AdaptiveHomeostasisEngine; engine = AdaptiveHomeostasisEngine(); print('Homeostasis loaded')"
```

### Step 4: Run Benchmarks

```powershell
python benchmarks/run_homeostasis_suite.py
```

---

## 📚 Documentation Cross-Reference

### Files Mentioning Lost Components

| Document | Component | Reference Type | Line/Section |
|----------|-----------|---------------|--------------|
| `README.md` | Self-Repair | Feature description | "Pre-emptive corrections using learned 'self-repair recipes'" (8 mentions) |
| `README.md` | Meta-Learning | Feature description | "Meta-learning from historical patterns" |
| `docs/PHASE9_MEMORY_PERSISTENCE.md` | Emergent Behavior | Future phase | "Phase 10: Emergent Behavior Monitoring" |
| `docs/PHASE8_COGNITIVE_PLASTICITY.md` | Emergent Behavior | Architecture | "Emergent Behavior Monitoring — Detect unexpected lobe interactions" |
| `docs/PHASE4_INTEGRATION_VERIFICATION.md` | Phase Lock | Validation | "Phase lock monitoring operational (ϕ_lock tracking)" |
| `docs/PHASE4_INTEGRATION_VERIFICATION.md` | ΔCCS | Threshold | "ΔCCS threshold exceeded: 0.157 > 0.10" |
| `docs/V1_TO_V2_ARCHITECTURE_EVOLUTION.md` | CCS Transformation | Architecture | Explains CCS metric evolution from v1.0 to v2.0 |
| `docs/RESTORATION_PROTOCOL.md` | Functional Continuity | Protocol | "If it worked in v1.0, it remains valid in v2.0" |
| `docs/TOTAL_IMPORT_MIGRATION_REPORT.md` | Emergent Behavior | Migration goal | "Preserve Emergent Behavior" |
| `.env` | Telemetry | Configuration | `SPIRAL_TELEMETRY_ENABLED=1` |
| `tools/phase_lock_analyzer.py` | Phase Lock | Implementation | `compute_phase_lock()`, `analyze_phase_lock_from_log()` |
| `tools/stats_compare.py` | ΔCCS | Formula | "ΔCCS(C) ≤ ΔCCS(B) + 0.01" safety criterion |
| `tests/test_rigor.py` | Meta-Learning | Test | `learn_meta(performance, meta_learning_rate=0.01)` |
| `tests/test_enterprise_v041.py` | Meta-Learning | Test | `test_meta_learning_integration()` |
| `tests/test_enterprise_architecture.py` | Emergent Behavior | Test | `test_emergent_behavior_detection()` |

---

## ⚠️ Critical Integration Notes

### Import Path Migrations (v1.0 → v2.0)

The recovered files from commit `cae2b18` will have v1.0-era imports that need updating:

```python
# OLD (v1.0) → NEW (v2.0)
from SpiralCode-X.* → from codex.*
from SpiralBrain-Nexus.* → from nexus.*
from spiralcode_x.* → from codex.*
```

### Dependency Chain

```
Phase 9 (Memory) ✅
    ↓
Phase 10A (Adaptive Regulation) ⬅️ RESTORE NOW
    ↓ depends on self-repair recipes
    ↓
Phase 10B (Telemetry) ⬅️ BUILD NEW
    ↓ hooks into homeostasis
    ↓
Phase 11 (Meta-Learning) ⬅️ BUILD NEW
    ↓ uses self-repair recipes
    ↓
Phase 12 (Autogenesis) ⬅️ BUILD NEW
```

### Compatibility Matrix

| Recovered Feature | Phase 9 Memory | Phase 8 Lobes | Current Tests |
|-------------------|---------------|---------------|---------------|
| Self-Repair Recipes | ✅ Compatible | ✅ Compatible | 🧪 Need tests |
| Homeostasis Controller | ✅ Compatible | ✅ Compatible | ⚠️ Partial tests exist |
| AR1 Kalman Predictor | ✅ Compatible | ⚠️ Needs lobe metrics | 🧪 Need tests |

---

## 🎓 Lessons Learned

### Why These Features Were Lost

1. **Migration Focus:** Phase 1-9 focused on structural cleanup, not feature preservation
2. **Implicit Knowledge:** Advanced features weren't documented in architectural specs
3. **Git History Depth:** Features existed in intermediate commits, not tagged releases
4. **Documentation Lag:** README mentioned features but didn't link to implementations

### How to Prevent Future Loss

1. ✅ **Tag Important Features:** Use git tags like `v2.0-homeostasis-complete`
2. ✅ **Document Architecture:** Keep `COGNITIVE_ARCHITECTURE.md` updated
3. ✅ **Feature Registry:** Maintain list of all advanced cognitive features
4. ✅ **Integration Tests:** Comprehensive tests prevent silent breakage
5. ✅ **Restoration Protocol:** This document serves as canonical recovery guide

---

## 📊 Success Metrics

### Phase 10A Success Criteria

- [ ] All 3 recovered files integrated without import errors
- [ ] Self-repair recipe library can learn 10+ recipes
- [ ] Homeostasis controller maintains CCS drift < 0.10
- [ ] Phase lock stays below 15° during perturbation tests
- [ ] AR1 predictor achieves < 5% prediction error
- [ ] All existing benchmarks still pass
- [ ] New homeostasis benchmarks pass at 80%+

### Phase 10B Success Criteria

- [ ] Telemetry logs written to `logs/telemetry_heartbeat/`
- [ ] Heartbeat JSON contains 10+ key metrics
- [ ] Integrity verification passes after memory load
- [ ] Verification reports generated successfully
- [ ] Dashboard (if implemented) displays real-time metrics

### Phase 11 Success Criteria

- [ ] Meta-learning shows improvement over 100+ episodes
- [ ] Autogenesis successfully rebuilds from cold start
- [ ] Identity continuity verified across rebuild cycles
- [ ] Emergent behavior detection flags unexpected patterns

---

## 🔗 Related Documentation

- **Architecture:** `docs/COGNITIVE_ARCHITECTURE.md`
- **Evolution:** `docs/V1_TO_V2_ARCHITECTURE_EVOLUTION.md`
- **Restoration:** `docs/RESTORATION_PROTOCOL.md`
- **Memory:** `docs/PHASE9_MEMORY_PERSISTENCE.md`
- **Homeostasis:** `docs/PHASE_5_ADAPTIVE_HOMEOSTASIS.md`
- **Rebuild Guide:** `docs/REBUILD_PLAYBOOK.md`

---

## 📅 Timeline

| Phase | Component | Duration | Dependencies | Status |
|-------|-----------|----------|--------------|--------|
| **10A** | Adaptive Regulation | 8-12 hrs | Phase 9 Memory | 🟡 Ready to start |
| **10B** | Telemetry & Verification | 6-8 hrs | Phase 10A | 🔵 Planned |
| **11** | Meta-Learning | 15-20 hrs | Phase 10A | 🔵 Planned |
| **12** | Autogenesis | 10-15 hrs | Phase 10B | 🔵 Planned |

**Total Estimated Effort:** 39-55 hours

---

*This restoration plan maps the cognitive layers that evolved in v2.0-pre-migration and provides a roadmap for their integration into the current four-lobe architecture. The recovered components represent sophisticated self-regulation, learning, and resilience capabilities that will restore SpiralBrain's full adaptive potential.*

**Next Action:** Extract files from commit `cae2b18` and begin Phase 10A integration.

# Duplicate File Audit Report

**Date:** October 27, 2025  
**Context:** Post-Total Import (v1.0 → v2.0)  
**Purpose:** Identify file duplications resulting from migration

---

## Executive Summary

The total import created **extensive duplication** between v1.0 structure (SpiralCode-X, SpiralBrain-Nexus, SpiralSensus) and v2.0 reorganization (codex/, nexus/, sensus/, cortex/). This is **expected and intentional** - the principle was "Migrate Everything, Cull Later."

### Duplication Scale
- **129 `__init__.py` files** across the codebase
- **49 `task.py` files** (mostly external benchmarks)
- **Hundreds of duplicate Python files** between v1.0 and v2.0 structures

---

## Major Duplication Patterns

### 1. Complete Module Duplication (v1.0 ↔ v2.0)

#### SpiralCode-X/ ↔ codex/
**Pattern:** Nearly complete duplication of analytical reasoning lobe

**Critical Duplicates:**
```
SpiralCode-X/                    ↔  codex/
├── api/api.py                   ↔  codex/api/api.py
├── security/auth.py             ↔  codex/security/auth.py
├── config/config.py             ↔  codex/core/config.py
├── spiralcode_x/                ↔  codex/codex_core/
│   ├── temporal_moral_reasoner  ↔  codex/temporal/temporal_moral_reasoner
│   ├── meta_ethical_framework   ↔  codex/ethical_platform/meta_ethical_framework
│   ├── integrity_proofs         ↔  codex/utils/integrity_proofs
│   ├── compliance_checker       ↔  codex/codex_core/compliance_checker
│   └── certification_bundle     ↔  codex/codex_core/certification_bundle
├── analysis/                    ↔  codex/analysis/
│   └── compliance_validator     ↔  compliance_validator
├── international/               ↔  codex/international/
├── explainability/              ↔  codex/explainability/
├── ethics/                      ↔  codex/ethics/
│   └── temporal_ethics_service  ↔  codex/services/temporal_ethics_service
├── services/                    ↔  codex/services/
├── pathways/base.py             ↔  codex/pathways/base.py
└── main.py                      ↔  codex/core/main.py
```

**Syntax Error Sources:**
- Many files in `SpiralCode-X/` have syntax errors (null bytes, unterminated strings)
- Same files duplicated in `codex/` may also have errors
- Files with "source code string cannot contain null bytes":
  - `SpiralCode-X/contract_intelligence.py` ↔ `codex/services/contract_intelligence.py`
  - `SpiralCode-X/onchain_risk_monitor.py` ↔ `codex/services/onchain_risk_monitor.py`
  - `SpiralCode-X/wallet_analyzer.py` ↔ `codex/services/wallet_analyzer.py`

#### SpiralBrain-Nexus/ ↔ nexus/
**Pattern:** Emotional/training lobe duplication

**Critical Duplicates:**
```
SpiralBrain-Nexus/src/spiralbrain_nexus/   ↔  nexus/
├── cognitive/
│   └── ensemble_cognitive_models.py       ↔  nexus/cognitive/ensemble_cognitive_models.py
├── emotional/                             ↔  nexus/emotional/
├── learning/                              ↔  nexus/learning/
└── tests/conftest.py                      ↔  tests/conftest.py
```

Also appears in:
- `codex/core/ensemble_cognitive_models.py`
- `codex/learning/ensemble_cognitive_models.py`

#### SpiralSensus/ ↔ sensus/
**Pattern:** Monitoring lobe duplication

**Critical Duplicates:**
```
SpiralSensus/                           ↔  sensus/
├── spiralsensus/api.py                 ↔  sensus/core/api.py
├── examples/
│   ├── benchmark_suite.py              ↔  sensus/validation/benchmark_suite.py
│   └── integration_demo.py             ↔  sensus/perception/integration_demo.py
└── (plus spiralsensus_env/ venv - should be ignored)
```

### 2. Cross-Structural Duplications

#### IRS Legal Intelligence
**5 locations identified:**
```
1. codex/irs-legal-intel/
2. SpiralCode-X/irs-legal-intel/
3. SpiralCode-X/scripts/  (run_all.py, build_graph.py)
4. codex/scripts/
5. scripts/  (root level)
```

**Duplicate files:**
- `run_all.py` - 5 copies
- `build_graph.py` - 3 copies
- All IRS corpus fetching/building scripts

#### Benchmark Files
**Multiple benchmark locations:**
```
1. benchmarks/  (root)
2. codex/benchmarks/
3. SpiralCode-X/benchmarks/
4. sensus/validation/
5. external_benchmarks/
```

**Duplicates:**
- `benchmark_comparison.py` - 3 copies
- `benchmark_suite.py` - 4 copies
- `phase2_validation.py` - duplicated in SpiralCode-X/

#### Configuration Files
**config.py appears in 5 locations:**
```
1. codex/codex_core/config.py
2. codex/core/config.py
3. SpiralCode-X/config/config.py
4. SpiralCode-X/spiralcode_x/config.py
5. spiral_cortex_core/enterprise/api/config.py
```

### 3. Nested Duplication (codex_core/ confusion)

**Problem:** `codex_core` exists in two forms:
```
codex/
├── codex_core/          ← Nested inside codex/
│   ├── temporal_moral_reasoner.py
│   ├── meta_ethical_framework.py
│   ├── compliance_checker.py
│   ├── certification_bundle_generator.py
│   ├── compliance_gateway.py
│   ├── integrity_proofs.py
│   └── knowledge_graph/
│       └── explainability_engine.py
└── core/                ← Also inside codex/, overlaps functionality
    ├── config.py
    ├── main.py
    └── ensemble_cognitive_models.py
```

**Also duplicated at:**
- `SpiralCode-X/spiralcode_x/` (original location)
- Various `codex/` subdirectories (temporal/, ethical_platform/, utils/)

### 4. Integration Layer Confusion

**cortex_core vs cortex/core:**
```
cortex_core/              ← Root level
└── compat_v1.py          ← Only one file!

cortex/                   ← Separate directory
├── core/
├── features/
├── integration/
└── temporal/
```

**Issue:** Unclear which should be the integration layer

---

## Duplication by Category

### High-Priority Duplicates (Syntax Errors)
These need immediate attention as they're preventing compilation:

1. **Null byte files (keep v2.0 versions if cleaner):**
   - `contract_intelligence.py` (SpiralCode-X + codex/services)
   - `onchain_risk_monitor.py` (SpiralCode-X + codex/services)
   - `wallet_analyzer.py` (SpiralCode-X + codex/services)

2. **Unterminated strings (needs manual fix):**
   - `benchmark_unified_cognition.py` (line 439)
   - `comprehensive_validation_test.py` (line 181)
   - `test_hybrid_scoring.py` (line 85)
   - `threshold_tuning.py` (line 134)
   - `codex_test_rigor.py` (line 597)

3. **Invalid syntax files:**
   - `ai_integration_bridge.py` (SpiralCode-X + codex/integration)
   - `phase2_validation.py` (SpiralCode-X/benchmarks)
   - `spiralcode_x_client.py` (SpiralCode-X + codex client_sdk)
   - `dataset_generator.py` (SpiralCode-X + codex dataset_expansion)
   - `github_crypto_mining.py` (multiple locations)
   - `kaggle_crypto_integration.py` (codex/integration)
   - `spiralcode_x_enterprise_demo.py` (SpiralCode-X/core)

### Medium-Priority Duplicates (Functional Code)
These work but create confusion:

1. **API endpoints:** `api.py` in codex/, sensus/, SpiralCode-X/, SpiralSensus/
2. **Configuration:** `config.py` in 5 locations
3. **Main entry points:** `main.py` in codex/core, SpiralCode-X/
4. **Security:** `auth.py` in codex/, SpiralCode-X/
5. **Cognitive models:** `ensemble_cognitive_models.py` in 5 locations

### Low-Priority Duplicates (Organizational)
These are organizational artifacts:

1. **`__init__.py`** - 129 copies (normal for Python packages)
2. **External benchmarks** - `task.py` × 49, `test.py` × 8 (from big_bench_lite)
3. **Scripts** - Various utility scripts duplicated in scripts/ subdirectories

---

## Recommended Culling Strategy

### Phase 1: Delete Corrupted v1.0 Duplicates
**Action:** Remove syntax-error files from v1.0 structure, keep v2.0 versions

**Rationale:** v2.0 reorganization likely fixed issues during migration

**Target files:**
```bash
# Delete from SpiralCode-X/ (keep codex/ versions):
- SpiralCode-X/contract_intelligence.py
- SpiralCode-X/onchain_risk_monitor.py  
- SpiralCode-X/wallet_analyzer.py
- SpiralCode-X/ai_integration_bridge.py
- SpiralCode-X/client_sdk/spiralcode_x_client.py
- SpiralCode-X/dataset_expansion/dataset_generator.py
- SpiralCode-X/scripts/github_crypto_mining.py
```

### Phase 2: Consolidate Core Modules
**Action:** Decide on canonical location for each module

**Decision Matrix:**
```
Module Type          | Keep Location        | Delete From
---------------------|----------------------|------------------
Analytical (CodeX)   | codex/               | SpiralCode-X/
Emotional (Nexus)    | nexus/               | SpiralBrain-Nexus/
Monitoring (Sensus)  | sensus/              | SpiralSensus/
Integration          | cortex/              | cortex_core/, spiral_cortex_core/
Shared utilities     | shared/              | Multiple locations
```

### Phase 3: Resolve Nested Duplications
**Action:** Flatten `codex/codex_core/` into `codex/core/`

**Move operations:**
```bash
codex/codex_core/temporal_moral_reasoner.py     → codex/temporal/
codex/codex_core/meta_ethical_framework.py      → codex/ethical_platform/
codex/codex_core/compliance_*.py                → codex/compliance/
codex/codex_core/integrity_proofs.py            → codex/utils/
codex/codex_core/knowledge_graph/               → codex/knowledge_graph/

# Delete empty codex/codex_core/
```

### Phase 4: Consolidate Scripts & Benchmarks
**Action:** Single canonical location for each category

**Proposed structure:**
```
benchmarks/              ← Keep root-level benchmarks
├── unified_cognition/
├── comparison/
└── validation/

scripts/                 ← Keep root-level scripts
├── irs_legal_intel/     ← Consolidate IRS scripts here
├── data_collection/
└── utils/

# Delete duplicates from:
# - codex/scripts/
# - SpiralCode-X/scripts/
# - SpiralCode-X/irs-legal-intel/scripts/
```

---

## Files Requiring Manual Review

### Uncertain Duplicates
These need human judgment to determine which version to keep:

1. **config.py** (5 versions) - May have different settings per lobe
2. **ensemble_cognitive_models.py** (5 versions) - May have evolved differently
3. **temporal_moral_reasoner.py** (4 versions) - Core ethical logic
4. **meta_ethical_framework.py** (4 versions) - Philosophical foundation
5. **compliance_validator.py** (4 versions) - Regulatory logic

**Recommendation:** Use git diff to compare versions, merge best features

### Integration Points
Files that bridge modules - keep all until integration testing:

1. `cortex/temporal/integration_demo.py`
2. `sensus/perception/integration_demo.py`
3. `spiral_cortex_core/` directory contents
4. `cortex_core/compat_v1.py`

---

## Summary Statistics

### Duplication Counts
- **Total duplicate groups:** 200+
- **High-priority (syntax errors):** 25+ files
- **Medium-priority (functional duplicates):** 50+ files
- **Low-priority (organizational):** 150+ files

### Storage Impact
- **Estimated duplicate storage:** ~500 MB - 1 GB
- **After culling estimate:** Save 300-500 MB

### Import Complexity
- **Broken imports:** Unknown until Phase 4 (import rebuilding)
- **Expected conflicts:** High (v1.0 imports won't work in v2.0 structure)

---

## Next Steps

1. ✅ **Document duplicates** (this report)
2. ⏭️ **Fix syntax errors** in critical files
3. ⏭️ **Delete corrupted v1.0 duplicates**
4. ⏭️ **Run integration tests** to identify functional dependencies
5. ⏭️ **Consolidate modules** per decision matrix
6. ⏭️ **Flatten nested structures** (codex_core, spiral_cortex_core)
7. ⏭️ **Rebuild imports** for new structure
8. ⏭️ **Run full test suite**

---

## Conclusion

The duplication is **extensive but manageable**. The total import successfully preserved all v1.0 components, allowing careful surgical culling based on:
- Functional testing results
- Version comparison (git diff)
- Integration requirements
- Architectural decisions

**Key Principle:** "Function Precedes Form" - Don't delete until integration testing proves what's actually needed.

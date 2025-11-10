# Deeply Nested Files Audit Report
**Date:** November 1, 2025  
**Repository:** SpiralCortex-v2.0  
**Audit Scope:** Files nested >4 directories deep (excluding .venv, node_modules, __pycache__, .git)

---

## Executive Summary

Comprehensive audit of deeply nested files revealed two main categories:
1. **176 benchmark result files** (7-10 levels deep) - **KEEP** for ML learning
2. **76 generated documentation site files** (5 levels deep) - **ADD TO .GITIGNORE**

---

## Category 1: External Benchmark Results ✅ KEEP

### Location
```
data/archive/results/external_benchmarks/neuroai_hub/big_bench_lite/bigbench/benchmark_tasks/
```

### Details
- **File Count:** 176 files (PDFs and PNGs)
- **Nesting Depth:** 9-10 directories
- **Date Created:** October 23, 2025
- **File Types:** Plot visualizations of benchmark performance

### Benchmark Tasks Evaluated (23 total)
1. abstract_narrative_understanding
2. bridging_anaphora_resolution_barqa
3. conceptual_combinations
4. context_definition_alignment
5. contextual_parametric_knowledge_conflicts
6. coqa_conversational_question_answering
7. evaluating_information_essentiality
8. formal_fallacies_syllogisms_negation
9. gender_inclusive_sentences_german
10. gender_sensitivity_chinese
11. gender_sensitivity_english
12. international_phonetic_alphabet_nli
13. international_phonetic_alphabet_transliterate
14. muslim_violence_bias
15. natural_instructions
16. salient_translation_error_detection
17. self_awareness
18. self_evaluation_tutoring
19. semantic_parsing_in_context_sparc
20. simple_arithmetic_json_multiple_choice
21. simple_arithmetic_multiple_targets_json
22. unnatural_in_context_learning
23. word_problems_on_sets_and_graphs

### Decision: **KEEP**

**Rationale:**
- Created October 23, 2025 - **Recent v2.0 benchmarks**, not v1.0 legacy
- Represents empirical performance data across diverse cognitive tasks
- Valuable for machine learning training and historical performance tracking
- Properly archived in `data/archive/results/` following repository conventions
- Supports cognitive architecture validation claims

**Integration Status:** ✅ Connected
- Benchmark runner exists: `benchmarks/external/neuroai_cognition_benchmarks.py`
- Uses adapter pattern: `benchmarks/external/adapter_template.py`
- Results properly archived in designated location

---

## Category 2: MkDocs Generated Site 🔧 ADD TO .GITIGNORE

### Location
```
docs/site/
```

### Details
- **File Count:** 76 files (HTML, JS, CSS, XML)
- **Nesting Depth:** 5 directories
- **Date Generated:** October 28, 2025
- **Source:** MkDocs static site generator (mkdocs.yml exists)

### Directory Structure
```
docs/site/
├── 404.html
├── index.html
├── sitemap.xml, sitemap.xml.gz
├── objects.inv
├── api/
├── architecture/
│   └── decision-records/ (ADRs 001-005)
├── assets/
│   └── javascripts/
│       └── lunr/min/ (30+ language files)
├── deployment/
├── development/
├── ethics/
├── patent/
│   └── drawings/
├── performance/
├── search/
└── use-cases/
```

### Decision: **ADD TO .GITIGNORE**

**Rationale:**
- Generated build artifacts from `mkdocs build`
- Can be regenerated from source markdown files in `docs/`
- Standard practice to exclude generated documentation from version control
- Reduces repository size and avoids merge conflicts
- GitHub Pages or other hosting can build on deployment

**Action Required:** Add `docs/site/` to `.gitignore`

---

## Category 3: Broken Legacy Scripts ❌ NEEDS FIX

### Files Affected
1. `tools/legacy_scripts/enhanced_empirical_cognition_study.py` (682 lines)
2. `tools/legacy_scripts/empirical_cognition_study.py` (452 lines)
3. `tools/legacy_scripts/perturbation_test.py` (commented import)

### Issue
All three files import from `external_benchmarks.neuroai_integration`:
```python
from external_benchmarks.neuroai_integration import NeuroAICognitionHub
```

**Problem:** This module **does not exist** in v2.0 repository structure.

### Root Cause
- v1.0 had `external_benchmarks/` as a top-level module directory
- v2.0 reorganized to `benchmarks/external/` structure
- Legacy scripts not updated during migration
- Module `NeuroAICognitionHub` never recreated or has different name

### Decision: **DOCUMENT AS DEPRECATED**

**Options:**
1. **Remove scripts** - They reference missing infrastructure
2. **Create integration bridge** - Recreate `NeuroAICognitionHub` in `benchmarks/external/`
3. **Document as deprecated** - Add clear status to `tools/legacy_scripts/README.md`

**Recommended:** Option 3 (Document) - Preserve historical code but mark clearly as non-functional pending v2.0 integration rewrite.

---

## Integration Plan for Disconnected Files

### Current Benchmark Integration (v2.0)
✅ **WORKING:**
- `benchmarks/external/neuroai_cognition_benchmarks.py` - Main runner
- `benchmarks/external/adapter_template.py` - Generic benchmark adapter
- `benchmarks/external/comfact_adapter.py` - ComFact-specific
- `benchmarks/external/goemotion_adapter.py` - GoEmotions-specific
- `benchmarks/external/crypto_adapter.py` - Crypto analysis
- `benchmarks/external/adapter_status.py` - Status tracking

### Missing Integration (v1.0 Legacy)
❌ **BROKEN:**
- `external_benchmarks/neuroai_integration.py` - **Does not exist**
- `NeuroAICognitionHub` class - **Not implemented in v2.0**

### Reintegration Requirements

To restore legacy scripts functionality:

1. **Create `benchmarks/external/neuroai_hub.py`:**
   ```python
   class NeuroAICognitionHub:
       """v2.0 compatible benchmark hub for empirical cognition studies."""
       def run_benchmark(self, benchmark_name: str):
           # Delegate to neuroai_cognition_benchmarks.py
           pass
   ```

2. **Update legacy script imports:**
   ```python
   # OLD (broken):
   from external_benchmarks.neuroai_integration import NeuroAICognitionHub
   
   # NEW (v2.0):
   from benchmarks.external.neuroai_hub import NeuroAICognitionHub
   ```

3. **Alternative:** Update scripts to use current adapter pattern directly

---

## Action Items

### Immediate Actions
- [x] Audit complete - All deeply nested files identified and categorized
- [ ] Add `docs/site/` to `.gitignore`
- [ ] Update `tools/legacy_scripts/README.md` with deprecation warnings
- [ ] Commit changes with clear documentation

### Future Integration Work
- [ ] Decide: Remove or restore legacy empirical cognition study scripts
- [ ] If restoring: Implement `NeuroAICognitionHub` v2.0 adapter
- [ ] If removing: Archive to `deprecated/` with explanation

### Documentation Updates
- [ ] Update `benchmarks/external/README.md` with integration architecture
- [ ] Document v1.0 → v2.0 benchmark migration path
- [ ] Add troubleshooting guide for legacy script users

---

## Conclusions

1. **External Benchmarks (176 files):** ✅ Keep - Valuable v2.0 performance data
2. **docs/site/ (76 files):** 🔧 Add to .gitignore - Build artifacts
3. **Legacy Scripts (3 files):** ❌ Document as broken - Missing v2.0 integration

**Overall Repository Health:** Good organizational structure with clear archival of results. Primary issue is incomplete migration documentation for v1.0 legacy scripts. No v1.0-specific content identified that requires removal.

**Deep Nesting Verdict:** Appropriate for benchmark result hierarchies (follows BigBench structure). Documentation site should not be committed (build artifacts).

# v1.0 Architecture Analysis: Module-based Brain Quadrants

**Date:** October 27, 2025  
**Purpose:** Understand v1.0's working architecture to properly migrate to v2.0  
**Key Insight:** v1.0 used independent modules with dynamic discovery - v2.0 merged into monolithic directories

---

## Critical Historical Clarification

**Exactly — that clarification is critical, and it aligns perfectly with what the internal documentation implies but never quite says outright.**

SpiralCortex **v1.0** (the "unofficial" version) wasn't a monolith—it was a *federation* of three autonomous cognitive subsystems, each capable of independent operation:

1. **SpiralCode-X** – the analytical, symbolic, rule-driven reasoning lobe; it handled structured cognition, ethical logic, and compliance analysis.
2. **SpiralBrain-Nexus** – the emotional-adaptive lobe; it embodied SEC vectors, biofeedback, and dynamic motivational weighting.
3. **SpiralSensus** – the perceptual-embodied lobe; it interpreted signals, telemetry, and pattern-level sensory coherence.

The **Cortex** in v1.0 wasn't a full lobe yet — it was a **connector and coordinator**, the "thin prefrontal bridge" that synchronized these three models. That's why so many of the old orchestration files (`integration_gating.py`, `lobe_registry.py`, etc.) appear to reference "external" lobes rather than internal modules.

---

## v1.0 Structure (Working Model)

```
SpiralCortex/  (Root repo - orchestration layer)
├── spiralcortex_core/          # Integration engine (lobe_registry, gating)
│   ├── lobe_registry.py        # Dynamic lobe discovery via META.yaml
│   ├── integration_gating.py   # AttentionGatingIntegrator
│   ├── realtime_adaptation.py  # Cross-lobe coordination
│   └── adaptive_integration_trainer.py
│
├── SpiralCode-X/               # Codex lobe (standalone module)
│   ├── core/                   # Pathways, models
│   ├── learning/               # Plasticity
│   ├── ethics/                 # Ethical reasoning
│   ├── analysis/               # Tax/crypto analysis
│   ├── pathways/               # Specialized pathways
│   ├── validation/             # Lobe-specific validation
│   └── [48 subdirectories]     # Full cognitive toolkit
│
├── SpiralBrain-Nexus/          # Nexus lobe (standalone module)
│   ├── core/                   # Training systems
│   ├── emotional/              # SEC protocol
│   ├── financial/              # Financial analysis
│   └── [20 subdirectories]     # Training/emotional systems
│
├── SpiralSensus/               # Sensus lobe (standalone module)
│   ├── spiralsensus/           # Core perception
│   └── examples/               # Usage examples
│
├── SpiralCortex/               # Cortex lobe (minimal - just lobes/)
│   └── lobes/                  # Lobe registration directory
│       └── spiralsensus/       # META.yaml for sensus
│
├── lobes/                      # Lobe discovery directory
│   └── spiralsensus/           # Lobe registration point
│
├── causal_introspection/       # Phase 5 feature (modular)
├── reflective_self_regulation/ # Phase 4 feature (modular)
├── temporal_self_consistency/  # Phase 6 feature (modular)
│
├── benchmarks/                 # Cross-lobe testing
├── tests/                      # Unit tests
└── [orchestration scripts]     # benchmark_unified_cognition.py, etc.
```

---

## Key Architecture Principles in v1.0

### 1. **Independent Module Design**

Each lobe was a **standalone Python package**:
- Own `requirements.txt` / `setup.py`
- Own test suite
- Own documentation
- Own internal structure
- Could be developed/tested independently
- Could be versioned independently

**Example:** SpiralCode-X was a complete module that could run without SpiralBrain-Nexus.

### 2. **Dynamic Lobe Registry**

**Core File:** `spiralcortex_core/lobe_registry.py`

```python
class LobeRegistry:
    """Dynamic lobe loader/registry.
    
    Supports META.yaml (preferred) or META.json.
    Discovers lobes at runtime, loads via entrypoint.
    """
    
    def register_lobe_dir(self, lobe_dir: Path) -> Dict[str, Any]:
        meta = self._load_meta(lobe_dir)  # Read META.yaml
        name = meta.get("name") or lobe_dir.name
        entrypoint = meta.get("entrypoint")
        module_obj, runner = self._load_entrypoint(lobe_dir, entrypoint)
        
        self.lobes[name] = {
            "meta": meta,
            "module": module_obj,
            "runner": runner,
            "path": str(lobe_dir),
        }
        return self.lobes[name]
```

**Benefits:**
- Lobes declare capabilities via META.yaml
- Runtime integration, not compile-time coupling
- Easy to add new lobes (just drop in lobes/ directory)
- Version-aware (META.yaml includes version)

### 3. **Integration Layer**

**Location:** `spiralcortex_core/`

**Purpose:** Coordinate communication between independent lobes

**Key Components:**
- `lobe_registry.py` - Discovery and loading
- `integration_gating.py` - `AttentionGatingIntegrator` for cross-lobe attention
- `realtime_adaptation.py` - `RealTimeAdapter` for dynamic coordination
- `adaptive_integration_trainer.py` - Learning optimal integration patterns

**Usage Pattern:**
```python
from spiralcortex_core.integration_gating import AttentionGatingIntegrator

# Unified benchmark imports integration layer
integrator = AttentionGatingIntegrator()
# Coordinates codex, nexus, sensus lobes
```

### 4. **Feature-Based Organization**

Advanced capabilities (Phases 4-6) lived as **modular features** at root:

```
causal_introspection/            # Phase 5: Why did I decide X?
reflective_self_regulation/      # Phase 4: Self-monitoring & adjustment
temporal_self_consistency/       # Phase 6: Past/present/future coherence
temporal_self_consistency_integration/
```

**Why at root:** These features span multiple lobes, so they're not "owned" by codex/nexus/sensus.

---

## v2.0 Current State (Problematic)

### ❌ What Got Lost in Migration

#### 1. **Module Independence Collapsed**

**v1.0:** SpiralCode-X was standalone (48 subdirectories)  
**v2.0:** Merged into `codex/` with 33 subdirectories

**Problem:** 
- Lost clean module boundaries
- Can't version codex independently
- Can't test codex in isolation
- Unclear what's codex-specific vs shared

#### 2. **Dynamic Discovery Removed**

**v1.0:** `LobeRegistry` + META.yaml files  
**v2.0:** Hard-coded imports

**Problem:**
```python
# v1.0 (dynamic)
registry = LobeRegistry()
registry.discover_and_register()  # Finds all lobes
codex = registry.get_module("SpiralCode-X")

# v2.0 (hard-coded)
from codex.core.something import something
from nexus.core.something import something
# Must manually track all cross-lobe dependencies
```

#### 3. **Integration Layer Lost**

**v1.0:** Clear integration in `spiralcortex_core/`  
**v2.0:** Integration logic unclear - where is `AttentionGatingIntegrator`?

**Problem:**
- `cortex_core/` at root has only `compat_v1.py`
- No clear equivalent to `lobe_registry.py`
- Cross-lobe coordination mechanism unclear

#### 4. **Structural Duplication**

**v2.0 has confusing duplications:**

```
SpiralCortex-v2.0/
├── validation/              # Top-level validation
├── codex/validation/        # Codex validation
├── nexus/validation/        # Nexus validation
├── cortex/validation/       # Cortex validation
└── sensus/validation/       # Sensus validation

├── analysis/                # Top-level analysis
└── codex/analysis/          # Codex analysis

├── cortex_core/             # What is this?
└── cortex/core/             # Or this?
```

**Unclear:**
- Which is authoritative?
- Should lobes have their own validation or shared?
- What belongs at root vs in lobes?

---

## Proposed v2.0 Architecture (Brain Quadrants Model)

### Design Philosophy

**The brain has 4 specialized regions that must coordinate:**

1. **Cortex** - Integration & orchestration (coordinates the other 3)
2. **Codex** - Analytical reasoning (logic, analysis, pathways)
3. **Nexus** - Emotional/training (SEC, biofeedback, plasticity)
4. **Sensus** - Perception/monitoring (real-time data, sensors)

**Key insight:** Cortex is not "just another lobe" - it's the **integration layer** that makes the other 3 work together.

---

### Recommended Structure

```
SpiralCortex-v2.0/
│
├── cortex/                        # Integration & Orchestration (The Coordinator)
│   ├── core/                      # Integration engine
│   │   ├── lobe_registry.py       # Dynamic lobe discovery (from v1.0)
│   │   ├── integration_gating.py  # AttentionGatingIntegrator (from v1.0)
│   │   ├── realtime_adaptation.py # Cross-lobe coordination (from v1.0)
│   │   └── adaptive_trainer.py    # Learning integration patterns
│   │
│   ├── lobes/                     # Lobe discovery directory
│   │   ├── codex/                 # Codex META.yaml
│   │   ├── nexus/                 # Nexus META.yaml
│   │   └── sensus/                # Sensus META.yaml
│   │
│   ├── features/                  # Advanced cross-lobe features (Phases 4-6)
│   │   ├── causal_introspection/
│   │   ├── reflective_self_regulation/
│   │   └── temporal_self_consistency/
│   │
│   └── validation/                # Integration validation
│       └── benchmark_unified_cognition.py
│
├── codex/                         # Codex Lobe (Analytical Reasoning)
│   ├── META.yaml                  # Lobe metadata (name, version, entrypoint)
│   ├── core/                      # Core pathways & models
│   ├── pathways/                  # Specialized reasoning pathways
│   ├── learning/                  # Cognitive plasticity
│   ├── ethics/                    # Ethical reasoning
│   ├── analysis/                  # Tax/crypto analysis
│   ├── temporal/                  # Temporal reasoning
│   ├── validation/                # Codex-specific validation
│   └── ...                        # Other codex components
│
├── nexus/                         # Nexus Lobe (Emotional & Training)
│   ├── META.yaml
│   ├── core/                      # Training systems
│   ├── emotional/                 # SEC protocol, emotion modulation
│   ├── learning/                  # Continuous learning, biofeedback
│   ├── financial/                 # Financial emotional analysis
│   ├── validation/                # Nexus-specific validation
│   └── ...
│
├── sensus/                        # Sensus Lobe (Perception & Monitoring)
│   ├── META.yaml
│   ├── core/                      # Perception engine
│   ├── perception/                # Sensory processing
│   ├── services/                  # Real-time data services
│   ├── validation/                # Sensus-specific validation
│   └── ...
│
├── shared/                        # Cross-Lobe Shared Infrastructure
│   ├── compliance/                # Regulatory (spans all lobes)
│   ├── config/                    # Configuration management
│   ├── security/                  # Security/auth
│   └── utils/                     # Common utilities
│
├── benchmarks/                    # Cross-lobe testing
├── tests/                         # Unit tests
├── tools/                         # Development tools
├── docs/                          # Documentation
└── data/                          # Shared data
```

---

## Key Design Decisions

### 1. **Cortex = Integration Hub, Not a 4th Lobe**

**v1.0 had:** `spiralcortex_core/` as integration layer  
**v2.0 should have:** `cortex/` as integration layer (not just another lobe)

**Cortex responsibilities:**
- Discover and register lobes (via META.yaml)
- Coordinate cross-lobe communication
- Provide integration features (Phases 4-6)
- Orchestrate unified cognition

**Cortex does NOT:**
- Duplicate lobe functionality
- Contain its own "cognitive pathways"
- Compete with codex/nexus/sensus

### 2. **Each Lobe = Independent Module**

**Restore v1.0 independence:**

```
codex/
├── META.yaml              # Declares: name, version, entrypoint, capabilities
├── setup.py               # Independent package
├── requirements.txt       # Own dependencies
└── [internal structure]   # Self-contained
```

**Benefits:**
- Can version codex/nexus/sensus independently
- Can test each lobe in isolation
- Clear ownership boundaries
- Can develop lobes in parallel

### 3. **Lobe-Specific vs Shared Resources**

**Lobe-specific (inside codex/nexus/sensus):**
- `validation/` - Lobe-specific tests (e.g., crypto tax accuracy for codex)
- `core/` - Lobe-specific core logic
- `models/` - Lobe-specific models

**Shared (at root or in shared/):**
- `compliance/` - Regulatory framework spans all lobes
- `config/` - Unified configuration
- `benchmarks/` - Cross-lobe integration tests
- `tools/` - Development utilities

**Top-level validation/ should NOT exist** - it's either:
- In `cortex/validation/` for integration tests, OR
- In each lobe's `validation/` for lobe-specific tests

### 4. **Dynamic Discovery via META.yaml**

**Restore v1.0's LobeRegistry pattern:**

```yaml
# codex/META.yaml
name: codex
version: 2.0.0
description: Analytical reasoning lobe
entrypoint: codex.core.main:run
capabilities:
  - tax_analysis
  - pathway_reasoning
  - ethical_decision_making
dependencies:
  - numpy>=1.24
  - torch>=2.0
```

**Runtime usage:**
```python
from cortex.core.lobe_registry import LobeRegistry

registry = LobeRegistry()
registry.discover_and_register()  # Finds all lobes with META.yaml

# Get specific lobe
codex = registry.get_module("codex")
codex_runner = registry.get_runner("codex")

# Or get all registered lobes
for lobe_name in registry.lobes:
    meta = registry.get_meta(lobe_name)
    print(f"Loaded {lobe_name} v{meta['version']}")
```

---

## Migration Path

### Option 1: Incremental Refactor (Safer)

**Keep v2.0 running while reorganizing:**

1. **Phase 1:** Create proper cortex structure
   - Copy v1.0 `spiralcortex_core/` → `cortex/core/`
   - Restore `LobeRegistry`, `AttentionGatingIntegrator`
   - Update import paths in cortex files only

2. **Phase 2:** Add META.yaml to existing lobes
   - Create `codex/META.yaml`
   - Create `nexus/META.yaml`
   - Create `sensus/META.yaml`
   - Test discovery without changing lobe internals

3. **Phase 3:** Consolidate duplicates
   - Remove top-level `validation/`, `analysis/`, `cortex_core/`
   - Document what moved where
   - Update imports incrementally

4. **Phase 4:** Move advanced features to cortex
   - Create `cortex/features/`
   - Move Phase 4-6 implementations
   - Update cross-lobe feature imports

5. **Phase 5:** Create shared/ directory
   - Move compliance, config to shared/
   - Update all lobe imports

### Option 2: Clean Slate (Faster but Riskier)

**Start with correct structure, migrate code in:**

1. **Create new structure**
   ```bash
   mkdir -p cortex/core cortex/lobes cortex/features
   mkdir -p codex nexus sensus shared
   ```

2. **Copy v1.0 integration layer**
   ```bash
   cp -r v1.0/spiralcortex_core/* v2.0/cortex/core/
   ```

3. **Extract each lobe from current v2.0**
   - Keep codex/ mostly as-is (just add META.yaml)
   - Keep nexus/ mostly as-is (just add META.yaml)
   - Keep sensus/ mostly as-is (just add META.yaml)

4. **Move cross-cutting concerns**
   - compliance/ → shared/compliance/
   - config/ → shared/config/
   - Top-level validation/ → DELETE (use lobe-specific)

5. **Test each lobe independently**
   ```bash
   cd codex && pytest
   cd nexus && pytest
   cd sensus && pytest
   ```

6. **Test integration**
   ```bash
   python cortex/validation/benchmark_unified_cognition.py
   ```

---

## Critical Files to Migrate

### From v1.0 spiralcortex_core/ → v2.0 cortex/core/

| v1.0 File | Purpose | v2.0 Location |
|-----------|---------|---------------|
| `lobe_registry.py` | Dynamic lobe discovery | `cortex/core/lobe_registry.py` |
| `integration_gating.py` | AttentionGatingIntegrator | `cortex/core/integration_gating.py` |
| `realtime_adaptation.py` | RealTimeAdapter | `cortex/core/realtime_adaptation.py` |
| `adaptive_integration_trainer.py` | Learning integration | `cortex/core/adaptive_trainer.py` |

### From v1.0 root → v2.0 cortex/features/

| v1.0 Directory | Purpose | v2.0 Location |
|----------------|---------|---------------|
| `causal_introspection/` | Phase 5 feature | `cortex/features/causal_introspection/` |
| `reflective_self_regulation/` | Phase 4 feature | `cortex/features/reflective_self_regulation/` |
| `temporal_self_consistency/` | Phase 6 feature | `cortex/features/temporal_self_consistency/` |

---

## Import Pattern Changes

### Current v2.0 (Problematic)
```python
# Hard-coded, brittle
from codex.core.something import Something
from nexus.core.something import Something
```

### Proposed v2.0 (Dynamic)
```python
# Via registry - flexible
from cortex.core.lobe_registry import LobeRegistry

registry = LobeRegistry()
registry.discover_and_register()

codex = registry.get_module("codex")
result = codex.analyze_portfolio(...)
```

### Lobe-Internal Imports (Stay the Same)
```python
# Within codex
from codex.pathways.pattern_recognition import PatternRecognitionPathway
from codex.learning.plasticity import PlasticitySystem
```

---

## Testing Strategy

### 1. **Lobe Isolation Tests**
Each lobe should have its own test suite:
```bash
cd codex && pytest tests/
cd nexus && pytest tests/
cd sensus && pytest tests/
```

### 2. **Integration Tests**
Cortex validates cross-lobe coordination:
```bash
python cortex/validation/benchmark_unified_cognition.py
python benchmarks/run_all_benchmarks.py
```

### 3. **Feature Tests**
Phase 4-6 features have their own validation:
```bash
python cortex/features/causal_introspection/validate.py
python cortex/features/reflective_self_regulation/validate.py
```

---

## Decision Required

**Which migration approach do you prefer?**

**Option 1: Incremental Refactor**
- ✅ Safer - keep v2.0 working throughout
- ✅ Can test each step
- ❌ Slower - more intermediate states
- ❌ May accumulate tech debt if we stop mid-migration

**Option 2: Clean Slate**
- ✅ Faster - get to correct structure quickly
- ✅ Forces us to think through all design decisions
- ❌ Riskier - v2.0 may be broken during migration
- ❌ Need to test everything at once

**Or Option 3: Hybrid?**
- Create correct structure (new directories)
- Move v1.0 integration layer first (cortex/core/)
- Then incrementally move lobe content
- This gives us the destination but allows incremental progress

---

## Success Criteria

**Migration is complete when:**

1. ✅ `LobeRegistry` works - can discover codex/nexus/sensus via META.yaml
2. ✅ Each lobe can be tested independently
3. ✅ Integration tests pass (benchmark_unified_cognition)
4. ✅ No top-level duplicates (validation, analysis, cortex_core)
5. ✅ Phases 4-6 features organized in cortex/features/
6. ✅ Import paths use registry pattern, not hard-coded
7. ✅ All v1.0 benchmarks ported and passing

**Most important:** The structure **matches your cognitive model** - independent specialized lobes coordinated by an integration cortex.

---

## Next Steps

1. **Decide migration approach** (Option 1, 2, or 3)
2. **Create cortex/core/ structure** and restore integration layer
3. **Add META.yaml** to each lobe
4. **Test lobe discovery** before moving any code
5. **Incrementally consolidate** duplicates
6. **Validate** at each step

What's your preference for proceeding?

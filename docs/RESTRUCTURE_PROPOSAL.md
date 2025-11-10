# SpiralCortex-v2.0 Folder Restructuring Proposal
**Date:** November 1, 2025  
**Purpose:** Reduce nesting, enable full-brain domain processing

---

## Problem Statement

Domain-specific features (tax, blockchain, compliance, ethics) are currently **deeply nested inside Codex subdirectories**, making them:
- Harder to discover
- Conceptually isolated to one lobe
- Unable to leverage full four-lobe processing

**Current nesting:**
```
codex/tax_engine/crypto_tax_analyzer.py           # 3 levels deep
codex/irs-legal-intel/schemas/form_8949.py        # 4 levels deep
codex/blockchain/contract_analyzer.py             # 3 levels deep
codex/compliance/compliance_gateway.py            # 3 levels deep
codex/ethics/ethical_reasoning_integration.py     # 3 levels deep
```

---

## Solution: Flatten Domain Logic, Keep Infrastructure

**Move domain features OUT** of nested Codex folders → **Create top-level `domains/`**  
**Keep infrastructure IN** Codex (api, core, services, pathways, learning)

---

## Proposed Structure

```
SpiralCortex-v2.0/
│
├── domains/                  # ← NEW: Domain-specific features (full-brain processing)
│   ├── tax/
│   │   ├── crypto_tax_analyzer.py            # FROM codex/tax_engine/
│   │   ├── multi_jurisdictional_tax_engine.py
│   │   ├── irs_8949_reconciliation.py
│   │   ├── tax_optimization_engine.py
│   │   └── legal/                            # FROM codex/irs-legal-intel/
│   │       ├── schemas/
│   │       └── scripts/
│   │
│   ├── blockchain/
│   │   ├── contract_analyzer.py              # FROM codex/blockchain/
│   │   ├── wallet_parser.py
│   │   ├── etherscan_provider.py
│   │   └── service.py
│   │
│   └── compliance/
│       ├── compliance_gateway.py             # FROM codex/compliance/
│       ├── compliance_checker.py
│       └── audit_trail_manager.py
│
├── nexus/
│   └── ethics/               # ← MOVED FROM codex/ethics/
│       ├── ethical_reasoning_integration.py
│       ├── temporal_ethics_service.py
│       └── meta_ethical_framework.py         # FROM codex/codex_core/
│
├── codex/                    # Analytical reasoning lobe (INFRASTRUCTURE ONLY)
│   ├── api/                  # REST API layer
│   ├── core/                 # Main servers, models
│   ├── codex_core/           # Core analytical models
│   ├── services/             # Service implementations
│   ├── pathways/             # Cognitive routing
│   ├── integration/          # External system adapters
│   ├── learning/             # Adaptive learning
│   └── validation/           # Data validation
│
├── sensus/                   # Perception lobe
├── cortex/                   # Executive oversight lobe
├── benchmarks/
├── tests/
├── tools/
└── showcases/
```

---

## Files to Move

### 1. Tax Domain (22 files)
**FROM:** `codex/tax_engine/` → **TO:** `domains/tax/`
- crypto_tax_analyzer.py
- multi_jurisdictional_tax_engine.py
- irs_8949_reconciliation.py
- tax_optimization_engine.py
- high_performance_tax_engine.py
- rule_based_tax_calculator.py
- tax_lot_engine.py
- (+ 6 more tax scripts)

**FROM:** `codex/irs-legal-intel/` → **TO:** `domains/tax/legal/`
- schemas/ (directory)
- scripts/ (directory)

### 2. Blockchain Domain (15 files)
**FROM:** `codex/blockchain/` → **TO:** `domains/blockchain/`
- contract_analyzer.py
- wallet_parser.py
- etherscan_provider.py
- provider_base.py
- blockchain_service.py
- stream_service.py
- router.py
- api_router.py
- (+ 7 more blockchain scripts)

### 3. Compliance Domain (13 files)
**FROM:** `codex/compliance/` → **TO:** `domains/compliance/`
- compliance_gateway.py
- compliance_checker.py
- audit_trail_manager.py
- audit_persistence.py
- audit_event_schemas.py
- certification_bundle_generator.py
- (+ 7 more compliance scripts)

### 4. Ethics Domain (9 files)
**FROM:** `codex/ethics/` → **TO:** `nexus/ethics/`
- ethical_reasoning_integration.py
- temporal_ethics_service.py
- ethical_monitoring_dashboard.py
- ethical_decision_scorer.py
- ethical_learning_loop.py
- ethics_metrics_collector.py
- (+ 3 more ethics scripts)

**FROM:** `codex/codex_core/meta_ethical_framework.py` → **TO:** `nexus/ethics/framework/`
**FROM:** `codex/specialized/temporal_moral_reasoner.py` → **TO:** `nexus/ethics/temporal/`

---

## What Stays in Codex (229 files)

**These are Codex-specific infrastructure, NOT domain logic:**

| Directory | Files | Purpose |
|-----------|-------|---------|
| `codex/root/` | 34 | Core Codex functionality |
| `codex/codex_core/` | 28 | Analytical models, SpiralCode-X |
| `codex/api/` | 21 | REST API routers |
| `codex/core/` | 21 | Main servers (main.py, etc.) |
| `codex/services/` | 12 | Service layer implementations |
| `codex/integration/` | 12 | External system adapters |
| `codex/pathways/` | 9 | Cognitive pathway routing |
| `codex/learning/` | 8 | Adaptive learning systems |
| `codex/validation/` | 9 | Input validation utilities |
| `codex/specialized/` | ~75 | Keep domain-agnostic analyzers |

---

## Import Path Updates

### Before (Nested)
```python
from codex.tax_engine.crypto_tax_analyzer import CryptoTaxAnalyzer
from codex.blockchain.contract_analyzer import ContractAnalyzer
from codex.compliance.compliance_gateway import ComplianceGateway
from codex.ethics.ethical_reasoning_integration import EthicalReasoningIntegrator
```

### After (Flat)
```python
from domains.tax.crypto_tax_analyzer import CryptoTaxAnalyzer
from domains.blockchain.contract_analyzer import ContractAnalyzer
from domains.compliance.compliance_gateway import ComplianceGateway
from nexus.ethics.ethical_reasoning_integration import EthicalReasoningIntegrator
```

### Backward Compatibility (3-month shim)
```python
# codex/tax_engine/__init__.py
"""
DEPRECATED: Use domains.tax instead.
This shim will be removed in v2.1 (February 2026).
"""
import warnings
from domains.tax.crypto_tax_analyzer import CryptoTaxAnalyzer

warnings.warn(
    "codex.tax_engine is deprecated. Import from domains.tax instead.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ['CryptoTaxAnalyzer']
```

---

## Migration Steps

### Step 1: Create New Directories (5 minutes)
```powershell
mkdir domains
mkdir domains\tax
mkdir domains\tax\legal
mkdir domains\blockchain
mkdir domains\compliance
mkdir nexus\ethics
mkdir nexus\ethics\framework
mkdir nexus\ethics\temporal
```

### Step 2: Move Files (10 minutes)
```powershell
# Tax domain
Move-Item codex\tax_engine\*.py domains\tax\
Move-Item codex\irs-legal-intel domains\tax\legal

# Blockchain domain
Move-Item codex\blockchain\*.py domains\blockchain\

# Compliance domain
Move-Item codex\compliance\*.py domains\compliance\

# Ethics to Nexus
Move-Item codex\ethics\*.py nexus\ethics\
Move-Item codex\codex_core\meta_ethical_framework.py nexus\ethics\framework\
Move-Item codex\specialized\temporal_moral_reasoner.py nexus\ethics\temporal\
```

### Step 3: Update Imports (20 minutes)
```powershell
# Find all Python files that import from moved modules
Get-ChildItem -Recurse -Filter "*.py" | Select-String "from codex.tax_engine|from codex.blockchain|from codex.compliance|from codex.ethics"

# Use find-and-replace:
# codex.tax_engine → domains.tax
# codex.blockchain → domains.blockchain
# codex.compliance → domains.compliance
# codex.ethics → nexus.ethics
```

### Step 4: Create Compatibility Shims (10 minutes)
```powershell
# Create __init__.py in old locations with deprecation warnings
```

### Step 5: Test All Entry Points (15 minutes)
```powershell
# Run showcases
python showcases\spiralcortex_analytical_reasoning.py
python showcases\spiralcortex_emotional_intelligence.py

# Check services
python check_services.py

# Run tests
pytest tests\
```

**Total Time: ~60 minutes**

---

## Benefits

### 1. **Clarity**
```
Before: codex/tax_engine/crypto_tax_analyzer.py
After:  domains/tax/crypto_tax_analyzer.py

Immediately clear this is a DOMAIN feature, not Codex infrastructure
```

### 2. **Discoverability**
```
domains/
├── tax/           ← "Oh, there's tax functionality"
├── blockchain/    ← "Oh, there's blockchain functionality"
└── compliance/    ← "Oh, there's compliance functionality"
```

### 3. **Full-Brain Ready**
Now it's natural to process `domains/tax/` through all four lobes:
```python
# domains/tax/crypto_tax_analyzer.py
def analyze_transactions(transactions):
    # Step 1: Sensus perceives patterns
    sensus_features = sensus.perceive(transactions)
    
    # Step 2: Codex calculates tax
    codex_tax = codex.calculate_tax(transactions, sensus_features)
    
    # Step 3: Nexus evaluates ethics
    nexus_ethics = nexus.evaluate_ethics(codex_tax)
    
    # Step 4: Cortex coordinates decision
    return cortex.integrate(sensus_features, codex_tax, nexus_ethics)
```

### 4. **Reduced Nesting**
```
Before: 3-4 levels deep
After:  2 levels deep (domains/tax/file.py)
```

---

## Risks & Mitigation

| Risk | Mitigation |
|------|------------|
| **Import breakage** | Compatibility shims for 3 months |
| **Lost during move** | Git tracks all file moves |
| **Tests fail** | Run full test suite after migration |
| **Users confused** | Update README with new structure |

---

## Decision: Approve or Defer?

**This restructuring:**
- ✅ Reduces nesting (3-4 levels → 2 levels)
- ✅ Clarifies domain vs infrastructure
- ✅ Enables full-brain processing patterns
- ✅ Takes ~60 minutes to execute
- ✅ Maintains backward compatibility (3 months)

**Ready to proceed?**
- [ ] Yes - execute restructuring now
- [ ] Yes with modifications - (specify changes)
- [ ] Defer - need more planning

---

**Prepared by:** GitHub Copilot  
**Execution Time:** ~60 minutes  
**Rollback:** Git revert if issues arise

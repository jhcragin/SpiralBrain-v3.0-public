# Full-Brain Integration Architecture Proposal
**Date:** November 1, 2025  
**Version:** 1.0  
**Status:** Proposal for Review

---

## Executive Summary

This document proposes restructuring SpiralBrain-v2.0 from **standalone Codex modules** to **full four-lobe brain integration**, where complex domain tasks (tax analysis, blockchain processing, compliance evaluation, ethical reasoning) flow through all cognitive lobes rather than being isolated in Codex subdirectories.

**Current State:** Domain-specific modules nested in `codex/` subdirectories operate largely independently  
**Proposed State:** Domain modules become **system-wide orchestrators** that leverage all four lobes for comprehensive cognitive processing

---

## Architectural Vision

### The Spiral Mind Principle

Just as the human brain doesn't isolate financial planning to one region, SpiralBrain-v2.0 should integrate:

1. **Sensus (Perception)** - Perceive data patterns, market signals, regulatory documents
2. **Codex (Analysis)** - Perform logical reasoning, tax calculations, compliance checks
3. **Nexus (Emotional/Ethical)** - Evaluate emotional context, ethical implications, stakeholder impact
4. **Cortex (Metacognition)** - Coordinate decision-making, regulate outputs, ensure coherence

**Example Flow - Tax Analysis:**

```
IRS Form 8949 Analysis Request
        ↓
[1] SENSUS perceives transaction patterns, document structure
        ↓
[2] CODEX performs tax calculations, applies IRS rules
        ↓
[3] NEXUS evaluates ethical implications, taxpayer sentiment
        ↓
[4] CORTEX coordinates final recommendation, confidence assessment
        ↓
Integrated Tax Analysis Output
```

---

## Current Architecture Analysis

### Codex Subdirectories (15 folders, 279 scripts)

| Directory | Scripts | Current Scope | Integration Potential |
|-----------|---------|---------------|----------------------|
| **codex/root** | 34 | Core Codex files | Keep as Codex internals |
| **codex/codex_core** | 28 | Core analytical models | Keep as Codex internals |
| **codex/api** | 21 | REST API layer | Keep as Codex service layer |
| **codex/core** | 21 | Main servers | Keep as Codex entry points |
| **codex/specialized** | 15 | Domain analyzers | **→ ELEVATE to `domains/`** |
| **codex/blockchain** | 15 | Blockchain analysis | **→ ELEVATE to `domains/blockchain/`** |
| **codex/tax_engine** | 13 | Tax computation | **→ ELEVATE to `domains/tax/`** |
| **codex/compliance** | 13 | Compliance checking | **→ ELEVATE to `domains/compliance/`** |
| **codex/services** | 12 | Service layers | Keep as Codex services |
| **codex/integration** | 12 | External connectors | Keep as Codex integration |
| **codex/pathways** | 9 | Cognitive pathways | Keep as Codex internals |
| **codex/validation** | 9 | Data validation | Keep as shared utility |
| **codex/irs-legal-intel** | 9 | IRS tax code | **→ ELEVATE to `domains/tax/legal/`** |
| **codex/ethics** | 9 | Ethical reasoning | **→ MOVE to `nexus/ethics/`** |
| **codex/learning** | 8 | Adaptive learning | Keep as Codex learning |

### Key Insight

**Infrastructure** (api, core, services, pathways, learning) → **Keep in Codex**  
**Domain Logic** (tax, blockchain, compliance, ethics) → **Elevate to full-brain orchestrators**

---

## Proposed Architecture

### New Directory Structure

```
SpiralBrain-v2.0/
├── codex/                    # Analytical reasoning lobe (INFRASTRUCTURE)
│   ├── api/                  # REST API layer
│   ├── core/                 # Main servers, models
│   ├── codex_core/           # Core analytical capabilities
│   ├── services/             # Service implementations
│   ├── pathways/             # Cognitive routing
│   ├── integration/          # External system adapters
│   ├── learning/             # Adaptive learning systems
│   └── validation/           # Data validation utilities
│
├── nexus/                    # Emotional/ethical intelligence lobe
│   ├── ethics/               # ← MOVE FROM codex/ethics/
│   │   ├── ethical_reasoning_integration.py
│   │   ├── temporal_ethics_service.py
│   │   ├── ethical_monitoring_dashboard.py
│   │   └── meta_ethical_framework.py (from codex/codex_core/)
│   ├── cognitive/
│   ├── emotional/
│   └── reflective/
│
├── sensus/                   # Perception lobe
│   ├── vision/
│   ├── audio/
│   └── data_perception/      # ← NEW: Data pattern perception
│       ├── market_perception.py
│       ├── document_perception.py
│       └── transaction_perception.py
│
├── cortex/                   # Executive oversight lobe
│   ├── metacognition/
│   ├── coordination/
│   └── integration/          # Cross-lobe orchestration
│       ├── integration_gating.py (existing)
│       └── domain_orchestrators.py (new)
│
├── domains/                  # ← NEW: System-wide domain orchestrators
│   ├── tax/                  # Full-brain tax analysis
│   │   ├── __init__.py
│   │   ├── orchestrator.py          # Main entry point
│   │   ├── engines/                 # ← FROM codex/tax_engine/
│   │   │   ├── crypto_tax_analyzer.py
│   │   │   ├── multi_jurisdictional_tax_engine.py
│   │   │   ├── irs_8949_reconciliation.py
│   │   │   └── tax_optimization_engine.py
│   │   └── legal/                   # ← FROM codex/irs-legal-intel/
│   │       ├── schemas/
│   │       └── scripts/
│   │
│   ├── blockchain/           # Full-brain blockchain analysis
│   │   ├── __init__.py
│   │   ├── orchestrator.py          # Main entry point
│   │   ├── analyzers/               # ← FROM codex/blockchain/
│   │   │   ├── contract_analyzer.py
│   │   │   ├── wallet_parser.py
│   │   │   └── etherscan_provider.py
│   │   └── services/
│   │       ├── blockchain_service.py
│   │       └── stream_service.py
│   │
│   ├── compliance/           # Full-brain compliance evaluation
│   │   ├── __init__.py
│   │   ├── orchestrator.py          # Main entry point
│   │   ├── gateways/                # ← FROM codex/compliance/
│   │   │   ├── compliance_gateway.py
│   │   │   ├── compliance_checker.py
│   │   │   └── audit_trail_manager.py
│   │   └── reporting/
│   │       └── compliance_reporting.py
│   │
│   └── specialized/          # Other domain orchestrators
│       ├── forensics/
│       ├── forecasting/
│       └── knowledge_graphs/
│
├── integration/              # Cross-system integration (existing)
└── showcases/                # Full-brain demonstrations (existing)
```

---

## Full-Brain Integration Patterns

### Pattern 1: Domain Orchestrator Class

Every domain gets an orchestrator that routes through all four lobes:

```python
# domains/tax/orchestrator.py

from typing import Dict, Any, List
from sensus.data_perception.transaction_perception import TransactionPerceptor
from codex.tax_engine.crypto_tax_analyzer import CryptoTaxAnalyzer
from nexus.ethics.ethical_reasoning_integration import EthicalReasoningIntegrator
from cortex.integration.integration_gating import AttentionGatingIntegrator

class TaxAnalysisOrchestrator:
    """
    Full-brain tax analysis orchestrator.
    Routes tax analysis requests through all four cognitive lobes.
    """
    
    def __init__(self):
        # Initialize all four lobes
        self.sensus_perceptor = TransactionPerceptor()
        self.codex_analyzer = CryptoTaxAnalyzer()
        self.nexus_ethics = EthicalReasoningIntegrator()
        self.cortex_coordinator = AttentionGatingIntegrator()
    
    def analyze_crypto_transactions(
        self, 
        transactions: List[Dict[str, Any]],
        tax_year: int,
        jurisdiction: str = "US"
    ) -> Dict[str, Any]:
        """
        Process crypto transactions through full brain stack.
        
        Pipeline:
        1. SENSUS: Perceive transaction patterns, identify anomalies
        2. CODEX: Calculate tax obligations, apply IRS rules
        3. NEXUS: Evaluate ethical implications, taxpayer impact
        4. CORTEX: Coordinate final decision, confidence assessment
        """
        
        # Step 1: SENSUS - Perceive transaction patterns
        sensus_output = self.sensus_perceptor.perceive_transactions(
            transactions=transactions,
            context={
                "tax_year": tax_year,
                "jurisdiction": jurisdiction
            }
        )
        
        # Step 2: CODEX - Perform tax calculations
        codex_output = self.codex_analyzer.analyze(
            transactions=transactions,
            perceptual_features=sensus_output["features"],
            jurisdiction=jurisdiction
        )
        
        # Step 3: NEXUS - Evaluate ethical implications
        nexus_output = self.nexus_ethics.evaluate(
            decision_context={
                "type": "tax_analysis",
                "tax_burden": codex_output["total_tax"],
                "optimization_options": codex_output["optimizations"],
                "stakeholder_impact": sensus_output["impact_assessment"]
            }
        )
        
        # Step 4: CORTEX - Coordinate final output
        cortex_output = self.cortex_coordinator.integrate(
            lobe_outputs={
                "sensus": sensus_output,
                "codex": codex_output,
                "nexus": nexus_output
            },
            decision_context={
                "complexity": sensus_output["complexity"],
                "confidence_threshold": 0.8
            }
        )
        
        return {
            "tax_analysis": codex_output,
            "ethical_evaluation": nexus_output,
            "perception_insights": sensus_output,
            "integrated_decision": cortex_output,
            "confidence": cortex_output["confidence"],
            "reasoning_trace": cortex_output["reasoning_trace"]
        }
```

### Pattern 2: Lobe-Specific Contributions

Each lobe contributes its expertise:

#### **SENSUS Contributions** (Perception)
- **Tax Domain:**
  - Perceive transaction patterns (clustering, anomaly detection)
  - Detect data quality issues (missing cost basis, incorrect dates)
  - Identify seasonal patterns in trading behavior
  
- **Blockchain Domain:**
  - Perceive on-chain patterns (whale movements, gas price trends)
  - Detect smart contract interactions (DeFi, NFT patterns)
  - Monitor mempool dynamics
  
- **Compliance Domain:**
  - Perceive document structure (regulatory forms, reports)
  - Detect language patterns in policies
  - Monitor real-time regulatory feeds

#### **CODEX Contributions** (Analysis)
- **Tax Domain:**
  - Calculate tax obligations (FIFO, LIFO, specific ID)
  - Apply IRS rules (wash sales, staking income, airdrops)
  - Optimize tax strategies (harvesting, basis selection)
  
- **Blockchain Domain:**
  - Analyze smart contracts (security, functionality)
  - Compute wallet valuations
  - Assess DeFi protocol risks
  
- **Compliance Domain:**
  - Check regulatory requirements (KYC, AML, GDPR)
  - Validate audit trails
  - Generate compliance reports

#### **NEXUS Contributions** (Emotional/Ethical)
- **Tax Domain:**
  - Evaluate fairness of tax optimization strategies
  - Consider taxpayer emotional state (stress, confusion)
  - Assess stakeholder impact (government revenue, taxpayer burden)
  
- **Blockchain Domain:**
  - Evaluate ethical implications of DeFi protocols
  - Consider societal impact of crypto adoption
  - Assess environmental concerns (PoW vs PoS)
  
- **Compliance Domain:**
  - Evaluate privacy vs transparency tradeoffs
  - Consider stakeholder rights (data subjects, regulators)
  - Assess societal implications of compliance requirements

#### **CORTEX Contributions** (Metacognition)
- **All Domains:**
  - Coordinate lobe outputs into coherent decisions
  - Regulate confidence based on uncertainty
  - Detect contradictions between lobe outputs
  - Adjust reasoning strategies based on context
  - Maintain audit trails for explainability

---

## Migration Strategy

### Phase 1: Create Domain Orchestrators (Week 1)

**Goals:**
- Create `domains/` directory structure
- Implement 3 initial orchestrators (tax, blockchain, compliance)
- Define standard orchestrator interface

**Files to Create:**
```
domains/
├── __init__.py
├── base_orchestrator.py          # Abstract base class
├── tax/
│   ├── __init__.py
│   └── orchestrator.py           # TaxAnalysisOrchestrator
├── blockchain/
│   ├── __init__.py
│   └── orchestrator.py           # BlockchainAnalysisOrchestrator
└── compliance/
    ├── __init__.py
    └── orchestrator.py           # ComplianceEvaluationOrchestrator
```

**Deliverables:**
- ✅ `domains/base_orchestrator.py` - Abstract orchestrator interface
- ✅ Working orchestrators for 3 domains
- ✅ Unit tests for each orchestrator
- ✅ Documentation of integration patterns

### Phase 2: Migrate Engine Code (Week 2)

**Goals:**
- Move domain-specific engines from `codex/` to `domains/`
- Update import paths throughout codebase
- Maintain backward compatibility with shims

**Files to Move:**

**Tax Domain (13 files):**
```bash
# Move tax engines
codex/tax_engine/*.py → domains/tax/engines/

# Move IRS legal intelligence
codex/irs-legal-intel/ → domains/tax/legal/
```

**Blockchain Domain (15 files):**
```bash
# Move blockchain analyzers
codex/blockchain/*.py → domains/blockchain/analyzers/
```

**Compliance Domain (13 files):**
```bash
# Move compliance gateways
codex/compliance/*.py → domains/compliance/gateways/
```

**Backward Compatibility:**
```python
# codex/tax_engine/__init__.py (compatibility shim)
"""
Compatibility shim for tax engine imports.
Redirects to new domains.tax.engines location.
"""
import warnings
from domains.tax.engines.crypto_tax_analyzer import CryptoTaxAnalyzer
from domains.tax.engines.multi_jurisdictional_tax_engine import MultiJurisdictionalTaxEngine

warnings.warn(
    "Importing from codex.tax_engine is deprecated. "
    "Use domains.tax.engines instead.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ['CryptoTaxAnalyzer', 'MultiJurisdictionalTaxEngine']
```

### Phase 3: Integrate Ethics into Nexus (Week 2)

**Goals:**
- Move ethical reasoning from Codex to Nexus
- Integrate ethics as core Nexus capability
- Update all ethical imports

**Files to Move:**
```bash
codex/ethics/ → nexus/ethics/
codex/codex_core/meta_ethical_framework.py → nexus/ethics/framework/
codex/specialized/temporal_moral_reasoner.py → nexus/ethics/temporal/
```

**Rationale:**
Ethics is fundamentally about **emotional and social intelligence**, not pure analytical reasoning. Nexus is the appropriate home for:
- Stakeholder impact assessment
- Moral reasoning
- Emotional context evaluation
- Social implications

### Phase 4: Enhance Sensus for Data Perception (Week 3)

**Goals:**
- Create data perception modules in Sensus
- Enable Sensus to perceive financial, blockchain, and compliance data
- Integrate with domain orchestrators

**New Files:**
```
sensus/data_perception/
├── __init__.py
├── transaction_perceptor.py      # Financial transaction patterns
├── market_perceptor.py            # Market signal perception
├── blockchain_perceptor.py        # On-chain pattern detection
└── document_perceptor.py          # Regulatory document perception
```

**Key Capabilities:**
- Pattern recognition in transaction sequences
- Anomaly detection in data streams
- Quality assessment of input data
- Feature extraction for downstream lobes

### Phase 5: Update Cortex Coordination (Week 3)

**Goals:**
- Enhance Cortex integration gating for domain orchestration
- Add domain-specific coordination logic
- Implement confidence aggregation across lobes

**Files to Update:**
```
cortex/integration/integration_gating.py    # Enhance for domain orchestration
cortex/integration/domain_coordinator.py     # NEW: Domain-specific coordination
```

**New Capabilities:**
- Domain-aware attention gating
- Cross-lobe output reconciliation
- Confidence aggregation algorithms
- Reasoning trace generation

### Phase 6: Update Entry Points (Week 4)

**Goals:**
- Update main applications to use domain orchestrators
- Create new domain-specific entry points
- Update showcases to demonstrate full-brain integration

**Files to Update:**
```
spiralcortex_dashboard.py               # Add domain orchestrator options
spiralcortex_multisector_app.py         # Integrate domain orchestrators
showcases/spiralcortex_tax_analysis.py  # NEW: Tax domain showcase
showcases/spiralcortex_blockchain.py     # NEW: Blockchain domain showcase
```

### Phase 7: Testing & Validation (Week 4)

**Goals:**
- Create integration tests for full-brain flows
- Validate all domain orchestrators
- Benchmark performance vs standalone Codex

**New Test Files:**
```
tests/integration/
├── test_tax_orchestrator.py
├── test_blockchain_orchestrator.py
├── test_compliance_orchestrator.py
└── test_full_brain_flow.py
```

**Validation Criteria:**
- ✅ All orchestrators pass integration tests
- ✅ Performance within 20% of standalone Codex
- ✅ All lobe outputs properly integrated
- ✅ Backward compatibility maintained with shims
- ✅ Documentation complete

---

## Benefits of Full-Brain Integration

### 1. **Holistic Decision Making**
Instead of purely analytical outputs, get integrated decisions considering:
- Logical correctness (Codex)
- Ethical implications (Nexus)
- Perceptual insights (Sensus)
- Metacognitive confidence (Cortex)

### 2. **Enhanced Explainability**
Full reasoning trace showing how all four lobes contributed:
```json
{
  "decision": "Recommend specific identification method for tax optimization",
  "reasoning_trace": {
    "sensus": "Detected high-volatility trading pattern in Q4 2024",
    "codex": "Specific ID yields $12,400 lower tax vs FIFO",
    "nexus": "Ethical score: 0.85 (legally compliant, stakeholder-fair)",
    "cortex": "Confidence: 0.92 (high agreement across lobes)"
  }
}
```

### 3. **Ethical Guardrails**
Nexus evaluates every decision for ethical implications, preventing:
- Aggressive tax avoidance that crosses into evasion
- DeFi strategies with high societal harm
- Compliance strategies that violate privacy rights

### 4. **Robustness to Uncertainty**
Cortex detects when lobe outputs conflict:
```python
{
  "conflict_detected": True,
  "conflict_details": {
    "codex": "Recommends aggressive wash sale optimization",
    "nexus": "Ethical score: 0.45 (legally dubious, stakeholder harm)",
    "cortex_resolution": "Conservative strategy recommended due to ethical concerns"
  }
}
```

### 5. **Domain Extensibility**
Easy to add new domains as full-brain orchestrators:
```
domains/
├── tax/                    # ✅ Implemented
├── blockchain/             # ✅ Implemented
├── compliance/             # ✅ Implemented
├── forensics/              # 🔜 Future
├── knowledge_graphs/       # 🔜 Future
└── forecasting/            # 🔜 Future
```

---

## Technical Considerations

### Import Path Management

**Current (v2.0 nested):**
```python
from codex.tax_engine.crypto_tax_analyzer import CryptoTaxAnalyzer
from codex.ethics.ethical_reasoning_integration import EthicalReasoningIntegrator
```

**Proposed (full-brain):**
```python
from domains.tax.orchestrator import TaxAnalysisOrchestrator
from nexus.ethics.ethical_reasoning_integration import EthicalReasoningIntegrator
```

**Backward Compatibility (shims):**
```python
# codex/tax_engine/__init__.py
from domains.tax.engines.crypto_tax_analyzer import CryptoTaxAnalyzer
warnings.warn("Use domains.tax.engines instead", DeprecationWarning)
```

### Performance Optimization

**Concern:** Four-lobe orchestration may add latency

**Solutions:**
1. **Parallel Processing:** Run independent lobe computations in parallel
2. **Caching:** Cache lobe outputs for similar inputs
3. **Lazy Evaluation:** Only invoke lobes when needed for decision
4. **Confidence Thresholds:** Skip low-value lobe contributions

**Benchmarking Target:** <20% latency increase vs standalone Codex

### Backward Compatibility Strategy

**Approach:**
1. **Keep existing Codex subdirectories** (Week 1-4)
2. **Create compatibility shims** with deprecation warnings
3. **Update internal imports gradually** (Week 2-4)
4. **Remove shims in v2.1** (3 months after v2.0 migration)

**Deprecation Timeline:**
- **v2.0 (Nov 2025):** Shims active, warnings issued
- **v2.0.5 (Jan 2026):** Shims active, documentation updated
- **v2.1 (Feb 2026):** Shims removed, full-brain only

---

## File Movement Plan

### Directories to Create (9 new)

```
domains/                               # NEW: System-wide domain orchestrators
domains/tax/                           # NEW: Tax analysis orchestration
domains/tax/engines/                   # NEW: Tax calculation engines
domains/tax/legal/                     # NEW: IRS legal intelligence
domains/blockchain/                    # NEW: Blockchain analysis orchestration
domains/blockchain/analyzers/          # NEW: Blockchain analyzers
domains/compliance/                    # NEW: Compliance evaluation orchestration
domains/compliance/gateways/           # NEW: Compliance gateways
sensus/data_perception/                # NEW: Data perception modules
```

### Files to Move (50 files)

**Tax Domain (22 files):**
- `codex/tax_engine/*.py` (13 files) → `domains/tax/engines/`
- `codex/irs-legal-intel/` (9 files) → `domains/tax/legal/`

**Blockchain Domain (15 files):**
- `codex/blockchain/*.py` (15 files) → `domains/blockchain/analyzers/`

**Compliance Domain (13 files):**
- `codex/compliance/*.py` (13 files) → `domains/compliance/gateways/`

**Ethics Domain (9 files):**
- `codex/ethics/*.py` (9 files) → `nexus/ethics/`

**Specialized Domain (varies):**
- `codex/specialized/` → evaluate per-file

**Total Files to Move:** ~50 files  
**Total Files to Keep in Codex:** ~229 files (infrastructure, core, api, services)

### Files to Keep in Codex (229 files)

**Infrastructure (Keep as Codex internals):**
- `codex/root/` (34 files) - Core Codex functionality
- `codex/codex_core/` (28 files) - Analytical models
- `codex/api/` (21 files) - REST API layer
- `codex/core/` (21 files) - Main servers
- `codex/services/` (12 files) - Service implementations
- `codex/integration/` (12 files) - External system adapters
- `codex/pathways/` (9 files) - Cognitive routing
- `codex/learning/` (8 files) - Adaptive learning
- `codex/validation/` (9 files) - Data validation

**Rationale:** These are **Codex-specific infrastructure** supporting its analytical reasoning role, not domain-specific logic that should be orchestrated brain-wide.

---

## Risk Assessment

### HIGH RISK: Import Path Breakage
**Mitigation:**
- Comprehensive import path audit before migration
- Automated script to update all imports
- Compatibility shims for 3-month deprecation period
- Extensive testing of all entry points

### MEDIUM RISK: Performance Degradation
**Mitigation:**
- Benchmark standalone Codex vs full-brain orchestration
- Implement parallel lobe processing where possible
- Add performance monitoring to orchestrators
- Target <20% latency increase

### MEDIUM RISK: Complexity Increase
**Mitigation:**
- Clear documentation of integration patterns
- Standard orchestrator interface (base class)
- Comprehensive examples in showcases
- Training materials for developers

### LOW RISK: Lobe Unavailability
**Mitigation:**
- Graceful degradation when lobe unavailable
- Fallback to Codex-only analysis if needed
- Health checks for all lobes
- Clear error messages

---

## Rollback Strategy

### Emergency Fallback: Codex-Only Mode

If orchestration performance degrades beyond acceptable limits (>25% latency increase), all orchestrators support **Codex-only fallback mode**.

**Activation Methods:**

1. **Command-line flag:**
```bash
python spiralcortex_dashboard.py --codex-only
```

2. **Environment variable:**
```bash
export SPIRALCORTEX_MODE=codex_only
python spiralcortex_dashboard.py
```

3. **Programmatic flag:**
```python
from domains.tax.orchestrator import TaxAnalysisOrchestrator

orchestrator = TaxAnalysisOrchestrator(mode="codex_only")
```

**Behavior in Codex-Only Mode:**
- Orchestrators bypass Sensus, Nexus, Cortex
- Direct invocation of Codex analysis engines
- No ethical evaluation or perception enhancement
- Performance matches standalone Codex (v2.0 pre-migration)
- Logs warning: `"Running in degraded mode: Codex-only analysis"`

**Rollback Timeline:**
- **Immediate (< 1 hour):** Enable `--codex-only` flag system-wide
- **Week 1:** Identify performance bottlenecks via profiling
- **Week 2:** Optimize or revert specific orchestrators
- **Week 3:** Re-enable full-brain mode with fixes

**Rollback Decision Criteria:**
- P0 production incident (system down)
- >25% latency increase persisting >24 hours
- Critical lobe failure affecting >50% of requests
- Stakeholder escalation requiring immediate stability

---

## Partial Brain Operation

### Graceful Degradation Matrix

Orchestrators must handle lobe unavailability gracefully. Behavior depends on which lobe is offline:

| Lobe Offline | Impact | Orchestrator Behavior | Output Quality |
|--------------|--------|----------------------|----------------|
| **Sensus** | Perception lost | Use raw data features, skip pattern detection | 85% - Analytical correctness preserved |
| **Codex** | Analysis lost | **HALT** - Cannot proceed without core reasoning | 0% - Fatal error |
| **Nexus** | Ethics lost | Skip ethical evaluation, log warning | 70% - No ethical guardrails |
| **Cortex** | Coordination lost | Use simple confidence averaging | 75% - Reduced metacognitive awareness |

**Implementation Pattern:**

```python
class TaxAnalysisOrchestrator(BaseDomainOrchestrator):
    def analyze_crypto_transactions(self, transactions, tax_year, jurisdiction="US"):
        """Process with graceful degradation."""
        
        # Step 1: SENSUS (Optional)
        if self.sensus.is_available():
            sensus_output = self.sensus_perceptor.perceive_transactions(...)
        else:
            logger.warning("Sensus unavailable - using raw data features")
            sensus_output = self._extract_basic_features(transactions)
        
        # Step 2: CODEX (Required)
        if not self.codex.is_available():
            raise CriticalLobeUnavailable("Codex is required for tax analysis")
        codex_output = self.codex_analyzer.analyze(...)
        
        # Step 3: NEXUS (Optional)
        if self.nexus.is_available():
            nexus_output = self.nexus_ethics.evaluate(...)
        else:
            logger.warning("Nexus unavailable - skipping ethical evaluation")
            nexus_output = {"ethical_score": None, "note": "Not evaluated"}
        
        # Step 4: CORTEX (Optional)
        if self.cortex.is_available():
            cortex_output = self.cortex_coordinator.integrate(...)
        else:
            logger.warning("Cortex unavailable - using simple averaging")
            cortex_output = self._simple_confidence_aggregation(...)
        
        return {
            "tax_analysis": codex_output,
            "ethical_evaluation": nexus_output,
            "perception_insights": sensus_output,
            "integrated_decision": cortex_output,
            "degraded_mode": not all([
                self.sensus.is_available(),
                self.nexus.is_available(),
                self.cortex.is_available()
            ])
        }
```

**Health Check Mechanism:**

```python
# All lobes implement .is_available() health check
class LobeHealthCheck:
    def is_available(self) -> bool:
        """Check if lobe is responsive."""
        try:
            response = self.ping(timeout=1.0)
            return response.status == "healthy"
        except (TimeoutError, ConnectionError):
            return False
```

**Degraded Mode Alerts:**

System monitors lobe availability and alerts when operating in degraded mode:

```
⚠️  DEGRADED MODE ACTIVE
Lobe Status:
  • Sensus:  ✅ Available
  • Codex:   ✅ Available
  • Nexus:   ❌ Unavailable (timeout)
  • Cortex:  ✅ Available

Impact: Ethical evaluation disabled
Quality: 70% (analytical correctness preserved)
Action: Check nexus/emotional/emotion_engine.py logs
```

---

## Success Metrics

### Functional Metrics
- ✅ All 3 domain orchestrators operational
- ✅ All showcases updated to demonstrate full-brain integration
- ✅ 100% backward compatibility with shims
- ✅ Zero broken imports after migration

### Performance Metrics
- ✅ <20% latency increase vs standalone Codex
- ✅ <5% memory overhead per orchestrator
- ✅ Lobe processing parallelization achieves >60% theoretical speedup

### Quality Metrics
- ✅ 100% test coverage for orchestrators
- ✅ Integration tests pass for all domain flows
- ✅ Documentation complete for all new patterns
- ✅ Code review approval from 2+ team members

### Adoption Metrics (3 months post-migration)
- ✅ 80% of new code uses orchestrators instead of direct Codex calls
- ✅ 50% of existing applications migrated to orchestrators
- ✅ Zero P1/P0 bugs related to migration
- ✅ Positive developer feedback on new architecture

---

## Next Steps

### Immediate Actions (This Week)
1. **Review this proposal** with team/stakeholders
2. **Validate architectural vision** aligns with SpiralCortex goals
3. **Prioritize domains** for initial orchestrator implementation
4. **Assign ownership** for each migration phase

### Week 1 Kickoff Tasks
1. Create `domains/` directory structure
2. Implement `domains/base_orchestrator.py` abstract class
3. Create first orchestrator: `domains/tax/orchestrator.py`
4. Write integration tests for tax orchestrator
5. Update one showcase to use tax orchestrator

### Decision Points
- [ ] **Approve architectural vision** (full-brain vs standalone)
- [ ] **Approve directory structure** (`domains/` location and naming)
- [ ] **Approve migration timeline** (4 weeks vs longer)
- [ ] **Approve backward compatibility strategy** (shims for 3 months)

---

## Appendices

### Appendix A: Example Full-Brain Flow (Tax Analysis)

```python
# Example: Crypto tax analysis through full brain

from domains.tax.orchestrator import TaxAnalysisOrchestrator

# Initialize orchestrator (coordinates all 4 lobes)
orchestrator = TaxAnalysisOrchestrator()

# Analyze crypto transactions
result = orchestrator.analyze_crypto_transactions(
    transactions=[
        {"date": "2024-01-15", "type": "buy", "asset": "BTC", "amount": 0.5, "price": 42000},
        {"date": "2024-06-20", "type": "sell", "asset": "BTC", "amount": 0.5, "price": 58000},
        # ... more transactions
    ],
    tax_year=2024,
    jurisdiction="US"
)

# Full-brain output includes all lobe contributions
print(f"Trace ID: {result['trace_id']}")  # For audit logging
print(f"Tax Analysis: {result['tax_analysis']}")
print(f"Ethical Evaluation: {result['ethical_evaluation']}")
print(f"Perception Insights: {result['perception_insights']}")
print(f"Integrated Decision: {result['integrated_decision']}")
print(f"Confidence: {result['confidence']}")
print(f"Reasoning Trace: {result['reasoning_trace']}")
print(f"Degraded Mode: {result['degraded_mode']}")  # False if all lobes available
```

**Output:**
```json
{
  "trace_id": "TaxAnalysisOrchestrator-7f3a9b2c5e1d",
  "tax_analysis": {
    "total_gain": 8000,
    "total_tax_owed": 1200,
    "methodology": "FIFO",
    "optimization_opportunities": [
      {
        "strategy": "specific_identification",
        "potential_savings": 400,
        "risk_level": "low"
      }
    ]
  },
  "ethical_evaluation": {
    "ethical_score": 0.92,
    "dimensions": {
      "legal_compliance": 0.98,
      "stakeholder_fairness": 0.88,
      "societal_impact": 0.90
    },
    "concerns": [],
    "recommendations": "Proposed optimization is ethical and legally compliant"
  },
  "perception_insights": {
    "pattern_detected": "consistent_monthly_trading",
    "anomalies": [],
    "data_quality": 0.95,
    "complexity": 0.4
  },
  "integrated_decision": {
    "recommendation": "Use specific identification for $400 tax savings",
    "confidence": 0.94,
    "rationale": "High confidence across all lobes, no ethical concerns"
  },
  "reasoning_trace": {
    "sensus": "Detected clean transaction data with consistent patterns",
    "codex": "Calculated $400 savings with specific ID, legally sound",
    "nexus": "Ethical evaluation: 0.92, stakeholder-fair approach",
    "cortex": "High lobe agreement (0.94), proceed with confidence"
  },
  "degraded_mode": false,
  "orchestrator_version": "1.0.0",
  "timestamp": "2025-11-01T14:32:18.472Z"
}
```

**Audit Trail Linkage:**

All lobe outputs are linked via `trace_id` for complete data lineage:

```
Audit Log Entries (linked by trace_id):
┌─────────────────────────────────────────────────────────────┐
│ trace_id: TaxAnalysisOrchestrator-7f3a9b2c5e1d             │
├─────────────────────────────────────────────────────────────┤
│ [14:32:18.102] SENSUS: Perception started                  │
│ [14:32:18.287] SENSUS: 24 transactions analyzed            │
│ [14:32:18.289] CODEX: Tax calculation started              │
│ [14:32:18.401] CODEX: FIFO method applied                  │
│ [14:32:18.402] NEXUS: Ethical evaluation started           │
│ [14:32:18.455] NEXUS: Score 0.92 (compliant)               │
│ [14:32:18.457] CORTEX: Integration started                 │
│ [14:32:18.472] CORTEX: Decision finalized (conf: 0.94)     │
│ [14:32:18.474] ORCHESTRATOR: Result returned               │
└─────────────────────────────────────────────────────────────┘

Query any trace_id to see complete decision provenance.
```

```python
# domains/base_orchestrator.py

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime
import uuid

# Orchestrator interface version
__version__ = "1.0.0"

@dataclass
class LobeOutput:
    """Output from a single lobe."""
    lobe_name: str
    output_data: Dict[str, Any]
    confidence: float
    processing_time_ms: float
    trace_id: str  # Links to parent orchestration
    timestamp: datetime

@dataclass
class OrchestrationResult:
    """Result from full-brain orchestration."""
    trace_id: str  # Unique identifier for this orchestration
    lobe_outputs: Dict[str, LobeOutput]
    integrated_decision: Dict[str, Any]
    confidence: float
    reasoning_trace: Dict[str, str]
    metadata: Dict[str, Any]
    orchestrator_version: str  # Interface version used
    timestamp: datetime

class BaseDomainOrchestrator(ABC):
    """
    Abstract base class for domain orchestrators.
    All domain orchestrators must implement this interface.
    
    Version: 1.0.0
    - Initial release with trace_id support
    - Health checks for all lobes
    - Graceful degradation patterns
    """
    
    # Interface version implemented by this orchestrator
    INTERFACE_VERSION = "1.0.0"
    
    def __init__(self):
        """Initialize all four lobes."""
        self.sensus = self._initialize_sensus()
        self.codex = self._initialize_codex()
        self.nexus = self._initialize_nexus()
        self.cortex = self._initialize_cortex()
    
    @abstractmethod
    def _initialize_sensus(self):
        """Initialize Sensus lobe for this domain."""
        pass
    
    @abstractmethod
    def _initialize_codex(self):
        """Initialize Codex lobe for this domain."""
        pass
    
    @abstractmethod
    def _initialize_nexus(self):
        """Initialize Nexus lobe for this domain."""
        pass
    
    @abstractmethod
    def _initialize_cortex(self):
        """Initialize Cortex lobe for this domain."""
        pass
    
    def _generate_trace_id(self) -> str:
        """Generate unique trace ID for this orchestration."""
        return f"{self.__class__.__name__}-{uuid.uuid4().hex[:12]}"
    
    @abstractmethod
    def process(self, input_data: Any, context: Dict[str, Any]) -> OrchestrationResult:
        """
        Process input through all four lobes.
        
        Must follow standard flow:
        1. Generate trace_id for data lineage
        2. Sensus perceives input
        3. Codex analyzes
        4. Nexus evaluates ethics
        5. Cortex coordinates decision
        
        Returns:
            OrchestrationResult with all lobe outputs and integrated decision
            
        Raises:
            CriticalLobeUnavailable: If Codex (required lobe) is unavailable
        """
        pass
    
    def _create_reasoning_trace(
        self, 
        lobe_outputs: Dict[str, LobeOutput]
    ) -> Dict[str, str]:
        """Generate human-readable reasoning trace from lobe outputs."""
        return {
            lobe_name: self._summarize_lobe_output(output)
            for lobe_name, output in lobe_outputs.items()
        }
    
    @abstractmethod
    def _summarize_lobe_output(self, output: LobeOutput) -> str:
        """Create human-readable summary of lobe output."""
        pass
    
    def _emit_audit_event(
        self, 
        trace_id: str, 
        event_type: str, 
        payload: Dict[str, Any]
    ):
        """
        Emit audit event for compliance logging.
        
        Links all lobe outputs via trace_id for complete data lineage.
        """
        audit_event = {
            "trace_id": trace_id,
            "orchestrator": self.__class__.__name__,
            "interface_version": self.INTERFACE_VERSION,
            "event_type": event_type,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }
        # Send to audit logging system
        # (Implementation depends on audit infrastructure)
        pass

class CriticalLobeUnavailable(Exception):
    """Raised when a required lobe is unavailable."""
    pass
```

### Interface Versioning Strategy

**Semantic Versioning:**
- **MAJOR.MINOR.PATCH** (e.g., `1.0.0`)
- **MAJOR:** Breaking changes to orchestrator interface
- **MINOR:** New optional methods/features (backward compatible)
- **PATCH:** Bug fixes, documentation updates

**Version Compatibility Rules:**

```python
# Orchestrators declare minimum interface version required
class TaxAnalysisOrchestrator(BaseDomainOrchestrator):
    MIN_INTERFACE_VERSION = "1.0.0"
    
    def __init__(self):
        # Check interface compatibility at initialization
        if not self._is_compatible(BaseDomainOrchestrator.INTERFACE_VERSION):
            raise IncompatibleInterfaceError(
                f"Requires interface v{self.MIN_INTERFACE_VERSION}, "
                f"but v{BaseDomainOrchestrator.INTERFACE_VERSION} found"
            )
        super().__init__()
    
    def _is_compatible(self, current_version: str) -> bool:
        """Check if current interface version is compatible."""
        return self._version_gte(current_version, self.MIN_INTERFACE_VERSION)
```

**Version Evolution Example:**

```
v1.0.0 (Nov 2025) - Initial release
  • trace_id support
  • Basic health checks
  • Four-lobe orchestration

v1.1.0 (Jan 2026) - Added features
  • Optional async processing
  • Caching layer for lobe outputs
  • Performance profiling hooks
  • Backward compatible with v1.0.0

v2.0.0 (Apr 2026) - Breaking changes
  • New required method: validate_input()
  • LobeOutput schema change (added 'provenance' field)
  • Orchestrators must explicitly upgrade
```

---

### Appendix B: Orchestrator Interface Specification (Updated)

```python

---

**End of Proposal**

**Prepared by:** GitHub Copilot  
**Review Requested from:** SpiralBrain-v2.0 Development Team  
**Decision Deadline:** November 8, 2025

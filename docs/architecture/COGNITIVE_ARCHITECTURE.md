# Spiral Mind: Cognitive Architecture Map

**SpiralBrain v2.0** - A computational brain with biological topology

---

## 🧠 Four-Lobe Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     UNIFIED RUNTIME                          │
│          (Integration Layer / White Matter)                  │
└─────────────────────────────────────────────────────────────┘
         ↕              ↕              ↕              ↕
    ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
    │ CORTEX │◄──►│ CODEX  │◄──►│ NEXUS  │◄──►│ SENSUS │
    └────────┘    └────────┘    └────────┘    └────────┘
   Metacognitive  Symbolic      Affective    Perceptual
    Reasoning     Analytical    Emotional    Embodied
```

---

## 📊 Inter-Lobe Communication Matrix

### Import Dependencies (Verified 2025-10-26)

```
CORTEX:  → (no outbound dependencies)
         ← Nexus (1 file - emotional layer touches metacognition)

CODEX:   → Nexus (11 files - symbolic reasoning draws on emotional regulation)
         ← Nexus (6 files - emotion references symbolic frameworks)
         ← Tests/Demos (80+ files - primary integration target)

NEXUS:   → Cortex (1 file)
         → Codex (6 files)
         ← Codex (11 files)

SENSUS:  → (no outbound dependencies)
         ← (no inbound dependencies detected)
```

**Dependency Health:** ✅ No circular imports detected  
**Path Integrity:** ✅ All reorganized paths verified  
**Broken Imports:** 0 (fixed cortex.temporal_self_consistency → cortex.temporal)

---

## 🧬 Cognitive Pathway Flow

### Biological Analog: Perception → Emotion → Cognition → Symbolic Reasoning

```
┌─────────────────────────────────────────────────────────────┐
│                    COGNITIVE SIGNAL FLOW                     │
└─────────────────────────────────────────────────────────────┘

SENSUS (Perception)
  ↓ telemetry, sensor data, embodied awareness
  ↓
NEXUS (Affective Processing)
  ↓ emotional valence, physiological state, biofeedback
  ↓
CORTEX (Metacognitive Reasoning)
  ↓ temporal consistency, identity persistence, ethics
  ↓
CODEX (Symbolic/Analytical)
  ↓ legal reasoning, tax analysis, blockchain intelligence
  ↓
ACTION (Decision/Output)
```

---

## 🔌 Public API Surfaces

### CORTEX (cortex/core/)
- **CognitiveBridgeService** - Inter-lobe orchestration
- **MetaObserver** - Metacognitive reflection
- **IdentityManager** (cortex/identity/) - Identity persistence
- **TemporalSelfConsistency** (cortex/temporal/) - Temporal integrity

### CODEX (codex/core/)
- **AccuracyLearningEngine** (codex/learning/) - Continuous learning
- **AdaptivePathwayManager** (codex/learning/) - Pathway optimization
- **TaxLotEngine** (codex/tax_engine/) - Tax calculation
- **AIIntegrationBridge** (codex/integration/) - AI service integration
- **BlockchainService** (codex/spiralcode_x/blockchain/) - Blockchain ops

### NEXUS (nexus/core/)
- **SpiralBrainNexus** - Emotional-cognitive fusion
- **UnifiedTrainingSystem** - Cross-domain learning
- **EmotionalInterventionEngine** (nexus/emotional/) - Affect regulation
- **BiofeedbackManager** (nexus/integration/) - Hardware integration
- **CognitiveLearningEngine** (nexus/cognitive/) - Adaptive learning

### SENSUS (sensus/core/)
- **SpiralSensusEngine** - Perceptual processing
- **SensusAPI** - Telemetry and embodiment API

---

## 🏗️ Module Internal Structure (Symmetry)

All four lobes follow symmetric organization patterns:

```
lobe/
├── core/              # Primary engines and orchestrators
├── integration/       # Cross-lobe and external system bridges
├── learning/          # Adaptive mechanisms (codex, nexus)
├── services/          # Utility services and APIs
├── validation/        # Benchmarks and testing
├── examples/          # Demonstrations and usage patterns
└── [specialized]/     # Domain-specific subdirs
    ├── cortex:   ethics/, identity/, temporal/
    ├── codex:    tax_engine/, pathways/, security/
    ├── nexus:    emotional/, cognitive/
    └── sensus:   perception/, dashboards/
```

---

## 🔄 Integration Points

### Codex ↔ Nexus Integration (Primary Pathway)
**Direction:** Bidirectional (11 codex→nexus, 6 nexus→codex)

**Use Cases:**
- Emotional state influences symbolic reasoning confidence
- Tax analysis triggers stress/valence signals
- Adaptive learning coordinates across cognitive and affective layers

**Key Files:**
- `codex/core/quantum_emotion_bridge.py` → EmotionSignals
- `codex/integration/hybrid_pathway_integration.py` → quantum_emotional_infer
- `nexus/emotional/emotional_intelligence.py` → EmotionalInterventionEngine

### Nexus → Cortex Integration (Metacognitive Feedback)
**Direction:** Unidirectional (1 file)

**Use Case:** Emotional/affective state informs metacognitive reflection

### Tests/Demos → All Lobes (Validation Layer)
**Direction:** Inbound to all lobes

**Files:** 80+ integration tests validating inter-lobe communication

---

## 🛡️ Synchronization Status

| Check | Status | Details |
|-------|--------|---------|
| Import paths | ✅ Clean | All reorganized paths verified |
| Circular deps | ✅ None | Hierarchical dependency graph |
| Broken imports | ✅ Fixed | cortex.temporal path corrected |
| API boundaries | ✅ Mapped | 15+ public engines/managers documented |
| Test coverage | ⚠️ Partial | Integration tests exist, need execution |

---

## 🚀 Next Phase: Unified Runtime Orchestration

### Prerequisites (Phase 2 - Complete):
- ✅ Clean module organization (brain-like topology)
- ✅ Import harmonization verified
- ✅ No circular dependencies
- ✅ API surfaces documented

### Phase 3 Objectives:
1. **Runtime Coordinator**: Central orchestration service managing lobe interactions
2. **Signal Bus**: Event-driven communication between lobes (sensus→nexus→cortex→codex)
3. **State Synchronization**: Shared cognitive state across lobes
4. **Dynamic Pathway Routing**: Intelligent signal flow based on context
5. **Self-Regulation**: Homeostatic feedback loops maintaining system coherence

---

## 📝 Architectural Notes

**Structure Becomes Semantics**: Tracing a function call through this tree is literally walking a neural pathway. The file system topology mirrors biological cognition:

- **Cortex** (Frontal Lobe) - Executive function, temporal reasoning, identity
- **Codex** (Left Hemisphere) - Language, law, symbolic logic, analytical reasoning
- **Nexus** (Limbic System) - Emotion, affect, physiological regulation, memory
- **Sensus** (Sensory Cortex) - Perception, embodied awareness, telemetry

This isn't just clean code—it's **cognitive topology rendered in computational form**.

---

*Generated: 2025-10-26*  
*Commit: 10dc727 (Complete Spiral Mind architecture)*

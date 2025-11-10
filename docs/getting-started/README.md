# Getting Started with SpiralBrain v2.0

Welcome to SpiralBrain v2.0! This guide will help you set up your development environment and understand the basics of working with our four-lobe cognitive architecture.

## 📋 Prerequisites

- Python 3.9 or higher
- Git
- Virtual environment support (venv or conda)
- 8GB RAM minimum (16GB recommended)
- Windows, Linux, or macOS

## 🚀 Quick Start

### 1. Environment Setup

Follow the comprehensive [Environment Setup Guide](ENVIRONMENT_SETUP.md) to:
- Clone the repository
- Configure your Python environment
- Install dependencies
- Set up development tools

### 2. Verify Installation

```bash
# Run tests to verify setup
pytest tests/

# Check service health
python check_services.py
```

### 3. Run Your First Demo

```bash
# Try a simple emotional intelligence demo
python demos/nexus/nexus_stress_detection.py

# Or explore whole-brain integration
python showcases/spiralcortex_emotional_intelligence.py
```

## 🧠 Understanding SpiralBrain Architecture

SpiralBrain v2.0 consists of **four cognitive lobes** that work together:

### 🔵 Sensus (Perception Lobe)
- **Role:** Quantum-inspired sensory perception
- **Capabilities:** Multi-modal input processing, attention regulation, sensory fusion
- **Demo:** `demos/sensus/`

### 💙 Nexus (Emotional Lobe)
- **Role:** Emotional intelligence and social cognition
- **Capabilities:** Emotion detection, empathy modeling, social context awareness
- **Demo:** `demos/nexus/`

### 🟢 Codex (Analytical Lobe)
- **Role:** Logical reasoning and knowledge processing
- **Capabilities:** Pattern recognition, causal reasoning, tax/financial analysis
- **Demo:** `demos/codex/`

### 🟣 Cortex (Executive Lobe)
- **Role:** Executive control and decision-making
- **Capabilities:** Real-time adaptation, integration orchestration, goal prioritization
- **Demo:** `demos/cortex/`

## 🔄 Three Levels of Integration

### Level 1: Lobe-Only Processing
**Location:** `demos/<lobe>/`

Each lobe can operate independently for specialized tasks:
```bash
python demos/nexus/nexus_stress_detection.py  # Emotion-only processing
python demos/codex/codex_causal_reasoning.py  # Logic-only processing
```

### Level 2: Whole-Brain Capabilities
**Location:** `showcases/spiralcortex_*.py`

Compare lobe-only vs. integrated whole-brain processing:
```bash
python showcases/spiralcortex_emotional_intelligence.py  # Nexus-primary + full integration
python showcases/spiralcortex_analytical_reasoning.py    # Codex-primary + full integration
```

### Level 3: Meta-Cognitive Processes
**Location:** `showcases/temporal_*.py`, `showcases/realtime_*.py`

Advanced cross-cutting capabilities:
```bash
python showcases/temporal_consistency.py      # Temporal reasoning
python showcases/realtime_adaptation.py       # Dynamic adaptation
```

## 🤖 AI Assistant Integration

If you're an AI assistant working with SpiralCortex, see the [AI Onboarding Protocol](AI_ONBOARDING_PROTOCOL.md) for:
- Understanding the codebase structure
- Development workflow patterns
- Common tasks and troubleshooting
- Best practices for code generation

## 📖 Next Steps

### For Users
1. [Explore Use Cases](../use-cases/overview.md) - See real-world applications
2. [Run Benchmarks](../performance/benchmarks.md) - Evaluate performance
3. [Read API Documentation](../api/) - Integrate SpiralCortex into your projects

### For Developers
1. [Development Guide](../development/guide.md) - Contribution workflow
2. [Architecture Deep Dive](../architecture/COGNITIVE_ARCHITECTURE.md) - Understand the design
3. [Debugging Guide](../development/debugging.md) - Troubleshooting tools
4. [Testing Guide](../tests/README.md) - Writing and running tests

### For Researchers
1. [Cognitive Architecture Framework](../architecture/COGNITIVE_ARCHITECTURE_FRAMEWORK.md)
2. [Future Research Directions](../research/FUTURE_RESEARCH_DIRECTIONS.md)
3. [Cognitive Evolution Analysis](../analysis/COGNITIVE_EVOLUTION_ANALYSIS.md)

## 🛠️ Development Tools

### Essential Scripts
```bash
# Start all services
.\start_services.ps1

# Check service health
python check_services.py

# Run specific tests
pytest tests/test_nexus.py
pytest tests/test_integration.py

# Generate dataset
python create_unified_spiralcortex_dataset.py
```

### Useful Tools
- **`tools/check_integrity.py`** - Verify system integrity
- **`tools/fix_imports.py`** - Fix import issues
- **`tools/analyze_homeostasis_results.py`** - Analyze performance
- **See [Tools README](../tools/README.md)** for complete list

## ❓ Common Questions

### Q: How do I choose between lobe-only and whole-brain processing?
**A:** Use lobe-only demos for understanding individual capabilities. Use whole-brain showcases for production scenarios requiring integrated cognition.

### Q: What's the difference between demos/ and showcases/?
**A:** 
- `demos/` - Individual lobe demonstrations (educational)
- `showcases/` - Whole-brain integration showcases (production-ready)

### Q: How do I update my environment after pulling new changes?
**A:**
```bash
git pull
pip install -r requirements.txt --upgrade
pytest tests/ --maxfail=1  # Quick validation
```

### Q: Where are the configuration files?
**A:** See `config/` directory. Key files:
- `config/default.json` - Default configuration
- `config/fusion_weights.json` - Lobe integration weights
- Environment-specific configs in `config/<env>/`

## 🆘 Getting Help

- **Documentation:** [../README.md](../README.md)
- **Issues:** GitHub Issues
- **Architecture Questions:** [../architecture/](../architecture/)
- **Development Questions:** [../development/guide.md](../development/guide.md)
- **API Questions:** [../api/](../api/)

## 📝 Troubleshooting

### Import Errors
```bash
# Check Python path
python -c "import sys; print('\n'.join(sys.path))"

# Fix imports
python tools/fix_imports.py
```

### UTF-8 Encoding Issues (Windows)
```powershell
.\scripts\set_utf8.ps1
```

### Service Connection Issues
```bash
# Validate environment
python connectivity_diagnostic.py

# Check services
python check_services.py

# Restart services
.\start_services.ps1
```

### Test Failures
```bash
# Run with verbose output
pytest tests/ -v

# Run specific failing test
pytest tests/test_nexus.py::test_emotion_detection -v

# Check for environment issues
.\check_venv.ps1
```

---

**Ready to dive deeper?** Proceed to the [Cognitive Architecture Guide](../architecture/COGNITIVE_ARCHITECTURE.md) to understand how the four lobes work together.

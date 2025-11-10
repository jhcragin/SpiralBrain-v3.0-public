# Migration Documentation

This directory contains documentation for migrating from SpiralCortex v1.x to v2.0.

## 📋 Overview

SpiralCortex v2.0 represents a complete architectural redesign introducing the four-lobe cognitive system. This documentation helps users understand the migration path and transition their v1.x implementations.

## 📚 Migration Documents

### [V1 Architecture Analysis](V1_ARCHITECTURE_ANALYSIS.md)
**Understanding v1.x design**

Comprehensive analysis of the v1.x architecture:
- Original design patterns
- Component organization
- Performance characteristics
- Limitations addressed in v2.0

### [V1 to V2 Architecture Evolution](V1_TO_V2_ARCHITECTURE_EVOLUTION.md)
**The path from v1.x to v2.0**

Detailed evolution documentation:
- Key architectural changes
- Four-lobe system introduction
- Breaking changes
- Migration rationale

### [V1 Documentation Migration Summary](V1_DOCUMENTATION_MIGRATION_SUMMARY.md)
**Documentation changes**

How documentation evolved during migration:
- Documentation restructuring
- Deprecated v1.x docs
- New v2.0 documentation
- Cross-reference updates

### [Total Import Migration Report](TOTAL_IMPORT_MIGRATION_REPORT.md)
**Import structure overhaul**

Complete report on import reorganization:
- v1.x import patterns
- v2.0 import structure
- Breaking import changes
- Migration scripts used

### [V1 Migration Details](v1_migration/)
**Detailed migration resources**

Additional migration materials:
- Benchmark comparisons
- External integration updates
- Federated benchmarking changes
- Specific component migrations

## 🚀 Quick Migration Guide

### Step 1: Assess Your v1.x Implementation

1. Review [V1 Architecture Analysis](V1_ARCHITECTURE_ANALYSIS.md)
2. Identify components you're using
3. Check [V1 to V2 Architecture Evolution](V1_TO_V2_ARCHITECTURE_EVOLUTION.md) for changes
4. Estimate migration effort

### Step 2: Plan Migration

**Small Projects (< 1000 LOC):**
- Consider full rewrite using v2.0 patterns
- Reference [Getting Started Guide](../getting-started/)
- Use v2.0 showcases as templates

**Large Projects (> 1000 LOC):**
- Phase migration by component
- Use migration scripts in `tools/`
- Maintain v1.x compatibility layer temporarily

### Step 3: Execute Migration

```bash
# Backup v1.x project
cp -r project_v1 project_v1_backup

# Run migration tool
python tools/migrate_v1_to_v2.py \
    --source project_v1 \
    --target project_v2

# Review migration report
cat tools/migration_report_*.txt

# Reorganize structure
python tools/reorganize_v1_migration.py

# Verify integrity
python tools/verify_integrity.py
```

### Step 4: Update Code

**Key Changes:**

1. **Import Paths** - See [Total Import Migration Report](TOTAL_IMPORT_MIGRATION_REPORT.md)
   ```python
   # v1.x
   from spiralcortex.engine import EmotionalEngine
   
   # v2.0
   from nexus.nexus_engine import NexusEngine
   ```

2. **API Patterns** - v2.0 uses lobe-specific APIs
   ```python
   # v1.x
   engine = EmotionalEngine()
   result = engine.process(data)
   
   # v2.0 - Lobe-only
   nexus = NexusEngine()
   result = nexus.process_emotional_state(data)
   
   # v2.0 - Whole-brain
   from integration.brain_integration import process_whole_brain
   result = process_whole_brain(data, primary_lobe='nexus')
   ```

3. **Configuration** - New config structure
   ```python
   # v1.x
   config = load_config('config.json')
   
   # v2.0
   from config.config_loader import load_config
   config = load_config('default')  # Loads config/default.json
   ```

### Step 5: Test & Validate

```bash
# Run migration validation tests
pytest tests/test_migration_compatibility.py

# Verify performance
python benchmarks/benchmark_sensus.py
python benchmarks/benchmark_nexus.py
python benchmarks/benchmark_codex.py
python benchmarks/benchmark_cortex.py

# Compare with v1.x baseline
python tools/compare_architecture.py \
    --config1 v1_config.json \
    --config2 v2_config.json
```

## 🔄 Breaking Changes

### Architecture Changes
- **Four-lobe system** replaces monolithic engine
- **Distributed processing** replaces centralized control
- **Dynamic integration** replaces fixed pipelines

### API Changes
- Engine classes renamed and reorganized
- Processing methods use lobe-specific signatures
- Configuration format updated
- Event system redesigned

### Performance Changes
- Initialization may be slower (four lobes to load)
- Processing typically faster (parallel lobe execution)
- Memory usage higher (multiple engines)
- Scalability improved (distributed architecture)

## 🆕 New Capabilities in v2.0

### Four-Lobe Architecture
- **Sensus** - Quantum-inspired perception (NEW)
- **Nexus** - Enhanced emotional intelligence
- **Codex** - Advanced analytical reasoning
- **Cortex** - Executive control and integration (NEW)

### Integration Features
- **Phase locking** - Cognitive synchronization
- **Dynamic routing** - Context-aware processing
- **Adaptive weighting** - Optimized lobe contribution
- **Emergent capabilities** - Whole-brain processing

### Developer Experience
- **Clear modularity** - Lobe-specific codebases
- **Better testing** - Independent lobe validation
- **Improved debugging** - Lobe-level observability
- **Enhanced documentation** - Comprehensive guides

## 📊 Migration Success Criteria

✅ **Migration Complete When:**
- [ ] All imports updated and working
- [ ] Tests passing at >90% of v1.x coverage
- [ ] Performance meets or exceeds v1.x baseline
- [ ] Documentation updated
- [ ] Team trained on v2.0 patterns

## 🆘 Migration Support

### Common Issues

**Import Errors:**
- Use `python tools/fix_imports.py` to auto-fix
- Reference [Total Import Migration Report](TOTAL_IMPORT_MIGRATION_REPORT.md)

**Performance Regression:**
- Check fusion weight configuration
- Review [Performance Guide](../performance/benchmarks.md)
- Use `python tools/optimize_fusion_weights.py`

**API Incompatibility:**
- Check [V1 to V2 Architecture Evolution](V1_TO_V2_ARCHITECTURE_EVOLUTION.md)
- Review [API Documentation](../api/)
- Consider compatibility layer (see `integration/v1_compatibility.py`)

### Resources
- **[Development Guide](../development/guide.md)** - v2.0 development patterns
- **[Architecture Docs](../architecture/)** - Understanding v2.0 design
- **[Getting Started](../getting-started/)** - v2.0 fundamentals
- **[Tools README](../../tools/README.md)** - Migration tools

## 📈 Migration Timeline Estimates

**Small Project (< 1000 LOC):**
- Planning: 1-2 days
- Execution: 2-5 days
- Testing: 1-3 days
- **Total: 1-2 weeks**

**Medium Project (1000-10000 LOC):**
- Planning: 1 week
- Execution: 2-4 weeks
- Testing: 1-2 weeks
- **Total: 4-7 weeks**

**Large Project (> 10000 LOC):**
- Planning: 2-3 weeks
- Execution: 6-12 weeks
- Testing: 2-4 weeks
- **Total: 10-19 weeks**

## 🔗 Related Documentation

- **[Historical Phases](../history/)** - Development journey
- **[Analysis Reports](../analysis/)** - System comparisons
- **[Architecture](../architecture/)** - v2.0 design details
- **[Getting Started](../getting-started/)** - v2.0 fundamentals

---

**Ready to migrate?** Start with [V1 Architecture Analysis](V1_ARCHITECTURE_ANALYSIS.md) to understand your starting point.

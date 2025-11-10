# Import Pattern Guidelines for SpiralBrain v2.0

This document outlines the correct patterns for handling optional imports and dependencies in the SpiralCortex codebase.

## Core Principle: Fail Fast, No Fake Code

**NEVER** provide fake/placeholder implementations that appear to work but don't. If a dependency is missing, either:

1. Fail fast with a clear error message
2. Provide a real alternative implementation (graceful degradation)
3. Use mocks only for testing/development (clearly marked)

## Pattern 1: Required Dependencies (Fail Fast)

For core functionality that must be available:

```python
try:
    from .core.spiralbrain_nexus import Nexus, CognitiveDomain, UnifiedCognitiveState
except ImportError as e:
    raise ImportError(
        f"CRITICAL: Could not import nexus core components from .core.spiralbrain_nexus. "
        f"This indicates a missing or broken core module. Error: {e}. "
        f"Please check that nexus/core/spiralbrain_nexus.py exists and is properly implemented."
    ) from e
```

**When to use**: Core modules, essential functionality, APIs that must work.

## Pattern 2: Graceful Degradation (Real Alternatives)

For optional features with real fallback implementations:

```python
try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False

def analyze_text(text):
    if TRANSFORMERS_AVAILABLE:
        # Use real ML model
        return pipeline("sentiment-analysis")(text)
    else:
        # Use rule-based alternative (real functionality)
        return rule_based_sentiment_analysis(text)
```

**When to use**: ML models with rule-based fallbacks, GUI with headless mode, persistence with memory-only storage.

## Pattern 3: Type Stubs (Fail on Use)

For optional dependencies that provide type hints but fail if actually used:

```python
try:
    from mujoco import MjModel, MjData
    MUJOCO_AVAILABLE = True
except ImportError:
    MUJOCO_AVAILABLE = False

    class MjModel:
        @classmethod
        def from_xml_path(cls, *_args, **_kwargs):
            raise ImportError("MuJoCo not available. Install with: pip install mujoco")

    class MjData:
        def __init__(self, *_args, **_kwargs):
            raise ImportError("MuJoCo not available. Install with: pip install mujoco")
```

**When to use**: Optional libraries with complex APIs, hardware SDKs.

## Pattern 4: Testing Mocks (Clearly Marked)

For test files only:

```python
try:
    import real_module
except ImportError as e:
    print(f"WARNING: Real module not available ({e}), using mock for testing")
    class MockModule:
        # Mock implementation for testing
        pass
    real_module = MockModule()
```

**When to use**: Test files, development environments, CI/CD pipelines.

## Pattern 5: Set to None (Check Before Use)

For simple optional utilities:

```python
try:
    import PIL.Image
except ImportError:
    PIL = None

def process_image(path):
    if PIL is None:
        raise ValueError("PIL required for image processing. Install with: pip install Pillow")
    return PIL.Image.open(path)
```

**When to use**: Simple utility libraries, non-core functionality.

## Anti-Patterns (DO NOT USE)

### ❌ Silent Failure with Fake Implementation
```python
# WRONG - gives false sense of working
try:
    import real_stuff
except ImportError:
    class FakeStuff:
        def do_something(self): return "fake result"
    real_stuff = FakeStuff()
```

### ❌ Silent Warning Only
```python
# WRONG - hides real problems
try:
    import critical_module
except ImportError as e:
    print(f"Warning: {e}")  # Just prints, continues with broken code
    critical_module = None
```

### ❌ Empty Except Blocks
```python
# WRONG - swallows all errors
try:
    import something
except:
    pass  # Silent failure
```

## Implementation Checklist

When adding new imports:

1. **Is this core functionality?** → Use Pattern 1 (Fail Fast)
2. **Is there a real alternative?** → Use Pattern 2 (Graceful Degradation)
3. **Is this for type hints only?** → Use Pattern 3 (Type Stubs)
4. **Is this for testing?** → Use Pattern 4 (Testing Mocks)
5. **Is this a simple utility?** → Use Pattern 5 (Set to None)

## Examples from Codebase

### ✅ Good: Fail Fast (nexus/__init__.py)
```python
try:
    from .core.spiralbrain_nexus import Nexus
except ImportError as e:
    raise ImportError(f"CRITICAL: Could not import nexus core...") from e
```

### ✅ Good: Graceful Degradation (transformers fallback)
```python
if TRANSFORMERS_AVAILABLE:
    return ml_model.predict(text)
else:
    return rule_based_analyzer(text)  # Real alternative
```

### ✅ Good: Type Stubs (mujoco_virtual_adapter.py)
```python
try:
    import mujoco
except ImportError:
    class MjModel:
        @classmethod
        def from_xml_path(cls, *_args, **_kwargs):
            raise ImportError("MuJoCo not available...")
```

### ❌ Bad: Fake Implementation (old nexus_engine.py)
```python
# OLD - provided fake classes that appeared to work
class SpiralCodeX(_DummyBase):
    def update(self, *args, **kwargs):
        return None  # Fake result!
```

## Migration Guide

To fix existing problematic imports:

1. **Identify the pattern**: Is it providing fake functionality?
2. **Determine intent**: Should it fail fast, degrade gracefully, or use type stubs?
3. **Replace with correct pattern**: Follow the guidelines above
4. **Update error messages**: Make them specific and actionable
5. **Test both paths**: Ensure code works with and without the dependency
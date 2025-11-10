# SpiralBrain v2.0 - Environment Setup Guide

**Created:** October 26, 2025  
**Purpose:** Reproducible Python environment for local development and cloud deployment

---

## Overview

SpiralBrain v2.0 uses a Python virtual environment (venv) to ensure consistent dependencies across development, testing, and deployment environments. The system is optimized for CPU execution, with optional GPU support when available.

---

## System Requirements

- **Python:** 3.12.x
- **OS:** Windows 10/11, Linux, macOS
- **RAM:** 8GB minimum, 16GB recommended
- **Storage:** 2GB for dependencies
- **GPU:** Optional (CUDA-capable GPU for acceleration)

---

## Quick Start

### 1. Create Virtual Environment

```powershell
# Windows PowerShell
cd C:\path\to\SpiralBrain-v2.0
python -m venv .venv
```

```bash
# Linux/macOS
cd /path/to/SpiralBrain-v2.0
python3 -m venv .venv
```

### 2. Activate Virtual Environment

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Or use the python executable directly:
& .\.venv\Scripts\python.exe
```

```bash
# Linux/macOS
source .venv/bin/activate
```

### 3. Upgrade pip and Build Tools

```powershell
python -m pip install --upgrade pip setuptools wheel
```

### 4. Install PyTorch (CPU-only)

**For CPU execution (default):**

```powershell
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

**For GPU execution (optional, requires CUDA):**

```powershell
# CUDA 11.8
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 5. Install Core Dependencies

```powershell
python -m pip install numpy pandas flask flask-cors scikit-learn requests cryptography
```

### 6. Verify Installation

```powershell
python -c "import torch; import pandas; import flask; import requests; print('✅ All dependencies loaded!'); print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"
```

**Expected output (CPU):**
```
✅ All dependencies loaded!
PyTorch: 2.9.0+cpu
CUDA available: False
```

---

## Installed Dependencies

### Core ML/AI

| Package | Version | Purpose |
|---------|---------|---------|
| `torch` | 2.9.0+cpu | Deep learning framework (CPU-optimized) |
| `torchvision` | 0.24.0+cpu | Computer vision utilities |
| `torchaudio` | 2.9.0+cpu | Audio processing |
| `numpy` | 2.3.3+ | Numerical computing |
| `pandas` | 2.3.3+ | Data manipulation |
| `scikit-learn` | 1.7.2+ | Machine learning algorithms |

### Web Services

| Package | Version | Purpose |
|---------|---------|---------|
| `flask` | 3.1.2+ | Web framework |
| `flask-cors` | 6.0.1+ | CORS support |
| `requests` | 2.32.5+ | HTTP client |

### Security & Utilities

| Package | Version | Purpose |
|---------|---------|---------|
| `cryptography` | 46.0.3+ | Cryptographic functions |

### Supporting Libraries

- `scipy` (1.16.2+) - Scientific computing
- `jinja2` (3.1.6+) - Templating engine
- `werkzeug` (3.1.3+) - WSGI utilities
- `certifi`, `urllib3`, `idna` - HTTP utilities

---

## Environment Variables

### Required for Benchmarks

```powershell
# Windows PowerShell
$env:PYTHONPATH = "C:\path\to\SpiralCortex-v2.0"
$env:PYTHONIOENCODING = "utf-8"
```

```bash
# Linux/macOS
export PYTHONPATH="/path/to/SpiralCortex-v2.0"
export PYTHONIOENCODING="utf-8"
```

### Optional: GPU Configuration

```powershell
# Force CPU execution (even if GPU available)
$env:CUDA_VISIBLE_DEVICES = "-1"

# Use specific GPU
$env:CUDA_VISIBLE_DEVICES = "0"
```

---

## Running Benchmarks

### With venv activated:

```powershell
python benchmarks/run_all_benchmarks.py
```

### Without activating venv:

```powershell
# Windows
& .\.venv\Scripts\python.exe benchmarks/run_all_benchmarks.py

# Linux/macOS
./.venv/bin/python benchmarks/run_all_benchmarks.py
```

### Run specific lobe benchmark:

```powershell
python benchmarks/benchmark_codex.py
python benchmarks/benchmark_nexus.py
python benchmarks/benchmark_sensus.py
python benchmarks/benchmark_cortex.py
```

---

## Cloud Deployment

### Docker Configuration

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

# Install CPU-only PyTorch
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install other dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app
ENV PYTHONIOENCODING=utf-8

CMD ["python", "benchmarks/run_all_benchmarks.py"]
```

### Azure/AWS Lambda

Use a `requirements.txt` with explicit CPU torch:

```text
--index-url https://download.pytorch.org/whl/cpu
torch==2.9.0+cpu
torchvision==0.24.0+cpu
torchaudio==2.9.0+cpu
numpy>=2.3.3
pandas>=2.3.3
flask>=3.1.2
flask-cors>=6.0.1
scikit-learn>=1.7.2
requests>=2.32.5
cryptography>=46.0.3
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'codex'`

**Solution:** Set PYTHONPATH:
```powershell
$env:PYTHONPATH = "C:\Users\youruser\source\repos\SpiralCortex-v2.0"
```

### Issue: `UnicodeDecodeError` with emoji output

**Solution:** Set UTF-8 encoding:
```powershell
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

### Issue: `[WinError 5] Access is denied` during pip install

**Solution:**
1. Close all Python processes (including VS Code terminals)
2. Delete `.venv` folder
3. Recreate venv from scratch

```powershell
Remove-Item -Recurse -Force .venv
python -m venv .venv
```

### Issue: Slow PyTorch performance on CPU

**Expected:** CPU execution is slower than GPU, but sufficient for testing.

**Optimization:**
- Use batch processing
- Reduce model complexity
- Consider cloud GPU instances for production

### Issue: Dependencies conflict (e.g., pydantic version)

**Solution:** These warnings are non-critical if all core imports work. To resolve:

```powershell
pip install --upgrade pydantic
```

---

## Verification Checklist

After setup, verify these components:

```powershell
# Test core imports
python -c "from codex.core.spiralcode_x_model import codex; print('✅ Codex loaded')"
python -c "from nexus import nexus_engine; print('✅ Nexus loaded')"
python -c "from sensus import sensusEngine; print('✅ Sensus loaded')"
python -c "from cortex import cognitive_bridge_service; print('✅ Cortex loaded')"

# Test benchmarks
python benchmarks/benchmark_suite.py
```

---

## Performance Notes

### CPU vs GPU

| Operation | CPU (Intel i7) | GPU (CUDA) |
|-----------|----------------|------------|
| Model initialization | ~0.3s | ~0.1s |
| Inference (single) | ~0.01s | ~0.001s |
| Batch (100) | ~1.5s | ~0.2s |
| Training epoch | ~60s | ~8s |

**Recommendation:** CPU is sufficient for:
- Development and testing
- Benchmark validation
- Low-volume inference (<100 req/min)

GPU recommended for:
- Training large models
- High-volume production
- Real-time processing

---

## Maintenance

### Update Dependencies

```powershell
python -m pip list --outdated
python -m pip install --upgrade <package>
```

### Freeze Environment

```powershell
python -m pip freeze > requirements-frozen.txt
```

### Clean Rebuild

```powershell
Remove-Item -Recurse -Force .venv
python -m venv .venv
# Re-run installation steps
```

---

## Integration with VS Code

### Configure Python Interpreter

1. Press `Ctrl+Shift+P`
2. Select "Python: Select Interpreter"
3. Choose `.venv\Scripts\python.exe`

### settings.json

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.envFile": "${workspaceFolder}/.env",
  "python.terminal.activateEnvironment": true
}
```

### .env file

```ini
PYTHONPATH=C:\Users\youruser\source\repos\SpiralCortex-v2.0
PYTHONIOENCODING=utf-8
```

---

## Phase 3 Validation Status

**Environment Status:** ✅ **Operational**

- Python 3.12.x with venv: ✅
- PyTorch 2.9.0+cpu: ✅
- All core dependencies: ✅
- PYTHONPATH configured: ✅
- UTF-8 encoding: ✅
- Benchmark runner: ✅ (9/18 passing)

**Validated:** October 26, 2025  
**Tag:** v2.0.2-stable-phase3

---

## Resources

- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [Python venv Documentation](https://docs.python.org/3/library/venv.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SpiralCortex v2.0 Phase 3 Results](PHASE_3_DYNAMIC_COHERENCE.md)

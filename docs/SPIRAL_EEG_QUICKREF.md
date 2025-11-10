# SpiralEEG Quick Reference

## Commands

```powershell
# Run full benchmark suite
python run_spiral_eeg.py --spiral-eeg

# Single scenario
python run_spiral_eeg.py --spiral-eeg --scenario-filter baseline

# Custom config
python run_spiral_eeg.py --spiral-eeg --scenarios custom.yaml --outdir results/custom

# Run all workflows
python run_spiral_eeg.py --all
```

## Perturbation Types

| Type | Parameters |
|------|------------|
| `sec_push` | valence, arousal, hazard, duration |
| `sec_noise` | sigma, duration |
| `symbolic_bias` | psi_bias, duration |
| `symbolic_noise` | sigma, duration |
| `input_noise` | sigma, duration |
| `input_dropout` | p, duration |
| `ethics_conflict` | intensity, duration |
| `value_shift` | target, delta, duration |
| `lambda_shock` | target_lambda, duration |

## Key Metrics

- **recovery_steps**: Time to return to baseline
- **lambda_star**: Equilibrium coupling parameter
- **phase_lock_deg**: Phase alignment (0°=perfect, 90°=neutral, 180°=anti)
- **ccs_cv_final**: Cognitive coherence stability
- **sec_drift_cv**: Emotional drift stability
- **phi_prime_mean**: Elastic consciousness
- **phi_iit_mean**: IIT consciousness

## File Structure

```
results/spiral_eeg/
├── SUMMARY.csv              # All scenarios & seeds
├── scenario_id/
│   └── seed_N/
│       ├── trace.parquet    # Time series data
│       ├── metrics.json     # Computed metrics
│       └── *.png            # Visualizations
```

## Analysis Examples

### Load Summary
```python
import pandas as pd
df = pd.read_csv("results/spiral_eeg/SUMMARY.csv")
print(df.groupby("scenario")["recovery_steps"].describe())
```

### Load Trace
```python
df = pd.read_parquet("results/spiral_eeg/baseline/seed_42/trace.parquet")
print(df[["t", "lambda", "phi_prime", "sec_drift"]].head())
```

### Custom Metrics
```python
from benchmarks.spiral_eeg.metrics import compute_adaptation_metrics
metrics = compute_adaptation_metrics("path/to/trace.parquet")
```

### Visualizations
```python
from benchmarks.spiral_eeg.visualize import make_all_plots
make_all_plots("path/to/run_dir")
```

## 28 Measurable Dimensions

### Core (13)
phi, psi, lambda, phi_prime, phi_iit, cxy0, iae_phi, si, ei, sec_drift_core, sec_entropy_core, corr_mag, ccs

### Emotional (10)
sec_valence, sec_arousal, sec_hazard, rh_res, rh_harm, rh_amp, rh_coh, rh_cplx, sec_drift, sec_entropy

### Trace Bounds (5)
phi_min, phi_max, psi_min, psi_max, corr_mag_mean

## Scenario Template

```yaml
scenarios:
  - id: my_scenario
    label: "My Custom Scenario"
    perturbations:
      - at: 1000
        kind: "sec_push"
        params: { valence: 0.8, arousal: 0.7, hazard: 0.2, duration: 500 }
      - at: 3000
        kind: "lambda_shock"
        params: { target_lambda: 0.9, duration: 300 }
```

## Common Issues

**Issue**: `recovery_steps: -1`  
**Solution**: System didn't recover. Reduce perturbation intensity or increase observation window.

**Issue**: All metrics are NaN  
**Solution**: Check that component handles are properly initialized in orchestrator.

**Issue**: Parquet import error  
**Solution**: Install pyarrow: `pip install pyarrow`

**Issue**: Missing plots  
**Solution**: Install matplotlib: `pip install matplotlib`

## Integration with Tests

1. Run tests to discover attractors:
   ```powershell
   pytest tests/test_core_hypotheses.py -v
   ```

2. Run SpiralEEG to measure recovery:
   ```powershell
   python run_spiral_eeg.py --spiral-eeg
   ```

3. Compare results:
   ```python
   # Test result: λ* ≈ 0.25
   # SpiralEEG result: lambda_star = 0.247 ± 0.018
   # ✓ Confirmed under stress
   ```

## See Also

- **benchmarks/spiral_eeg/README.md** - Full documentation
- **docs/SPIRAL_EEG_INTEGRATION.md** - Integration guide
- **docs/MEASURABLE_DATA_POINTS.md** - Complete metric list
- **docs/TEST_PHILOSOPHY_V2.md** - Observational framework

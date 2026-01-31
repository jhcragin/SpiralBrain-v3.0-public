# Sample Implementation Excerpts

This document provides illustrative excerpts from the implementation used in the reported experiments. These fragments are provided for conceptual clarity only and are not sufficient to execute the system.

## Observation Aggregation (Illustrative)

```python
flow_summary = {
    "speed_mean": np.mean(speed),
    "speed_max": np.max(speed),
    "vorticity_mean": np.mean(vorticity),
}
obs_vector = project_to_128d(flow_summary)
```

## Parameter Modulation Hook (Illustrative)

```python
if step % adaptation_interval == 0:
    nu, dt = sensus_modulation(obs_vector)
    nu = clamp(nu, nu_min, nu_max)
    dt = clamp(dt, dt_min, dt_max)
```

These excerpts illustrate the nature of the coupling without exposing the full runtime or decision logic.
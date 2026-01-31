# Experiment Specification: Navier–Stokes Coupling

This document specifies the experimental configuration used in the paper. All values and constraints listed here correspond exactly to the reported results.

## Physical System

- Domain: 2D incompressible Navier–Stokes
- Grid resolution: 64 × 64
- Boundary conditions: No-slip on all boundaries
- Initial condition: Centered Gaussian velocity perturbation
- Pressure solve: Successive over-relaxation (SOR)
- Simulation horizon: 50 timesteps

## Cognitive Coupling

- Coupling interval: Every 10 timesteps
- Observations provided to the cognitive system:
  - Aggregate flow statistics (mean, max, variance, vorticity summaries)
  - Fixed projection into a 128-dimensional observation vector
- Permitted modulations:
  - Kinematic viscosity (ν)
  - Simulation timestep (Δt)
- Forbidden modulations:
  - Direct velocity or pressure forcing
  - Boundary condition modification
  - External energy injection

## Experimental Conditions

Four sequential observer-effect conditions were evaluated:

1. Baseline (no coupling)
2. Observer (passive observation only)
3. Regulator (active modulation)
4. Adaptive regulator (full regulatory intelligence)

All conditions were evaluated within the same system instance to test for carryover effects.
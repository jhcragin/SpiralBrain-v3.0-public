Supplementary Robustness Run: 20 Random Emotional Profiles

This is a supplementary robustness experiment for the paper "Emotion-Conditioned Risk Posture in Crypto Markets".

Purpose: Demonstrate that the buy/hold participation bifurcation observed in the canonical 6-profile run persists under randomized emotional profiles.

Key Details:
- Profile Count: 20
- Profile Generation: Randomly sampled from valid parameter ranges (valence [-1,1], arousal [0,1], hazard [0,1], flex_level [-1,1])
- Seed: 42 (for reproducibility)
- Market Window: Same as canonical run (Dec 4, 2025 – Feb 1, 2026)
- Git Commit Hash: [to be filled if needed]
- Timestamp: 2026-02-01

Results Summary:
- 16 profiles: 100% buy signals
- 4 profiles: 100% hold signals
- 0 sell signals (enforced binary space)

This run is not the reference experiment. It provides supporting evidence for robustness but does not redefine the canonical claims.

For verification, use verify_reference_run.py with this directory.
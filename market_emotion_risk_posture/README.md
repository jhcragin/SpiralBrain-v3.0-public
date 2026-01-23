# Emotion-Conditioned Risk Posture in Crypto Markets

## Overview

This paper reports a *reproducible, audit-bundled* experiment: SpiralBrain v3.0 is exposed to real market context (Fear \& Greed sentiment + BTC price/volume) and emits a discrete market posture decision (buy/hold/sell) under multiple emotional profiles.

The objective is not price-prediction performance. The objective is to measure how emotion-conditioned regulation changes *risk posture selection* given the same external market context.

## Grounding and Constraints

- **No synthetic data**: inputs are retrieved from real upstream providers.
- **Fail-loudly**: no placeholders or silent fallbacks.
- **Audit bundle**: raw upstream payloads are archived (gzipped) and hashed; the exact `market_data_used.json` passed to the brain is saved and hashed.

## Provable Claims (Artifact-Based)

All quantitative results referenced in this paper must be traceable to:

- A run directory under `results/market_emotion_research_*/`
- A `summary_report_*.json` file
- A `provenance/` directory containing:
  - `raw/<sha>.json.gz` for upstream payloads
  - `index.json`
  - `market_data_used.json`

## Reproducibility

1. Run the benchmark:

   - `python benchmarks/market_emotion_prediction_v3.py --mode research --days 60`

2. Verify provenance and export paper tables:

   - `python analyze_market_emotion_results.py results/market_emotion_research_YYYYMMDD_HHMMSS`

3. Compile LaTeX:

   - Update the `\input{...}` path in `market_emotion_risk_posture.tex` to point at the chosen run’s `paper_exports/profile_summary_table.tex`.

## Status

- Outline: draft
- LaTeX: scaffolded
- Next: write Methods + Results narrative tied directly to `summary_report_*.json` and the provenance hashes.

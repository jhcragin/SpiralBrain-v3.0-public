# Results Folder: Confirmable Artifacts for SpiralBrain v3.0 Regularities

This folder contains artifacts supporting the confirmable research standard adopted in the manuscript. These are **not** full replication bundles but auditability aids for the reported empirical regularities.

## Scope and Limits

- **Purpose**: Enable independent verification that the 9 empirical discoveries derive systematically from high-volume runs, without requiring re-execution of the non-redistributable SpiralBrain v3.0 engine.
- **Contents**: Summaries of internal metrics, manifests of experiment metadata, and cryptographic hashes of original logs.
- **Exclusions**: No raw external data (e.g., BTC prices, MMLU questions), no domain-specific code, no full pipelines. Those reside in companion RI papers.
- **Legal Note**: Artifacts confirm runs occurred but do not constitute redistribution of the core engine.

## Structure

- `manifests/`: JSON files with experiment IDs, dates, SpiralBrain version hashes, and which regularity is corroborated.
- `summaries/`: JSON files with only internal metrics (coherence ranges, SEC drift bounds, recovery times, posture flags).
- `hashes/`: SHA-256 hashes of archived logs, datasets, and scripts.

## Verification

To verify a claim:
1. Check the manifest for experiment metadata.
2. Review the summary for relevant internal metrics.
3. Compare hashes against your own archives if available.

For full domain logic or data, refer to the cited companion papers.
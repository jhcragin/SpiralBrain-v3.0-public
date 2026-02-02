# Emotion-Conditioned Risk Posture in Crypto Markets

## Working Title (can change)

**Emotion-Conditioned Risk Posture Selection Under Real Market Inputs**

## 1. Introduction
- Motivation: regulation shapes decisions, not just outputs
- Task framing: posture selection (buy/hold/sell) under emotional profiles
- What is being claimed vs not claimed

## 2. Data and Provenance
- Upstream sources:
  - Fear & Greed Index (alternative.me)
  - BTC market chart (CoinGecko)
- Alignment methodology (UTC day key)
- Audit bundle:
  - raw payload gz artifacts keyed by SHA-256
  - deterministic hash of `market_data_used.json`

## 3. System and Experimental Setup
- SpiralBrain v3.0 entry path used (documented brain entry)
- Emotional profiles tested
- Prediction contract (required output fields; no fallback)

## 4. Results
- Summary metrics per profile:
  - direction distribution (buy/hold/sell)
  - avg confidence
- Table: profile summary (auto-generated from run artifacts)

## 5. Analysis
- Inter-profile posture separation
- Interpretation as emotion-conditioned regulation (not market alpha)

## 6. Limitations
- Single market (BTC) and limited window (60 days)
- No trading simulation / PnL claims
- One architecture instrument

## 7. Reproducibility Checklist
- Commands to reproduce
- What files must match hashes
- How to verify offline using provenance bundle

## 8. Conclusion
- Restate: measurable regulation-induced posture differences under shared real inputs

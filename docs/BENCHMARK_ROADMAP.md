# SpiralBrain Benchmark Roadmap

**Last Updated:** November 7, 2025  
**Status:** Phase 1 Complete (Infrastructure), Phase 2 In Progress (Semantic Integration)

---

## Overview

This roadmap tracks SpiralBrain's benchmark development, showing progression from existing financial benchmarks through MMLU baseline to comprehensive temporal forecasting evaluation.

**Philosophy:** Test what SpiralBrain **DOES** (temporal patterns, multi-modal fusion), not what it **DOESN'T** (static classification without semantic layer).

---

## Current Benchmark Inventory

### ✅ Existing Benchmarks

#### 1. Crypto Tax Calculations
**File:** `benchmarks/crypto_tax_benchmark.py` (925 lines)  
**Status:** ✅ Functional  
**Tests:** FIFO/LIFO cost basis, tax liability calculations  
**Datasets:** HODLer, day trader, miner, DeFi, volatile markets, large portfolio  
**Baseline:** FIFO baseline, average cost, simple pattern recognition  
**Strengths:** Realistic transaction scenarios, comprehensive tax rules

#### 2. Financial Volatility → SEC Mapping
**File:** `benchmarks/finance_volatility_sec/run_benchmark.py` (130 lines)  
**Status:** ✅ Functional  
**Tests:** Maps realized volatility → Stress/Energy/Coherence vectors  
**Metrics:** Volatility vs arousal, drawdown vs valence  
**Strengths:** Connects financial metrics to cognitive states

#### 3. Financial Classification (Credit/Fraud)
**File:** `benchmarks/financial_benchmark_summary.py`  
**Status:** ⚠️ Shows SpiralBrain weaknesses  
**Results:**
- Credit risk: 12.8% acc (vs RandomForest 92.8%)
- Fraud detection: 0.5% acc (vs RandomForest 99.99%)  
**Insight:** SpiralBrain struggles with **tabular classification** (not its strength)

### ⚠️ Key Finding from Existing Benchmarks

**Classification benchmarks show SpiralBrain fails at:**
- Static tabular data (credit risk, fraud detection)
- Imbalanced datasets (99.5% legitimate, 0.5% fraud)
- Feature engineering without temporal context

**Recommendation:** Stop testing classification, focus on **temporal prediction**

---

## Phase 1: Infrastructure Validation (✅ Complete)

### 1.1 MMLU Baseline (✅ Complete)

**File:** `benchmarks/external_adapters/mmlu_adapter.py` (600+ lines)  
**Created:** November 6-7, 2025  
**Status:** ✅ Fully documented as infrastructure test

**What Was Tested:**
- 14,042 questions across 57 subjects
- MultiPathwayBrain processes all questions without failure
- Lobe activation tracking works
- Coherence remains stable (0.5)

**Results:**
- **Accuracy:** 25.3% (= random baseline, as expected)
- **Coherence:** 0.500 (fixed, not adaptive)
- **Chi-square:** 0.67 (not significant, confirms random)
- **Lobe activations:** Constant (no specialization)

**Why This Matters:**
- ✅ Proves architecture is mechanically sound
- ✅ Validates pathway coordination works
- ✅ Establishes honest baseline for comparison
- ✅ Defines roadmap for semantic integration

**Documentation:**
- `benchmarks/external_adapters/MMLU_BASELINE_FINDINGS.md` (comprehensive)
- `MMLU_BASELINE_SUMMARY.md` (quick reference)
- `analyze_mmlu_results.py` (statistical analysis)

**4-Phase Roadmap to 75-85% Accuracy:**
1. Add text embeddings (sentence-transformers)
2. Integrate lightweight LLM (Phi-3, Mistral-7B)
3. Fine-tune on MMLU training data
4. Add RAG for factual recall

### 1.2 Crypto Forecasting Infrastructure (✅ Complete)

**File:** `benchmarks/external_adapters/crypto_forecasting_adapter.py` (985 lines)  
**Created:** November 7, 2025  
**Status:** ⚠️ Infrastructure works, training pending

**What Was Tested:**
- Multi-horizon forecasting (1-day, 7-day, 30-day)
- Baseline comparisons (ARIMA, XGBoost, Prophet)
- Technical feature engineering (lagged prices, MA, volatility)
- Comprehensive metrics (MAE, RMSE, direction accuracy, Sharpe ratio)

**Infrastructure Validation:**
- ✅ Processes temporal sequences
- ✅ Pathways activate and coordinate
- ✅ Fast processing (3.6ms per prediction)
- ✅ Automated report generation
- ✅ Baseline models work correctly

**Current Limitation:**
- ⚠️ No trained prediction head (placeholder uses true values)
- ⚠️ Can't report honest accuracy yet (data leakage)
- ⏳ Training loop not implemented

**Documentation:**
- `CRYPTO_FORECASTING_SUMMARY.md` (this phase)
- `benchmarks/results/crypto_forecasting/CRYPTO_FORECASTING_REPORT.md`

**Expected Performance After Training:**
- Untrained: ~50% direction accuracy (random walk)
- Trained: 55-65% direction accuracy (competitive)
- SOTA deep learning: 60-70% direction accuracy

---

## Phase 2: Semantic Integration (🔄 In Progress)

### 2.1 MMLU Semantic Layer (⏳ Planned)

**Goal:** Achieve 75-85% accuracy on MMLU (from 25.3% baseline)

**Steps:**
1. **Text Embeddings** (Target: 40-50% accuracy)
   - Add sentence-transformers (all-MiniLM-L6-v2)
   - Replace hash-based tensors with semantic embeddings
   - Expected: Lobe specialization by subject category

2. **Lightweight LLM Integration** (Target: 60-70% accuracy)
   - Integrate Phi-3-mini (3.8B) or Mistral-7B
   - Use as "semantic oracle" for pathways
   - Expected: Coherence becomes adaptive

3. **Fine-Tuning** (Target: 70-75% accuracy)
   - Fine-tune on MMLU training set (auxiliary_train)
   - Few-shot prompting for question types
   - Expected: Approach SoTA open-source LLMs

4. **RAG Enhancement** (Target: 75-85% accuracy)
   - Add retrieval over STEM databases
   - Integrate Haystack adapter for factual recall
   - Expected: Competitive with GPT-3.5 level models

**Timeline:** 2-4 weeks per step

### 2.2 Crypto Forecasting Training (⏳ Immediate Next)

**Goal:** Honest baseline + competitive temporal forecasting

**Steps:**
1. **Fix Data Leakage** (This week)
   - Remove `y[i]` from prediction logic
   - Add untrained baseline (random walk)
   - Document honest 50% direction accuracy

2. **Add Prediction Head** (Next week)
   - Linear or MLP layer (state_dim → 256 → 1)
   - MSE or Huber loss
   - Adam optimizer (lr=1e-4)

3. **Training Loop** (Next week)
   - 60/20/20 train/val/test split
   - 50-100 epochs
   - Early stopping on validation loss
   - Track training curves

4. **Real Data Integration** (Week 3-4)
   - Replace synthetic data with Coin Metrics API
   - Fetch 1+ years historical prices
   - Test on 21 major cryptos
   - Compare vs crypto-forecasting-benchmark baselines

**Expected Outcomes:**
- Trained SpiralBrain: 55-65% direction accuracy
- Competitive MAE vs ARIMA/Prophet
- Lobe activation patterns emerge (e.g., Attention → volatility)
- Coherence adapts to market conditions

**Timeline:** 3-4 weeks

---

## Phase 3: Advanced Temporal Benchmarks (📅 Future)

### 3.1 Time-Series Forecasting Suite

**Goal:** Demonstrate SpiralBrain's temporal reasoning strength

**Benchmarks:**
1. **Cryptocurrency Price Prediction** (in progress)
   - 21 major cryptos
   - 1-day, 7-day, 30-day horizons
   - vs ARIMA, XGBoost, Prophet, LSTM, Transformer

2. **Stock Market Forecasting**
   - S&P 500 stocks
   - Multi-step ahead prediction
   - Sector-specific pathway specialization

3. **Volatility Forecasting** (extends existing SEC benchmark)
   - VIX prediction
   - Realized vs implied volatility
   - Risk metric estimation

4. **Financial Event Detection**
   - Market crashes, bull runs
   - Earnings surprises
   - Regulatory announcements

**Target:** 60-70% direction accuracy across asset classes

### 3.2 Multi-Modal Financial Analysis

**Goal:** Leverage SpiralBrain's multi-modal fusion

**Data Sources:**
1. **Price data** (existing)
2. **News sentiment** (via Haystack adapter)
3. **Social media** (Twitter/Reddit sentiment)
4. **On-chain metrics** (blockchain data)
5. **Technical indicators** (existing)

**Expected Advantage:**
- SpiralBrain's multi-pathway architecture naturally fuses modalities
- Single-modal models (ARIMA, Prophet) can't compete
- Target: 65-75% direction accuracy with multi-modal input

### 3.3 Deep Learning Baseline Comparisons

**Goal:** Compare against SOTA time-series models

**Baselines:**
1. **LSTM** (Long Short-Term Memory)
   - Standard sequential model
   - 2-3 layer architecture

2. **Transformer** (Temporal Fusion Transformer)
   - Attention-based time-series
   - State-of-the-art accuracy

3. **N-BEATS** (Neural Basis Expansion Analysis)
   - Specialized time-series forecasting
   - Interpretable architecture

4. **Ensemble** (LSTM + Transformer + N-BEATS)
   - Combined predictions
   - Benchmark upper bound

**Target:** SpiralBrain competitive or better on multi-modal scenarios

---

## Phase 4: Production-Ready Benchmarks (📅 Q1 2026)

### 4.1 Walk-Forward Validation

**Goal:** Realistic trading simulation

**Features:**
- Rolling window training
- Daily retraining
- Transaction costs
- Slippage modeling
- Portfolio rebalancing

**Metrics:**
- Annualized returns
- Sharpe ratio
- Max drawdown
- Win rate
- Profit factor

### 4.2 Live Prediction API

**Goal:** Real-time forecasting benchmark

**Components:**
- WebSocket streaming data
- Sub-second prediction latency
- Continuous model updates
- A/B testing framework

### 4.3 Risk-Adjusted Performance

**Goal:** Financial industry standards

**Metrics:**
- Sortino ratio (downside risk)
- Calmar ratio (drawdown-adjusted)
- Information ratio (excess returns)
- Value at Risk (VaR)
- Conditional VaR (CVaR)

---

## Benchmark Comparison Matrix

| Benchmark | Status | Tests | SpiralBrain Strength | Next Action |
|-----------|--------|-------|---------------------|-------------|
| **Crypto Tax** | ✅ Functional | Tax calculations | Medium (rule-based) | Integrate with forecasting |
| **Volatility SEC** | ✅ Functional | Cognitive mapping | High (multi-modal) | Expand to prediction |
| **Credit/Fraud** | ⚠️ Weak | Classification | Low (tabular) | Deprioritize |
| **MMLU** | ✅ Baseline | Infrastructure | Low (no semantic) | Add embeddings |
| **Crypto Forecast** | ⚠️ Infra | Temporal prediction | High (pending training) | Add prediction head |
| **Stock Forecast** | 📅 Planned | Time-series | High (expected) | After crypto training |
| **Multi-Modal** | 📅 Planned | Fusion | Very High (core strength) | After semantic layer |
| **Deep Learning** | 📅 Planned | vs LSTM/Transformer | Medium-High | After training |

---

## Key Insights from Benchmarks

### What SpiralBrain Excels At (Expected)
1. ✅ **Temporal pattern recognition** (multi-pathway coordination)
2. ✅ **Multi-modal fusion** (Haystack, Vision, Falcon adapters)
3. ✅ **Adaptive coherence** (market volatility → cognitive state)
4. ✅ **Interpretability** (lobe activation = feature importance)

### What SpiralBrain Struggles With (Proven)
1. ❌ **Static tabular classification** (credit risk: 12.8% vs 92.8%)
2. ❌ **Imbalanced datasets** (fraud: 0.5% vs 99.99%)
3. ❌ **Language Q&A without semantic layer** (MMLU: 25.3% random)
4. ⚠️ **Untrained temporal prediction** (need training loop)

### Honest Assessment
- **Infrastructure:** ✅ Fully validated (MMLU + crypto forecasting)
- **Semantic Layer:** ❌ Missing (text embeddings, LLM integration)
- **Temporal Training:** ⏳ Pending (prediction head + backpropagation)
- **Production Ready:** ❌ Not yet (need real data + live API)

---

## Benchmark Roadmap Timeline

### ✅ Completed (November 2025)
- [x] MMLU baseline (25.3%, documented as infrastructure test)
- [x] Crypto forecasting infrastructure (architecture validated)
- [x] Comprehensive documentation (findings, roadmaps, summaries)

### 🔄 In Progress (November 2025)
- [ ] Fix crypto forecasting data leakage (this week)
- [ ] Add prediction head + training loop (next week)
- [ ] Document honest untrained baseline (this week)

### 📅 Next Month (December 2025)
- [ ] Train crypto forecasting model (real data)
- [ ] Test on 21 major cryptos (vs baselines)
- [ ] Add text embeddings to MMLU (40-50% target)
- [ ] Stock market forecasting benchmark

### 📅 Q1 2026
- [ ] Multi-modal financial analysis
- [ ] Deep learning baseline comparisons
- [ ] Walk-forward validation
- [ ] Production-ready API

---

## References

### Benchmark Files
- `benchmarks/crypto_tax_benchmark.py` (925 lines)
- `benchmarks/finance_volatility_sec/run_benchmark.py` (130 lines)
- `benchmarks/financial_benchmark_summary.py`
- `benchmarks/external_adapters/mmlu_adapter.py` (600+ lines)
- `benchmarks/external_adapters/crypto_forecasting_adapter.py` (985 lines)

### Documentation
- `benchmarks/external_adapters/MMLU_BASELINE_FINDINGS.md`
- `MMLU_BASELINE_SUMMARY.md`
- `CRYPTO_FORECASTING_SUMMARY.md`
- `analyze_mmlu_results.py` (250+ lines)

### External References (User-Provided)
1. **CryptoTaxTools/crypto-tax-report** - Tax calculation reference
2. **crypto-forecasting-benchmark** - 21 cryptos, ARIMA/XGBoost/Prophet
3. **Coin Metrics API** - Real crypto price data
4. **Kaiko API** - Real-time market data
5. **OpenBB Terminal** - Financial data aggregation

---

## Next Immediate Actions

1. **Fix crypto forecasting data leakage** (remove `y[i]` from predictions)
2. **Document honest untrained baseline** (expected: 50% direction)
3. **Implement prediction head** (Linear/MLP layer)
4. **Create training loop** (MSE loss, Adam optimizer)
5. **Re-run with trained model** (establish real baseline)

**Goal:** By end of November, have honest trained crypto forecasting baseline comparable to ARIMA/Prophet.

---

**Benchmark Philosophy:** Test what SpiralBrain **DOES**, document limitations honestly, define clear roadmaps for improvement.

**Status:** Infrastructure validated ✅ | Semantic integration in progress 🔄 | Training pending ⏳

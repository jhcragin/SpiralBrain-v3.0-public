# Crypto Forecasting Benchmark Report

**Generated:** 2025-11-30 19:11:41

## Executive Summary

This benchmark evaluates SpiralBrain's temporal prediction capabilities
on cryptocurrency price forecasting against baseline models (ARIMA, XGBoost, Prophet).

### Overall Statistics

- **Cryptocurrencies Tested:** 2
- **Forecasting Horizons:** [1, 7, 30] days
- **Total Benchmark Runs:** 24
- **Models Compared:** SpiralBrain, ARIMA, XGBoost, Prophet

### Model Win Rates

- **SpiralBrain:** 6/6 (100.0%)
- **ARIMA:** 0/6 (0.0%)
- **XGBoost:** 0/6 (0.0%)
- **Prophet:** 0/6 (0.0%)

### Average Metrics by Model

#### SpiralBrain

- **MAE:** $1048.99
- **Direction Accuracy:** 53.5%
- **Sharpe Ratio:** -1.04

#### ARIMA

- **MAE:** $3654.37
- **Direction Accuracy:** 51.8%
- **Sharpe Ratio:** -6.54

#### XGBoost

- **MAE:** $4922.42
- **Direction Accuracy:** 0.0%
- **Sharpe Ratio:** 0.00

#### Prophet

- **MAE:** $3698.41
- **Direction Accuracy:** 57.9%
- **Sharpe Ratio:** -2.83

### SpiralBrain Diagnostics

- **Average Coherence:** 0.500
- **Average Processing Time:** 13.2ms per prediction

#### Average Lobe Activation

- **Reasoning:** 0.500
- **Attention:** 0.500
- **Sensory:** 0.500
- **Motor:** 0.500

## Detailed Results by Cryptocurrency

### BTC

#### 1-Day Forecast

| Model | MAE | RMSE | Direction Acc | Sharpe |
|-------|-----|------|---------------|--------|
| SpiralBrain | $1940.96 | $2485.58 | 53.8% | -1.56 |
| Prophet | $6354.78 | $7337.84 | 53.8% | -3.10 |
| ARIMA | $7055.49 | $8355.52 | 50.8% | -7.37 |
| XGBoost | $9255.40 | $10940.26 | 0.0% | 0.00 |

#### 7-Day Forecast

| Model | MAE | RMSE | Direction Acc | Sharpe |
|-------|-----|------|---------------|--------|
| SpiralBrain | $2084.64 | $2503.05 | 55.9% | -2.34 |
| Prophet | $5975.45 | $7130.11 | 54.2% | -3.17 |
| ARIMA | $7479.78 | $8674.06 | 49.2% | -5.55 |
| XGBoost | $8746.51 | $10531.18 | 0.0% | 0.00 |

#### 30-Day Forecast

| Model | MAE | RMSE | Direction Acc | Sharpe |
|-------|-----|------|---------------|--------|
| SpiralBrain | $1938.33 | $2534.56 | 61.1% | 0.49 |
| ARIMA | $6440.57 | $7757.01 | 38.9% | -2.69 |
| Prophet | $8965.42 | $10156.29 | 52.8% | -2.90 |
| XGBoost | $9119.20 | $10548.87 | 0.0% | 0.00 |

### ETH

#### 1-Day Forecast

| Model | MAE | RMSE | Direction Acc | Sharpe |
|-------|-----|------|---------------|--------|
| SpiralBrain | $102.69 | $137.49 | 52.3% | -1.41 |
| Prophet | $278.60 | $334.51 | 61.5% | -2.83 |
| ARIMA | $318.32 | $371.29 | 56.9% | -9.70 |
| XGBoost | $669.81 | $807.46 | 0.0% | 0.00 |

#### 7-Day Forecast

| Model | MAE | RMSE | Direction Acc | Sharpe |
|-------|-----|------|---------------|--------|
| SpiralBrain | $115.53 | $152.51 | 50.8% | -1.82 |
| Prophet | $257.70 | $309.22 | 61.0% | -2.86 |
| ARIMA | $341.91 | $388.05 | 59.3% | -8.25 |
| XGBoost | $728.48 | $846.42 | 0.0% | 0.00 |

#### 30-Day Forecast

| Model | MAE | RMSE | Direction Acc | Sharpe |
|-------|-----|------|---------------|--------|
| SpiralBrain | $111.77 | $156.23 | 47.2% | 0.39 |
| ARIMA | $290.14 | $341.79 | 55.6% | -5.67 |
| Prophet | $358.49 | $407.47 | 63.9% | -2.12 |
| XGBoost | $1015.10 | $1046.43 | 0.0% | 0.00 |

## Conclusions

### Strengths

- Multi-pathway architecture enables adaptive forecasting
- Coherence tracking provides confidence estimation
- Lobe activation patterns reveal feature importance

### Areas for Improvement

- Add proper prediction head (linear/MLP on top of pathways)
- Train on real historical crypto data
- Implement attention mechanism for relevant features
- Integrate with real-time market data feeds

### Next Steps

1. Replace synthetic data with Coin Metrics / Kaiko API
2. Add proper training loop with backpropagation
3. Implement cross-validation for robust evaluation
4. Compare against deep learning baselines (LSTM, Transformer)
5. Test on additional asset classes (stocks, commodities)

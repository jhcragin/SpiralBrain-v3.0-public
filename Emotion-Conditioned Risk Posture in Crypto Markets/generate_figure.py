import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import json

# Load real data from the experiment run
with open('c:/Users/johnc/source/repos/SpiralBrain-v3.0/results/market_emotion_research_20260201_204741/provenance/market_data_used.json', 'r') as f:
    market_data = json.load(f)

# Extract data
dates = [datetime.fromisoformat(item['timestamp'][:-6]) for item in market_data]  # Remove timezone offset
btc_prices = [item['btc_price'] for item in market_data]
fng_values = [item['fear_greed_index'] for item in market_data]

# Plot
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(dates, btc_prices, color='blue', label='BTC Price (USD)')
ax1.set_xlabel('Date')
ax1.set_ylabel('BTC Price (USD)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(dates, fng_values, color='red', label='Fear & Greed Index')
ax2.set_ylabel('Fear & Greed Index', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.axhline(y=25, color='gray', linestyle='--', alpha=0.5, label='Fear/Neutral Threshold')
ax2.axhline(y=75, color='gray', linestyle='--', alpha=0.5, label='Greed Threshold')

fig.suptitle('BTC Price and Fear & Greed Index (Dec 4, 2025 – Feb 1, 2026)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('figures/btc_fng_timeline.png', dpi=150)
plt.show()
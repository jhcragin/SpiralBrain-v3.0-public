import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic data for the window Nov 22, 2025 – Jan 20, 2026 (60 days)
start_date = datetime(2025, 11, 22)
dates = [start_date + timedelta(days=i) for i in range(60)]

# Synthetic BTC price: starts at ~84.6k, recovers to ~88-97k, ends at ~88.3k, choppy
btc_prices = []
current_price = 84648
for i in range(60):
    if i < 10:
        current_price += np.random.uniform(-500, 1000)  # initial recovery
    elif i < 30:
        current_price += np.random.uniform(-1000, 1500)  # mid recovery
    else:
        current_price += np.random.uniform(-1500, 500)  # choppy end
    btc_prices.append(current_price)

# Synthetic Fear & Greed: starts at 10-13 (Extreme Fear), transitions to 20-50 (Fear/Neutral)
fng_values = []
for i in range(60):
    if i < 10:
        fng = np.random.uniform(10, 15)
    elif i < 30:
        fng = np.random.uniform(20, 40)
    else:
        fng = np.random.uniform(30, 50)
    fng_values.append(fng)

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

fig.suptitle('BTC Price and Fear & Greed Index (Nov 22, 2025 – Jan 20, 2026)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('figures/btc_fng_timeline.png', dpi=150)
plt.show()
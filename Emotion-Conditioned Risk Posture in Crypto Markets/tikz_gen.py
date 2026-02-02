import json

with open('results/market_emotion_participation_only_20260201/provenance/market_data_used.json', 'r') as f:
    data = json.load(f)

# Data is in reverse order, so reverse it for plotting from old to new
data = data[::-1]

btc_coords = [f'({i}, {item["btc_price"]:.2f})' for i, item in enumerate(data)]
fng_coords = [f'({i}, {item["fear_greed_index"]})' for i, item in enumerate(data)]

print('\\addplot[color=blue, mark=none] coordinates {')
for c in btc_coords:
    print(f'    {c}')
print('};')
print()
print('\\addplot[color=red, mark=none] coordinates {')
for c in fng_coords:
    print(f'    {c}')
print('};')
---
name: gia-vang
description: Get current gold prices from PNJ (Phu Nhuan Jewelry) - Vietnam's leading gold retailer. Returns buy/sell prices for PNJ and SJC gold across major cities including Ho Chi Minh, Hanoi, Da Nang, and Can Tho.
metadata:
  homepage: https://github.com/tinbeta/gia-vang-skill
  author: tinbeta
  version: 1.0.0
---

# gia-vang

## Instructions

When the user asks for gold prices, invoke the Python script to fetch real-time data from PNJ's official API.

### Step 1: Run the Script
Call the script to get current gold prices:

```bash
python3 scripts/gia_vang.py
```

### Step 2: Interpret Results
The script returns gold prices for:
- **PNJ Gold**: Phu Nhuan Jewelry's own gold brand
- **SJC Gold**: State-owned gold brand (widely recognized in Vietnam)

Prices are shown for major cities:
- TPHCM (Ho Chi Minh City)
- Ha Noi (Hanoi)
- Da Nang
- Can Tho

### Step 3: Present to User
Format the output clearly showing:
- Current date/time of the price
- Buy price (Gia Mua) - what PNJ pays to buy gold from customers
- Sell price (Gia Ban) - what customers pay to buy gold from PNJ
- Price differences between cities (if any)

### Optional Parameters
You can specify location for city-specific prices:

```bash
python3 scripts/gia_vang.py --location "TPHCM"
```

Or get specific gold types:
```bash
python3 scripts/gia_vang.py --type "SJC"     # SJC gold only
python3 scripts/gia_vang.py --jewelry        # Jewelry prices
```

## Invocation Triggers

You should invoke this skill when the user:
- Asks for current gold prices ("giá vàng hôm nay")
- Wants PNJ gold prices specifically
- Wants SJC gold prices
- Asks for gold prices in a specific city
- Wants to compare gold prices across locations

## Data Source

- **API**: `https://edge-api.pnj.io/ecom-frontend/v3/get-gold-price`
- **Provider**: PNJ (Phu Nhuan Jewelry)
- **Update frequency**: Real-time
- **Unit**: VND per tael (1 tael = 37.5g)

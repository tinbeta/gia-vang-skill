---
name: gia-vang
description: Get current gold prices from PNJ (Phu Nhuan Jewelry) - Vietnam's leading gold retailer. Returns buy/sell prices for PNJ and SJC gold across major cities.
metadata:
  homepage: https://github.com/tinbeta/gia-vang-skill/tree/main
  author: tinbeta
---

# gia-vang

Get gold prices (PNJ/SJC) from official API.

## Examples

* "Get gold price today"
* "PNJ gold price in Ho Chi Minh"
* "SJC gold price"
* "Giá vàng hôm nay"
* "Giá vàng PNJ"

## Instructions

Call the Python script with the following:

```bash
python3 scripts/gia_vang.py
```

The script returns PNJ and SJC gold prices for areas: TPHCM, Ha Noi, Da Nang, Can Tho.

Optional: Specify location for city-specific prices:
```bash
python3 scripts/gia_vang.py --location "TPHCM"
```

Or get specific gold types:
```bash
python3 scripts/gia_vang.py --type "SJC"
python3 scripts/gia_vang.py --jewelry
```

API endpoint: `https://edge-api.pnj.io/ecom-frontend/v3/get-gold-price`

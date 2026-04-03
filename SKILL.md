---
name: gia-vang
description: Get gold prices from PNJ
author: tinbeta
---

# gia-vang

Get gold prices (PNJ/SJC) from official API.

## Examples

- "Get gold price today"
- "PNJ gold price in Ho Chi Minh"
- "SJC gold price"

---

## Instructions

Run Python script to get gold prices:

```bash
python3 scripts/gia_vang.py
```

The script returns PNJ and SJC gold prices for areas: TPHCM, Ha Noi, Da Nang, Can Tho.

API endpoint: `https://edge-api.pnj.io/ecom-frontend/v3/get-gold-price`

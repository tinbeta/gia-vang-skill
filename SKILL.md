---
name: gia-vang
description: Lấy giá vàng từ PNJ
homepage: https://github.com/tinbeta/gia-vang-skill
author: tinbeta
version: 1.0.0
metadata:
  openclaw:
    emoji: 🥇
    requires:
      bins: [python3]
---

# gia-vang 🥇

Lấy giá vàng PNJ/SJC từ API chính thức.

## Cài đặt

Không cần cài đặt thêm, dùng Python có sẵn.

## Sử dụng

```bash
# Lấy giá vàng hiện tại
python3 scripts/gia_vang.py

# Lấy giá vàng khu vực cụ thể
python3 scripts/gia_vang.py --location "TPHCM"

# Lấy giá vàng SJC
python3 scripts/gia_vang.py --type "SJC"

# Lấy giá vàng nữ trang
python3 scripts/gia_vang.py --jewelry
```

## API

- **Endpoint:** `https://edge-api.pnj.io/ecom-frontend/v3/get-gold-price`
- **Method:** GET
- **Response:** JSON

## Output

```
🥇 Giá vàng PNJ - 05/02/2026 09:05:02

📍 TPHCM
  PNJ: Mua 175.400 | Bán 178.400
  SJC: Mua 175.800 | Bán 178.800

📍 Hà Nội
  PNJ: Mua 175.400 | Bán 178.400
  SJC: Mua 175.800 | Bán 178.800
...
```

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

# gia-vang

Lấy giá vàng PNJ/SJC từ API chính thức.

## Cài đặt

Không cần cài đặt thêm, dùng Python có sẵn.

## Sử dụng

```bash
python3 scripts/gia_vang.py
```

## API

- **Endpoint:** `https://edge-api.pnj.io/ecom-frontend/v3/get-gold-price`
- **Method:** GET

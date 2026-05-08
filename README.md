# Gia Vàng Skill

![Gia Vàng Skill Banner](assets/banner.svg)

Một skill/API nhỏ gọn dùng để lấy giá vàng từ PNJ (Phú Nhuận Jewelry) — một trong những thương hiệu vàng lớn và uy tín nhất tại Việt Nam.

## ✨ Tính năng

- Lấy giá vàng PNJ theo thời gian thực
- Dashboard realtime với FastAPI
- REST API tích hợp sẵn
- Hỗ trợ Python, Node.js và Rust
- Phù hợp cho AI Agents, automation và fintech
- Có thể mở rộng thêm nhiều nguồn giá vàng khác tại Việt Nam
- Phát hành theo giấy phép MIT

---

## 📌 Trường hợp sử dụng

Gia Vàng Skill có thể dùng cho:

- AI Assistant trả lời giá vàng
- Dashboard tài chính realtime
- Bot theo dõi giá vàng
- Automation cho Telegram/Discord
- Hệ thống theo dõi thị trường
- Ứng dụng fintech tại Việt Nam

---

## 🏗 Cấu trúc dự án

```bash
.
├── assets/
├── dashboard/
│   └── app.py
├── examples/
│   ├── nodejs/
│   └── rust/
├── python/
│   ├── gia_vang_skill/
│   └── requirements.txt
├── .github/workflows/
├── LICENSE
└── README.md
```

---

# 🚀 Chạy Dashboard Realtime

### Cài dependencies

```bash
pip install -r python/requirements.txt
```

### Chạy FastAPI dashboard

```bash
uvicorn dashboard.app:app --reload
```

### Mở trình duyệt

```text
http://127.0.0.1:8000
```

Dashboard sẽ tự động cập nhật giá vàng mỗi 10 giây.

---

# 🔌 REST API

### Lấy dữ liệu giá vàng

```text
GET /api/prices
```

Ví dụ dữ liệu:

```json
[
  {
    "provider": "PNJ",
    "type": "24K",
    "buy": "11800000",
    "sell": "12100000",
    "currency": "VND"
  }
]
```

---

# 🟨 Node.js Example

```bash
npm install axios cheerio
node examples/nodejs/pnj_price.js
```

---

# 🦀 Rust Example

```toml
[dependencies]
reqwest = { version = "0.12", features = ["json"] }
tokio = { version = "1", features = ["full"] }
scraper = "0.19"
```

```bash
cargo run
```

---

## 🔮 Kế hoạch phát triển

- Hỗ trợ giá vàng SJC/DOJI
- WebSocket realtime
- Biểu đồ lịch sử giá vàng
- SQLite/PostgreSQL
- Docker deployment
- SDK đa nền tảng
- AI phân tích xu hướng giá vàng

---

## 🛡 Giấy phép

Dự án được phát hành theo giấy phép MIT License.

---

## 👨‍💻 Tác giả

Phát triển và duy trì bởi Tinbeta.

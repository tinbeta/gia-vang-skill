# Gia Vàng Skill

![Gia Vàng Skill Banner](assets/banner.svg)

Một skill/API nhỏ gọn dùng để lấy giá vàng từ PNJ (Phú Nhuận Jewelry) — một trong những thương hiệu vàng lớn và uy tín nhất tại Việt Nam.

## ✨ Tính năng

- Lấy giá vàng PNJ theo thời gian thực
- Tích hợp đơn giản, nhẹ và dễ mở rộng
- Phù hợp cho AI Agents, automation và dashboard
- Có thể mở rộng thêm nhiều nguồn giá vàng khác tại Việt Nam
- Phát hành theo giấy phép MIT

---

## 📌 Trường hợp sử dụng

Gia Vàng Skill có thể dùng cho:

- AI Assistant trả lời giá vàng
- Dashboard tài chính
- Bot theo dõi giá vàng
- Automation cho Telegram/Discord
- Hệ thống theo dõi thị trường
- Ứng dụng fintech tại Việt Nam

---

## 🏗 Cấu trúc dự án

```bash
.
├── assets/
│   └── banner.svg
├── README.md
└── src/
```

---

## 🚀 Bắt đầu nhanh

### Clone repository

```bash
git clone https://github.com/tinbeta/gia-vang-skill.git
cd gia-vang-skill
```

### Cài đặt dependencies

```bash
# Ví dụ
pip install -r requirements.txt
```

### Chạy dự án

```bash
python main.py
```

---

## 📊 Ví dụ dữ liệu trả về

```json
{
  "brand": "PNJ",
  "gold_type": "24K",
  "buy_price": "11800000",
  "sell_price": "12100000",
  "currency": "VND"
}
```

---

## 🔮 Kế hoạch phát triển

Các tính năng dự kiến trong tương lai:

- Hỗ trợ giá vàng SJC
- Chế độ REST API
- Dashboard web
- Biểu đồ lịch sử giá vàng
- Cập nhật realtime bằng WebSocket
- Hỗ trợ đa ngôn ngữ

---

## 🛡 Giấy phép

Dự án được phát hành theo giấy phép MIT License.

---

## 👨‍💻 Tác giả

Phát triển và duy trì bởi Tinbeta.

Nếu bạn thấy dự án hữu ích, hãy cho repo một ⭐ trên GitHub.

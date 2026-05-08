from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from gia_vang_skill.client import PNJClient

app = FastAPI(title='Gia Vang Skill Dashboard')

HTML = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gia Vàng Realtime Dashboard</title>
    <style>
        body {
            background: #0f172a;
            color: white;
            font-family: Arial, sans-serif;
            padding: 40px;
        }

        h1 {
            color: #facc15;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: #111827;
        }

        th, td {
            padding: 14px;
            border-bottom: 1px solid #374151;
            text-align: left;
        }

        th {
            color: #facc15;
        }

        .updated {
            margin-top: 20px;
            color: #94a3b8;
        }
    </style>
</head>
<body>
    <h1>📈 Dashboard Giá Vàng Realtime</h1>

    <table>
        <thead>
            <tr>
                <th>Loại vàng</th>
                <th>Giá mua</th>
                <th>Giá bán</th>
                <th>Tiền tệ</th>
            </tr>
        </thead>
        <tbody id="gold-data"></tbody>
    </table>

    <div class="updated" id="updated"></div>

    <script>
        async function fetchPrices() {
            const response = await fetch('/api/prices');
            const data = await response.json();

            const tbody = document.getElementById('gold-data');
            tbody.innerHTML = '';

            data.forEach(item => {
                tbody.innerHTML += `
                    <tr>
                        <td>${item.type}</td>
                        <td>${item.buy}</td>
                        <td>${item.sell}</td>
                        <td>${item.currency}</td>
                    </tr>
                `;
            });

            document.getElementById('updated').innerText =
                'Cập nhật: ' + new Date().toLocaleTimeString();
        }

        fetchPrices();
        setInterval(fetchPrices, 10000);
    </script>
</body>
</html>
'''


@app.get('/', response_class=HTMLResponse)
def dashboard():
    return HTML


@app.get('/api/prices')
def prices():
    client = PNJClient()
    return client.fetch_prices()

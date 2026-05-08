import requests
from bs4 import BeautifulSoup
from datetime import datetime


class PNJClient:
    URL = 'https://www.pnj.com.vn/blog/gia-vang/'

    def fetch_prices(self):
        response = requests.get(self.URL, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []

        rows = soup.select('table tbody tr')

        for row in rows:
            cols = row.find_all('td')

            if len(cols) >= 3:
                data.append({
                    'provider': 'PNJ',
                    'type': cols[0].get_text(strip=True),
                    'buy': cols[1].get_text(strip=True),
                    'sell': cols[2].get_text(strip=True),
                    'currency': 'VND',
                    'updated_at': datetime.utcnow().isoformat()
                })

        return data


if __name__ == '__main__':
    client = PNJClient()

    for item in client.fetch_prices():
        print(item)

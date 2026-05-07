const axios = require('axios');
const cheerio = require('cheerio');

async function fetchPNJGoldPrice() {
    try {
        const response = await axios.get('https://www.pnj.com.vn/blog/gia-vang/');
        const $ = cheerio.load(response.data);

        const rows = $('table tbody tr');

        rows.each((index, row) => {
            const columns = $(row).find('td');

            const goldType = $(columns[0]).text().trim();
            const buyPrice = $(columns[1]).text().trim();
            const sellPrice = $(columns[2]).text().trim();

            console.log({
                brand: 'PNJ',
                gold_type: goldType,
                buy_price: buyPrice,
                sell_price: sellPrice,
                currency: 'VND'
            });
        });
    } catch (error) {
        console.error('Lỗi khi lấy giá vàng:', error.message);
    }
}

fetchPNJGoldPrice();

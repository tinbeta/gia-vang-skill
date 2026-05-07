use reqwest;
use scraper::{Html, Selector};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let body = reqwest::get("https://www.pnj.com.vn/blog/gia-vang/")
        .await?
        .text()
        .await?;

    let document = Html::parse_document(&body);
    let row_selector = Selector::parse("table tbody tr").unwrap();
    let cell_selector = Selector::parse("td").unwrap();

    for row in document.select(&row_selector) {
        let cells: Vec<_> = row.select(&cell_selector).collect();

        if cells.len() >= 3 {
            let gold_type = cells[0].text().collect::<String>().trim().to_string();
            let buy_price = cells[1].text().collect::<String>().trim().to_string();
            let sell_price = cells[2].text().collect::<String>().trim().to_string();

            println!(
                "PNJ | {} | Mua: {} | Bán: {} VND",
                gold_type,
                buy_price,
                sell_price
            );
        }
    }

    Ok(())
}

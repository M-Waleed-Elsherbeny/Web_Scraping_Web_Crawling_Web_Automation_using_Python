import requests
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from tqdm import tqdm
import concurrent.futures


BASE_URL = "https://www.amazon.eg/s?k=computers&language=en_AE&page=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
HEADERS = {
    "User-Agent": USER_AGENT,
    "accept-language": "en-US,en;q=0.5,"
}

def get_products_urls():
    response = requests.get(url=BASE_URL, headers=HEADERS)
    # sleep(5)
    soup = BeautifulSoup(response.content, "lxml")
    urls = soup.find_all('a', class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal", href=True)
    print(len(urls))
    for url in urls:
        url_links = url["href"] # type: ignore
        custom_urls = f"https://www.amazon.eg{url_links}"
        # print(url_links)
        with open("Amazon_Scraper/links.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([custom_urls])
    
def get_products_title(soup: BeautifulSoup) -> str:
    product_title = soup.find("span", attrs={"id": "productTitle"}).text.strip() # pyright: ignore[reportOptionalMemberAccess]
    return product_title

def get_products_price(soup: BeautifulSoup) -> float:
    product_price =  soup.find_all("span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")
    for span in product_price:
        main_price = span.text.strip().replace("EGP", "").replace(",", "")
        return float(main_price)
    return float()

def get_products_rating(soup: BeautifulSoup) -> float:
    try:
        rating = soup.find("span", id="acrPopover").text.strip().split(" ")[0] # type: ignore
        return float(rating)
    except:
        return 0.0

def get_products_details(soup: BeautifulSoup):
    details = {}
    table_section = soup.find("table", id="productDetails_techSpec_section_1")
    table_rows = table_section.find_all("tr") # type: ignore
    for rows in table_rows:
        table_header = rows.find("th").text.strip() # type: ignore
        table_details = rows.find("td").text.strip().replace("\u200e", "") # type: ignore
        details[table_header] = table_details
    return details

def get_products_info(url, output):
    products_details = {}
    print(f"Scraping Url : {url}\n\n")
    response = requests.get(url=url, headers=HEADERS)
    # sleep(3)
    soup = BeautifulSoup(response.content, "lxml")
    products_details["title"] = get_products_title(soup)
    products_details["price"] = get_products_price(soup)
    products_details["rating"] = get_products_rating(soup)
    products_details.update(get_products_details(soup))
    output.append(products_details)

if __name__ == "__main__":
    # get_products_urls()
    products_data = []
    urls = []
    with open("Amazon_Scraper/links.csv", "r", newline="", encoding="utf-8") as file:
        urls = list(csv.reader(file))
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
        for url in tqdm(range(0, len(urls))):
            executer.submit(get_products_info, urls[url][0], products_data)
    output_date = datetime.today().strftime("%d-%m-%Y")
    output_file = f"Amazon_Scraper/Output/output-{output_date}.csv"
    with open(output_file, mode="w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(products_data[0].keys())
        for product in products_data:
            writer.writerow(product.values())
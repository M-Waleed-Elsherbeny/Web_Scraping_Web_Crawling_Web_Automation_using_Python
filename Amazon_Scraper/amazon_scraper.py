import requests
from time import sleep
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.amazon.eg/s?k=computers&language=en_AE&page=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
HEADERS = {
    "User-Agent": USER_AGENT,
    "accept-language": "en-US,en;q=0.5,"
}

def get_products_urls():
    response = requests.get(url=BASE_URL, headers=HEADERS)
    sleep(5)
    soup = BeautifulSoup(response.content, "lxml")
    urls = soup.find_all("div", class_="sg-col-4-of-4 sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-8 sg-col-4-of-20")
    print(len(urls))
    for url in urls:
        url_links = url.find("a")['href']
        custom_urls = f"https://www.amazon.eg{url_links}"
        # print(url_links)
        with open("Amazon_Scraper/links.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([custom_urls])
    

def get_products_details(url):
    products_details = {}
    # get_products_urls()
    print(f"Scraping Url: {url}")
    response = requests.get(url=url, headers=HEADERS)
    sleep(3)
    soup = BeautifulSoup(response.content, "lxml")
    # products_details["title"] = soup.find("h1", id="title").get_text().strip()
    price =  soup.find("div", class_="a-section a-spacing-none aok-align-center aok-relative")
    main_price = price.find("span", class_="a-price-whole").get_text().strip().replace(",", "")
    price_decimal = price.find("span", class_="a-price-fraction").get_text().strip()
    products_details["price"] = float(main_price + price_decimal)
    print(products_details)

if __name__ == "__main__":
    with open("Amazon_Scraper/links.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            url = row[0]
            get_products_details(url)
    
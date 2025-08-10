import requests
from time import sleep
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.amazon.eg/s?k=computers&language=en_AE&page=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
HEADERS = {
    "User-Agent": USER_AGENT,
    "accept-language": "en-US,en;q=0.9,ar;q=0.8"
}

def get_products_urls():
    response = requests.get(url=BASE_URL, headers=HEADERS)
    sleep(5)
    soup = BeautifulSoup(response.content, "lxml")
    urls = soup.find_all("div", class_="a-section a-spacing-base")
    # for url in urls:
    #     url_links = url.find("a")
    print(urls)
    

if __name__ == "__main__":
    get_products_urls()
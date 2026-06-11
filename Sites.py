import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books[:5]:
    title = book.find("h3").find("a")["title"]
    print(title)
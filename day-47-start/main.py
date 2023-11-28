import requests
import lxml
from bs4 import BeautifulSoup


url = "https://www.amazon.com/COSORI-Electric-Sterilizer-Dishwasher-Stainless/dp/B0BFX95J5P"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = float(soup.find(class_="a-price-whole").getText())
currency = soup.find(class_="a-price-symbol").getText()
print(price)
print(currency)
# <span class="a-offscreen">$97.93</span>
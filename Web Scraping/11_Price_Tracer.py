import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
        self.response=requests.get(url=self.url,headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response ,"lxml")

    def product_title(self):
        title=self.soup.find("span" , {"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price_whole = self.soup.find("span", {"class": "a-price-whole"})
        price_fraction = self.soup.find("span", {"class": "a-price-fraction"})
        if price_whole is not None:
            price = price_whole.text.strip()
            if price_fraction is not None:
                price += price_fraction.text.strip()
            return price
        else:
            return "Tag not found"

device=PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Black-128GB-Storage/dp/B07KXCH2FP?th=1")
print(device.product_title())
print(device.product_price())
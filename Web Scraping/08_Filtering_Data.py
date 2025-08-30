import requests
from bs4 import BeautifulSoup

def Extract(url):
    response=requests.get(url=url)
    soup=BeautifulSoup(response.text,'lxml')
    tag=soup.find('div',{"id":"main-content"})
    h=tag.find("h2").find("a")
    print(h)
    g = tag.find_all("h2")
    print(g)
    content=[p.text for p in h]
    print(content)

Extract(url="https://www.django-rest-framework.org/")

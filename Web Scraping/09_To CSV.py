import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    response=requests.get(url=url)
    soup=BeautifulSoup(response.text,'lxml')
    tag=soup.find('div',{"id":"main-content"})
    h=tag.find("h2").find("a")
    print(h)
    g = tag.find_all("h2")
    print(g)
    content=[a.text for a in h]
    print(content)

    with open("wiki.csv","w") as csv_file:
        csv_write=csv.writer(csv_file)
        csv_write.writerow(content)

Extract(url="https://www.django-rest-framework.org/")
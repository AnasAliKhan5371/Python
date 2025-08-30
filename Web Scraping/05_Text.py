import requests
url="https://www.django-rest-framework.org"

response=requests.get(url=url)

print(type(response.text)) #return all data in form of string

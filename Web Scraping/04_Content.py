import requests
url="https://www.django-rest-framework.org/img/logo.png"

user={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
response=requests.get(url=url,headers=user)

pic=response.content  # content - return in form of bytes
f=open("logo.png","wb")
f.write(pic)

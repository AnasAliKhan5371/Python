import urllib.request,urllib.parse, urllib.error

url=urllib.request.urlopen("https://www.django-rest-framework.org/")
for line in url:
    print(line.decode().strip())
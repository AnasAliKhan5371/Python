import requests
url="https://www.django-rest-framework.org/"
response=requests.get(url=url)
print(dir(response))
print(response.status_code)
print(response.headers)
print(response.request.headers)


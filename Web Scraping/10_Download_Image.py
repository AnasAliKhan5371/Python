
import requests
import re
import os

user = input("Enter image name: ")
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

url = f"https://www.google.com/search?q={user}&tbm=isch"


response_text = requests.get(url=url, headers=user_agent).text


pattern = r'"(https?://[^"]+?\.(?:jpg|jpeg|png|gif))"'

image_urls = re.findall(pattern, response_text)
print(f"Total Images Found: {len(image_urls)}")

no_of_images = int(input("No. of images to be downloaded: "))

if image_urls:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)
    for i, image_url in enumerate(image_urls[:no_of_images]):
        image_response = requests.get(image_url)
        image_name = image_url.split('/')[-1]

        with open(image_name, "wb") as file:
            file.write(image_response.content)








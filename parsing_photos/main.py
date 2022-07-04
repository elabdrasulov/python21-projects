import requests

url = 'https://www.rosphoto.com/images/u/articles/1510/10_3.jpg'

res = requests.get(url)
print(res.text)
name = 'photos/photo1.jpg'

with open(name, "wb") as file:
    file.write(res.content)
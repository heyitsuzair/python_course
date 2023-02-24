import requests
# url = 'https://jsonplaceholder.typicode.com/posts'
from bs4 import BeautifulSoup

# response = requests.get('https://google.com')
# print(response.text)

# data = {
#     "userId": "12",
#     "title": "hello2",
#     "body": "fmpfefefpmep2"
# }

# response = requests.post(
#    url , json=data)
# print(response.text)


response = requests.get('https://google.com')
soup = BeautifulSoup(response.text, 'html.parser')

for img in soup.find_all('img'):
    print(img['src'])

import requests

response = requests.get('http://geekbrains.ru/')

print(response)
print(response.content.decode('utf-8'))

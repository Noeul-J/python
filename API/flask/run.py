import requests

# req = requests.get('http://127.0.0.1:8000/hello?name=Alice')
#
# print(req.text)

# req = requests.get('http://127.0.0.1:8000/get_csv')
req = requests.get('http://localhost:8000/get_csv')

print(req.text)

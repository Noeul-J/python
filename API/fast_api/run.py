import requests

# req = requests.get('http://127.0.0.1:8000/random_number')
#
# print(req.text)

# req = requests.get('http://127.0.0.1:8000/hello')
#
# print(req.text)

req = requests.get('http://127.0.0.1:8000/get_csv')

print(req.text)
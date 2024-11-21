import requests


endpoint = "http://localhost:8000/api/products/154345234"
get_response = requests.get(endpoint)


print(get_response.json())
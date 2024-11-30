import requests


endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint,json={"title":"meowasdaawawe","price":99 })


print(get_response.json())

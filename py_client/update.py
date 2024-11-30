import requests


endpoint = "http://localhost:8000/api/products/18/update/"

data = {

    "title":"what is that supposed to mean",
    "price": 99.8
}



get_response = requests.put(endpoint,json=data)


print(get_response.json())
import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {

    "title":"saturday nights alright for fighting",
    "price": 99.8
}



get_response = requests.put(endpoint,json=data)


print(get_response.json())
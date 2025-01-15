import requests

headers = {"Authorization": "Bearer d9987037d3c2b43ecfa542dc333439022c52954f"}
endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(
    endpoint,
    json={
        "title": "meowasdasdasdaawawe",
        "price": 99,
        "email": "stalin@gmail.com",
        "gopnik": "car",
    },
    headers=headers,
)


print(get_response.json())

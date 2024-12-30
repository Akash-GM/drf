import requests

headers = {"Authorization": "Bearer 12a41750b70cb6388bfcdb644ca846e067ef860c"}
endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(
    endpoint, json={"title": "meowasdaawawe", "price": 99}, headers=headers
)


print(get_response.json())

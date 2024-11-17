import requests
import winsound
import time

endpoint = "http://localhost:8000/api/"



get_response = requests.get(endpoint)


a= get_response.json()

print(a['message'])





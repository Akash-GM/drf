import requests


endpoint = "http://localhost:8000/api/"



get_response = requests.post(endpoint,json={"title":"asdas","pricdrtge":"abasd"})





print(get_response.json())


 
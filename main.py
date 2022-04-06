import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "token"
GRAPH_ID = "code100"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "100 days of code",
    "unit": "minutos",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_enpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

date = today.strftime("%Y%m%d")

pixels_params = {
    "date": date,
    "quantity": input("¿Cuántos minutos programaste el día de hoy? "),
    "optionalData": input("¿Qué día del 100 days of code hiciste hoy? "),
}

response = requests.post(url=pixela_pixel, json=pixels_params, headers=headers)
print(response.text)

pixela_put = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

put_params = {
    "quantity": "40",
    "optionalData": None,
}

# response = requests.put(url=pixela_put, json=put_params, headers=headers)
# print(response.text)

delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def obtener_albumes():
    response = requests.get(f"{BASE_URL}/albums")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error al obtener álbumes")

def obtener_fotos():
    response = requests.get(f"{BASE_URL}/photos")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error al obtener fotos")
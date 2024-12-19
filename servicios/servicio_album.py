import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Método para obtener álbumes desde la API
def obtener_albumes():
    try:
        response = requests.get(f"{BASE_URL}/albums")
        response.raise_for_status()  # Lanza una excepción si el status no es 200
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error al obtener álbumes: {e}")

# Método para obtener fotos desde la API
def obtener_fotos():
    try:
        response = requests.get(f"{BASE_URL}/photos")
        response.raise_for_status()  # Lanza una excepción si el status no es 200
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error al obtener fotos: {e}")

# Método para crear un álbum en la API
def crear_album(album_data):
    try:
        response = requests.post(f"{BASE_URL}/albums", json=album_data)
        response.raise_for_status()  # Lanza una excepción si el status no es 201
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception("Error al crear álbum: Respuesta inesperada")
    except requests.RequestException as e:
        raise Exception(f"Error al crear álbum: {e}")

# Método para actualizar un álbum en la API
def actualizar_album(album_id, album_data):
    try:
        response = requests.put(f"{BASE_URL}/albums/{album_id}", json=album_data)
        response.raise_for_status()  # Lanza una excepción si el status no es 200
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al actualizar álbum: Respuesta inesperada")
    except requests.RequestException as e:
        raise Exception(f"Error al actualizar álbum: {e}")

# Método para borrar un álbum en la API
def borrar_album(album_id):
    try:
        response = requests.delete(f"{BASE_URL}/albums/{album_id}")
        response.raise_for_status()  # Lanza una excepción si el status no es 200
        if response.status_code == 200:
            return {"mensaje": "Álbum borrado con éxito"}
        else:
            raise Exception("Error al borrar álbum: Respuesta inesperada")
    except requests.RequestException as e:
        raise Exception(f"Error al borrar álbum: {e}")
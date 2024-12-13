import requests

def buscar_con_serper(termino_busqueda):
    """
    Realiza una búsqueda en Google usando la API de Serper.

    :param termino_busqueda: String con el término que el usuario quiere buscar.
    :return: Lista de resultados relevantes.
    """
    # Sustituya "SU_API_KEY" por la clave de API de Serper
    API_KEY = "6c990d9638d2c48fb79f430b6bceceb0c286030c"
    URL = "https://google.serper.dev/search"

    # Datos de la solicitud
    headers = {"X-API-KEY": API_KEY}
    payload = {"q": termino_busqueda}

    try:
        # Solicitud POST
        response = requests.post(URL, headers=headers, json=payload)
        response.raise_for_status()  # Lanza un error si el código de estado no es 200
        data = response.json()

        # Extrae los títulos de los resultados
        resultados = [item["title"] for item in data.get("organic", [])]
        return resultados if resultados else ["No se encontraron resultados."]
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la búsqueda: {e}")
        return ["Error al realizar la búsqueda."]
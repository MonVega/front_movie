import requests
from typing import Optional

def get_movie_prediction(title: str, description: str) -> Optional[float]:
   
    url = "https://monse14-api-movie.hf.space/predict"  

    # Form data
    data = {
        "col1": title,
        "col2": description
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  
        result = response.json()
        return float(result["prediction"])
    except requests.RequestException as e:
        print("Error al consumir la API:", e)
        return None
    except KeyError:
        print("Respuesta inesperada:", response.text)
        return None


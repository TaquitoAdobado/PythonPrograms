# En este script se muestra como consumir APIs externas con Flask usando la libreria requests.
# Para eso primero debemos isntalarla con: pip install requests
# No confundamos request de Flask con requests (plural).
# Para consumir una API externa debemos hacer una solicitud HTTP a la API.
# Siempre buscar APIs que tengan documentacion clara para entenderlas.
# Puede que algunas APIs requieran una API Key para acceder a los datos e incluirla en la solicitud.
# NUNCA exponer la API Key en tu codigo, siempre usar variables de entorno. Guardalas en tu archivo .env
# En este script usaremos una API key de OpenWeatherMap.com (es gratuita y de uso personal).

from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

# Creamos el servidor de Flask como de costumbre
app = Flask(__name__)

# Cargamos las variables de entorno
load_dotenv()

# Llamamos a la API key
WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_MAP_KEY')


# Definimos el endpoint de la API que consumira la api externa
@app.route('/api/weather/<city>', methods=['GET'])
def get_weather(city):
    """ Este endpoint nos devolvera el clima de una ciudad.

    Primero se usa la API Geocoding para obtener la latitud y longitud de la ciudad.
    Luego se usa la API de clima con las coordenadas obtenidas para obtener el clima.
    Los endpoints de ambas APIs asi como su personalizacion se encuentran en su documentacion respectiva.

    DOCUMENTACION:
        API de clima:
        https://openweathermap.org/api/current?collection=current_forecast#data

        Geocoding API:
        https://openweathermap.org/api/geocoding-api?collection=other
    """
    
    # ENDPOINT de la API Geocoding para la ciudad escrita en nuestro url.
    city_data_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},MX&limit=1&appid={WEATHER_API_KEY}"

    # Usamos request para consumir las APIs
    try:

        # --------- Geocoding API ---------

        # Obtenemos la respuesta HTTP de la API Geocoding
        response_geocoding = requests.get(city_data_url)
        response_geocoding.raise_for_status() # Si la solicitud no fue exitosa, lanza una excepcion.
        
        # Obtenemos los datos de la ciudad
        city_data = response_geocoding.json()

        # Validamos los datos (En este caso que no sean nulos)
        if not city_data:
            return jsonify({"error": "Ciudad no encontrada"}), 404

        # Extraemos la latitud y longitud de la ciudad
        # Usamos [0] porque la API nos devuelve una lista con la informacion de la ciudad
        lat, lon = city_data[0]["lat"], city_data[0]["lon"]

        # --------- Clima API ---------

        # ENDPOINT de la API de clima.
        city_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric&lang=es"

        # Obtenemos la respuesta HTTP de la API de clima
        response_weather = requests.get(city_weather_url)
        response_weather.raise_for_status()  # Si la solicitud no fue exitosa, lanza una excepcion.

        # Obtenemos los datos del clima de la ciudad
        city_weather = response_weather.json()

        # Validamos los datos (En este caso que no sean nulos)
        if not city_weather:
            return jsonify({"error": "Ciudad no encontrada"}), 404
        
        # En este punto podemos usar POSTMAN para ver los datos del clima que nos devolvio la API
        # De esta forma podemos seleccionar los datos que queramos y devolverlos donde queramos.

        # Datos seleccionados de la API de clima.
        city_name = city_weather.get("name")
        country = city_weather.get("sys", {}).get("country", "N/A")
        sky_state = city_weather.get("weather", [{}])[0].get("description", "N/A")
        temp = city_weather.get("main", {}).get("temp", "N/A")
        max_temp = city_weather.get("main", {}).get("temp_max", "N/A")
        min_temp = city_weather.get("main", {}).get("temp_min", "N/A")
        sensation_temp = city_weather.get("main", {}).get("feels_like", "N/A")
        pressure = city_weather.get("main", {}).get("pressure", "N/A")
        humidity = city_weather.get("main", {}).get("humidity", "N/A")

        # Creamos un diccionario con los datos seleccionados.
        city_weather_dict = {
            "location": {"city": city_name, "country": country},
            "weather": {"sky_state": sky_state, "temp": f"{temp} °C"},
            "details": {
                "max_temp": f"{max_temp} °C",
                "min_temp": f"{min_temp} °C",
                "termical_sensation": f"{sensation_temp} °C",
                "pressure": f"{pressure} hPa",
                "humidity": f"{humidity} %"}
        }

        # Retornamos los datos del clima de la ciudad
        return jsonify(city_weather_dict), 200
    
    # Capturamos las excepciones
    except requests.exceptions.HTTPError as err:    # Capturamos la excepcion de .raise_for_status
        status_code = err.response.status_code      # Obtenemos el codigo de estado
        # Retornamos el error con el codigo de estado y la url de la api que nos dio el error
        return jsonify({
            "error": str(err),
            "url": err.response.url,
            "status_code": status_code
            }), status_code    # Retornamos el codigo de estado en la respuesta HTTP
    except requests.exceptions.RequestException as err: # Captura cualquier otro error de la libreria requests
        # Retornamos el error
        return jsonify({"error": str(err)}), 500

    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")

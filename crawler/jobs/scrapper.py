from crawler.components.payloads import headers
from crawler.components.constants import BASE_URL, APPID
from datetime import datetime
import requests

class Scrapper:
    
    def __init__(self, city: str):
        self.__city = city
        self.params = {
            "appid": APPID,
            "units": "metric"
        }

    def get_info_city(self):
        self.params['q'] = self.__city
        response = requests.get(
            url= f'{BASE_URL}/find',
            params= self.params,
            headers= headers
        )
        return response.json()
    

    def get_weather_metrics(self):
        city_info = self.get_info_city()
        latitude, longitude = city_info['list'][0]['coord']['lat'], city_info['list'][0]['coord']['lon']
        self.params['lat'] = latitude
        self.params['lon'] = longitude
        response_api = requests.get(
            url = f'{BASE_URL}/onecall',
            params= self.params,
            headers= headers
        ).json()
        convert_timestamp = lambda timestamp: datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y")

        response = {
            "data": convert_timestamp(response_api['current']['dt']),
            "cidade": {
                "nome": self.__city,
                "latitude": latitude,
                "longitude": longitude
            }, 
            "metricas":{
                "temperatura": round(response_api['current']['temp']),
                "sensacao": round(response_api['current']['feels_like']),
                "humidade": response_api['current']['humidity'],
                "velocidade_vento": response_api['current']['wind_speed'],
                "visibilidade": f"{float(response_api['current']['visibility'] / 1000 )} Km",
                },
            }
        return response
    
    def run(self):
        return self.get_weather_metrics()

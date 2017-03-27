from .locations import LOCATIONS
import requests

SITE_URL = 'http://taps-aff.co.uk'

def GetWeatherData(location):
    if not location:
        return None

    url = SITE_URL+'/?api&location=' + location
    response = requests.get(url)
    return response.json()


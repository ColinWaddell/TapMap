import requests

API_URL = 'http://django.taps-aff.co.uk/api'

def GetWeatherData(location):
    if not location:
        return None

    url = '%s/%s' % (API_URL, location)
    weather_json = {}

    try:
        response = requests.get(url)
        weather_json = response.json()
    except requests.exceptions.ConnectionError:
        print ("Error retrieving data from " + url)

    return weather_json

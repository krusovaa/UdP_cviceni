import requests

API_KEY = "a377d32d67992b29cf7579755aa03c4c"
API_ADDR = "http://api.openweathermap.org/data/2.5/forecast"

params = {
    "q": "Praha",
    "APIKEY": API_KEY,
    "units": "metric"
}

res = requests.get(API_ADDR, params=params)
data = res.json()
print(type(data))

forecast = []
predpoved = data['list']
for p in predpoved:
    a = ['main']['temp']
    b = ['wind']['speed']
    c = ['dt_txt']
    forecast.append(a, b, c)
    print()
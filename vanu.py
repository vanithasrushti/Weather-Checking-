import requests
city_name="mysore"
API_key="d9b8d6b11a09a0d7cd564d46a6eb36e5"
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print('weather is',data['weather'][0]['description'])
    print('Current Temperature is ',data['main']['temp'])
    print('Current Temperature Feels like is',data['main']['feels_like'])
    print('Humidity is',data['main']['humidity'])

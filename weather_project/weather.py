import requests

api_key ="ce85fe5f2d183c7249b473b6a76b99f0"
base_url= "http://api.openweathermap.org/data/2.5/weather"

city=input("Enter a city name: ")
request_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

if response.status_code==200:
    data = response.json()
    weather=data['weather'][0]['main']
    temp=round(data['main']['temp']-273.15, 2)  #round(some  int claculation,2) rounds it to 2 decimals
    print("Weather: ",weather.upper())
    print("Temperature: ",temp,"°C")

else:
    print('error occured')
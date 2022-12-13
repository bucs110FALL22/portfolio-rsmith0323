import requests
from WeatherAPI import WeatherAPI


def main():
  '''prints weather data for the city inputed'''
  
  city = input("Enter a city: ")
  api_key = '49e959aa36dc4eec78008ec6b7e9c6bf'

  weather_data = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  
  temp = requests.get(weather_data)
  response = temp.json()['main']
  print(response)
    


main()
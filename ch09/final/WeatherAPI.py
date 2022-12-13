import requests

class WeatherAPI:
  
  def __init(self, city, api_key):
    api_key = '49e959aa36dc4eec78008ec6b7e9c6bf'

    self.url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  

  def get(self):
    temp = requests.get(self.url)
    print(temp)
    response = temp.json()['main']
    
    return(response)





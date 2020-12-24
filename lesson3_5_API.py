import requests

city = input('Узнать погоду в городе: ')
key = 'b8cce234bfbd89d888db71802043d2b2'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'q': city, 'appid': key, 'lang': 'ru', 'units': 'metric'}
file = requests.get(url, params)
# h = file.headers  # словарь, содержит тип содержимого, дату запроса, статус сервера и т.д.
# print(h['Content-Type'])
data = file.json()
temp = data['main']['temp']
string = 'Температура в городе {} - {} градусов'
print(string.format(city, temp))

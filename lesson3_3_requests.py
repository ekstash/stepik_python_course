import requests

res = requests.get('https://docs.python.org/3.9/_static/py.png')
print(res.status_code)  # статус ответа res
print(res.headers['Content-Type'])  # тип содержимого res

html = res.content  # бинарное содержимое
# print(res.text)  # если содержимое - текстовый файл

with open('py.png', 'wb') as png:  # картинкку тоже можно сохранить в файл
    png.write(html)

res = requests.get('https://yandex.ru/search/',  # равнозначно поиску в яндексе
                   params={
                       'text': 'Stepic',
                       'test': 'test1',
                       'name': 'Name With Spaces',
                       'list': ['test1', 'test2']
                   })

print(res.url)  # как выглядит запрос в поисковике

import requests
from random import random


def strings():
    print('abcd'.startswith(('ab', 'bc', 'de')))  # можно передать целый кортеж, если хоть одно верно - True
    s = 'image.png'
    print(s.endswith("png"))
    s = 'abcabc'
    s.find('abc')  # вернет 0
    s.rfind('abc')  # вернет 3, поиск ведется с конца

    tmp = '{1}я строка{0}'  # место для вставки, причем сначала мы используем 1 аргумент, потом 0
    print(tmp.format(')', '1'))
    tmp = '{num}я строка{sym}'  # можно обозначить параметры
    print(tmp.format(sym=')', num='1'))

    res = requests.get('https://vk.com')
    tmp = 'Обращение к странице {0.url} с кодом {0.status_code}'  # можем обращаться и к аргументам
    print(tmp.format(res))

    x = random()
    print(x)
    print('{:.3}'.format(x))  # округление до 3 знаков после запятой


strings()

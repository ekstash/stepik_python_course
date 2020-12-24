import requests


def check(number):
    url_num = url + number + '/math'
    file = requests.get(url_num, 'json')
    data = file.json()
    if data['found'] == True:
        return 'Interesting'
    return 'Boring'


url = 'http://numbersapi.com/'

with open('input.txt') as inp:
    with open('output.txt', 'w') as out:
        for line in inp:
            out.write(check(line.strip())+'\n')

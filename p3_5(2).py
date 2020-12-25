import requests
import json


def get_art(artist):
    pass


client_id = '75683d07db118d3210ad'
client_secret = 'b9ee4cdeb39020061c7db9d190e62e5b'

url = 'https://api.artsy.net/api/artists'

params = {'client_id': client_id, 'client_secret': client_secret}
r = requests.post('https://api.artsy.net/api/tokens/xapp_token', data=params)
j = json.loads(r.text)
token = j['token']

headers = {"X-Xapp-Token": token}
art_list = dict()

with open('input.txt') as inp:
    for line in inp:
        line = line.strip()
        r = requests.get("https://api.artsy.net/api/artists/" + line, headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)
        art_list[line] = [j['sortable_name'], j['birthday']]

art_list = sorted(art_list.values(), key=lambda x: (x[1], x[0]))

with open('output.txt', 'w') as w:
    for s in art_list:
        w.write(s[0]+'\n')

import requests
import re

A = ''

with open('input.txt') as f:
    A = f.read()

pattern = r'<a.*href="(.*?)"'  # нежадность
urls1 = re.findall(pattern, A)
urls = []
for u in urls1:
    u = str(u)
    if not u.startswith('..'):
        start = u.find('//')
        if start != -1:
            u = u[start + 2:]
        fin1 = u.find('/')
        if fin1 != -1:
            u = u[:fin1]
        fin2 = u.find(':')
        if fin2 != -1:
            u = u[:fin2]
        if u not in urls:
            urls.append(u)

urls = sorted(urls)
for u in urls:
    print(u)

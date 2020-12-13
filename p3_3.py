import requests
import re


def run(pattern, x):
    res = requests.get(x).text
    urls = re.findall(pattern, res)
    return urls

def p_1():
    A = input()
    B = input()

    # with open('input.txt') as f:
    #     A = f.readline().strip()
    #     B = f.readline().strip()

    pattern = r'<a.*href="(.*)"'
    urls1 = run(pattern, A)

    urls2 = []
    for url in urls1:
        urls2 += run(url)

    if B in urls2:
        print('Yes')
    else:
        print('No')
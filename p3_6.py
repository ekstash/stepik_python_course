from xml.etree import ElementTree as Et

s = input()
root = Et.fromstring(s)

colors = {'red': 0, 'green': 0, 'blue': 0}


def func(elem, val):
    attr = elem.attrib
    colors[attr['color']] += val
    for child in elem:
        func(child, val + 1)


func(root, 1)

for val in colors.values():
    print(val, end = ' ')

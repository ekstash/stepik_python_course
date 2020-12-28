# структура файла xml - <tag> data </tag>. Списки описываются структурой
# <tag>
#   <tag2> data </tag2>
# </tag>
# теги могут имет атрибуты: <tag atr="1">
# в корне - всегда один тег

from xml.etree import ElementTree as Et
from lxml import etree
import requests

tree = Et.parse('example.xml')  # возвращает дерево, объект типа ElementTree
root = tree.getroot()  # тип Element, имеет параметры тег, атрибут, текст и tail (?)


def read_xml():
    s = "<tag> text </tag>"
    s_tree = Et.fromstring(s)  # то же самое,  что и parse, но из строки

    for child in root:  # можем перебрать элементы из списка
        print(child.tag, child.attrib)
    print(root[0][0].text)  # так тоже можно

    for el in root.iter("scores"):  # по всем элементам тега "scores"
        score_sum = 0
        for childs in el:
            score_sum += float(childs.text)
        print(score_sum)


def change_xml():
    greg = root[0]
    mod1 = next(greg.iter("module1"))
    print(mod1, mod1.text)
    mod1.text = str(float(mod1.text) + 30)  # присвоили полю новое значение
    print(mod1, mod1.text)

    cert = greg[2]
    cert.set('type', 'great!')  # установили атрибут type со значением great!

    description = Et.Element('description')  # ('tag')
    description.text = 'This is just description'
    greg.append(description)

    greg.remove(greg.find('description'))  # нашли и удалили первый элемент с данным тегом

    tree.write('ex_copy.xml')


def new_xml():
    root = Et.Element('student')
    name = Et.SubElement(root, 'name')  # (родитель, тег)
    name.text = 'Greg'
    tree = Et.ElementTree(root)  # создали дерево
    tree.write('new_tree.xml')  # записали дерево


def lxml_format():
    res = requests.get('https://docs.python.org/3/')
    parser = etree.HTMLParser()  # аналог ElementTree.parse() для криво сформированных html страниц
    root = etree.fromstring(res.text, parser)
    for el in root.iter('a'):
        print(el, el.attrib)

read_xml()
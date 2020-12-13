# открытие файлов
# 'r' - для чтения, 'r+' - для чтения и записи
# 'w' - для записи, содержимое стирается, 'w+' - для чтения и записи, аналогично
# 'a' - для записи в конец файла
# 'b' - бинарное открытие
# 't' - текстовый режим
# при этом можно указывать два флажка сразу, например, 'rb'

import os
import shutil


def read_files():
    f = open("input.txt")
    f.read(6)  # читает 6 первых символов
    x = f.read()  # читает с того места, где остановились в прошлый раз, и до конца
    x = x.splitlines()  # разбивает текст построчно
    x = f.readline().rstrip()  # убирает символы типа '/n' и прочие пробельные (справа от строки)
    print(repr(x))  # переводит текст в строку
    for line in f:
        print(line.strip())  # по всей строке, lstrip - слева от строки
    f.close()


def write_file():
    f = open("output.txt", 'w')
    lines = ['l1', 'l2', 'l3']
    contents = '\n'.join(lines)  # создает из списка строку с указанным разделителем между элементами
    f.write(contents)
    f.close()


# with open используется, чтобы избежать незакрытия файла в случае возникновения ошибки

os.listdir()  # список файлов в текущей папке
os.getcwd()  # узнать текущий путь
os.path.exists()  # узнает о существовании файла или папки
os.path.isfile()  # является ли объект файлом
os.path.isdir()  # является ли объект папкой
os.path.abspath()  # выдаст полный путь файла
os.chdir()  # сменить директорию
os.walk()  # генератор, возвращает кортеж из текущей директории, списка всех директорий, списка всех файлов
# то же самое для всех вложенных папок
shutil.copy("output.txt", "input.txt")  # копирование, при отсутствии файла создает его
shutil.copytree()  # то же самое, копирует папку целиком

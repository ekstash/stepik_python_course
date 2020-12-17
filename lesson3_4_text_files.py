import csv
import json


# csv -  формат файла, в котором все значения разделены запятыми (по умолчанию), без пробелов
# подходит для хранениия табличных данных

# можно использовать запятую или символ переноса строки внутри значения,
# тогда значение берется в кавычки (по умолчанию).
# Главное, чтобы перед кавычками не оказалось, например, пробела

def read_csv():
    with open('input.csv') as file:
        reader = csv.reader(file)  # итерируемый класс, возвращает списки по строкам
        for row in reader:
            print(row)

    # в качестве разделителя можно использовать не только запятую, но и знак табуляции
    # тогда формат станет tsv, a при чтении библиотекой csv указываем параметр delimiter="\t"

    with open('input.tsv') as file:
        read = csv.reader(file, delimiter="\t")
        for row in read:
            print(row)


def write_csv():
    # newline необходим, чтобы избежать печати пустой строки (нужно только в винде)
    with open('output.csv', 'w', newline='') as f:
        list = [
            ['name', 'last', 'age', 'weight'], ['Roman', 'Antipov', '17', '65,4']
        ]
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # заключить все значения в кавычки

        # можно записывать построчно:
        for row in list:
            writer.writerow(row)

        # а можно целиком:
        writer.writerows(list)


# json - что-то типа словаря. Но в качестве ключа могут выступать только строки,
# булевы значения всегда пишутся с маленькой буквы


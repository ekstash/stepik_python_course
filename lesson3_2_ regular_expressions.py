import re


def regular_base():
    s = "Hello\"world"
    print(s)
    s = r"Hello\"world"  # r - все символы внутри строки читаются естественным образом
    print(s)


def re_module():
    pattern = r'abc'
    string = 'habcdabc'
    match_obj = re.match(pattern, string)  # Проверяет, подходит ли string под шаблон pattern
    # имеет атрибуты span(x,y) - позиции вхождения строки (y не включено) и match - искомую подстроку
    # возвращается объект либо None,
    # если такой строки нет или начало строки не совпадает с началом шаблона
    print(match_obj)

    search_obj = re.search(pattern, string)
    # подобна match, но найдет искомый шаблон не только в начале строки
    print(search_obj)

    pattern = r'a[abc]c'  # под шаблон будут подходить строки, у которых на 1й позиции символы a,b или c
    string = 'accd'
    print(re.match(pattern, string))

    string = 'abc, acc, aacc, aac'
    print(re.findall(pattern, string))  # выдаст список подходящих под шаблон подстрок,
    # не найдет пересекающиеся, будет повторяться
    # если в регулярке одна группа, вернет список подстрок, подходящих ТОЛЬКО ПОД ЭТУ ГРУППУ

    print(re.sub(pattern, 'abc', string, ))  # заменит все подстроки, подходящие под шаблон, строкой abc


def re_and_metacharacters():
    pattern = r'english?'  # знак вопроса игнорируется, т.к является метасимволом
    string = 'do you speak english?'
    print(re.search(pattern, string))  # подстрокой будет являться только 'english'

    pattern = r'english\?'  # экранируем знак вопроса
    print(re.search(pattern, string))

    # . ^ $ * + ? { } [ ] \ | ( ) - - метасимволы

    # - - диапазон:

    pattern = r'a[a-zA-z]c'  # на первой позиции - любые буквы латинского алфавита
    string = 'abc, aKc, a_c, a.c'
    print(re.findall(pattern, string))

    # ^ - отрицание:
    pattern = r'a[^a-z]c'  # на первой позиции не должно быть строчных латинских букв
    print(re.findall(pattern, string))

    # некоторые обозначения:
    # \d - [0-9]
    # \D - [^0-9]
    # \s - [ \t\n\r\f\v] - пробельные
    # \S - [^ \t\n\r\f\v]
    # \w - [a-zA-Z0-9_] - буквы, цифры и _
    # \W - [^a-zA-Z0-9_]
    # \b - начало слова
    # \B - не начало слова

    pattern = r'a\wc'  # на первой позиции любая буква, цифра или _
    print(re.findall(pattern, string))

    # . - любой символ, кроме переноса строки

    # * - любое количество этого символа, включая ноль
    pattern = r'ab*c'
    string = 'ac, abc, abbc'
    print(re.findall(pattern, string))

    # + - то же самое, но без нуля

    # - 0 или 1 вхождение

    # {x} - ровно x вхождений, {x,y} - диапазон от x до y вхождений
    pattern = r'ab{1,3}c'
    string = 'ac, abc, abbc'
    print(re.findall(pattern, string))

    # комбинирование []+
    pattern = r'a[ab]+a'
    string = 'abaaba'
    print(re.findall(pattern, string))
    # вернет максимальную подходящую подстроку - вследствие "жадности" []+

    # для нежадности можно поставить "?" после метасимвола "+"
    # однако этот алгоритм найдет лишь минимальные, причем непересекающиеся, подстроки
    pattern = r'a[abc]+?a'
    string = 'abaaaaca'
    print(re.findall(pattern, string))


def re_groups():

    # (строка) - группировка по строкам
    # | - выбор из двух групп символов:
    pattern = r'((test|text)*|(abc))'
    string = 'testtextabc'
    match = re.match(pattern, string)
    print(match)  # testtext
    print(match.groups())  # ('testtext', 'text', None)
    # показывается, что в найденной подстроке принадлежит какой группировке, по порядку скобок.
    print(match.group(0))  # testtext - все рег.выражение, даже если оно все в скобках, по умолчанию
    print(match.group(1))  # testtext - далее, как в groups(), по порядку
    print(match.group(2))  # text
    print(re.findall(pattern, string))
    # [('testtext', 'text', ''), ('', '', ''), ('abc', '', 'abc'), ('', '', '')]
    # тоже выдает результаты по группам

    pattern = r'(\w+)-\1'  # \1 - точно такая же группа, как 1, с точностью до буквы
    string = 'test-test text-text'
    print(re.findall(pattern, string))
    print(re.sub(pattern, r'\1', string))  # test-test заменится на test


def re_flags():

    # IGNORECASE проверяет, подходит ли строка под шаблон без учета регистра
    # DEBUG выдает сводку по нашей подстроке
    print(re.match(r'(te)*xt', "TEXT", re.IGNORECASE | re.DEBUG))


re_module()
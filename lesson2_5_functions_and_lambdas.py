import operator as op
from functools import partial


def fun_map():
    x = input().split()
    y, z = x  # оказывается, так можно
    print(y + z)  # склеенная строка
    y, z = map(int, x)  # применяет функцию int ко всем элементам списка x. является итератором
    print(y + z)  # сумма чисел


# def even(x):
#     return x % 2 == 0

# even = lambda x: x % 2 == 0  # равносильно строчкам выше


def fun_filter():
    x = map(int, input().split())

    # nums = filter(even, x)  # пример применения фильтра - пропускает через even последовательность x.

    nums = filter(lambda y: y % 2 == 0, x)  # лямбда функции можно вызывать, не объявляя их

    # объект этого типа является итератором. его можно представить в виде списка
    print(list(nums))


# def length(name):
#     return len(name)

def sort_list():
    l = ['Kate', 'Anna', 'Dmitry', 'Pit']
    l.sort(key=lambda name: len(name))  # сортируем по результатам функции length, ее можно объявить
    # лямбдой
    print(l)


class Ex:
    a = 10


def op_funcs():
    sum = op.add(4, 5)  # возвращает сумму
    mul = op.mul(4, 5)  # произведение
    bool = op.contains([1, 2, 3], 4)  # содержится ли элемент в списке
    f = op.itemgetter(1)  # при вызове f(x) вернет x[1]
    f = op.attrgetter('a')  # при вызове вернет значение атрибута a
    print(f(Ex))


def funcs_2():
    x = int("1101", base=2)  # говорим, что число будет подаваться в двоичной системе счисления
    int_2 = partial(int, base=2)  # та же самая int, но с начальным параметром base=2
    x = int_2("1101")
    l = ['Kate', 'Anna', 'Dmitry', 'Pit']
    sort_by_name_len = partial(list.sort, key=lambda name: len(name))
    sort_by_name_len(l)
    print(l)


funcs_2()

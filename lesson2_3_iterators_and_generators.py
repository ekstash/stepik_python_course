from random import random


def iteration():
    lst = [1, 2, 3]

    for i in lst:
        print(i)

    # принцип работы цикла for: равнозначно записи

    it = iter(lst)
    while True:
        try:
            i = next(it)
            print(i)
        except StopIteration:
            break


# реализуем собственный итератор в классе - он решает, какой элемент возвращать следующим

class RandomIterator:
    """
Это описание, считающееся документацией. Вызывается параметром doc
    """

    # создаем переменные класса
    def __init__(self, k):
        self.k = k
        self.i = 0

    # говорим, что будет происходить при перечислении
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

    # определяем итератор, обычно возвращает сам класс
    def __iter__(self):
        return self


def random_return():
    x = RandomIterator(3)
    for i in x:
        print(i)
    print(x.__doc__)


def random_generator(k):
    for i in range(k):
        yield random()  # возвращает значение не один раз, а несколько. показывает, что функция является классом
        # типа генератор


# аналог random_return()
def print_generator():
    gen = random_generator(3)
    for i in gen:
        print(i)


def simple_generation():
    print('1')
    yield random()
    print('2')
    return "Mistake text"  # по команде "next" выдаст ошибку с указанным текстом, на for-e не работает, поскольку for
    # по-своему обрабатывает ошибку "StopIteration(?)", в общем случае for будет выполнять код
    # от yield до yield
    yield random()


def print_simple():
    gen = simple_generation()
    print(gen.__next__())
    print(gen.__next__())


def lists():
    x = [-1, 0, 1]
    y = [i * i for i in x if i > 0]  # вариант создания списка. for-ов может быть несколько


def generator():
    z = ((x, y) for x in range(3) for y in range(3) if y >= x)  # это будет генератор
    print(next(z))


random_return()
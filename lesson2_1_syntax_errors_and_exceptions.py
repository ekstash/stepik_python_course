__all__ = ["BadName", "greet"]  # при импорте from ... import * импортируются только эти объекты

def error_catch():
    try:  # блок, в котором может возникнуть ошибка
        x = [1, 2, 'error']
        x.sort()

    except TypeError:  # обработка ошибки типа TypeError; при этом можно не указывать тип вообще - любая ошибка
        print('ошибка типов')


def f(x, y):
    try:
        z = x / y
    except (TypeError, ZeroDivisionError) as e:  # можно передавать сразу кортеж ошибок
        print('Ошибка', e)
        print(isinstance(e, ArithmeticError))  # в отличие от type(), не сравнивает сами типы, а определяет вхождение
    else:
        print(z)
    finally:
        print('Обязательно')


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " - некорректное имя!")  # сами выдаем ошибку типа BadName


_st = "Run"  # таким образом, переменная будет недоступна и при отсутствии __all__

# определим, запускается модуль или импортируется

if __name__ == '__main__':
    print(_st)

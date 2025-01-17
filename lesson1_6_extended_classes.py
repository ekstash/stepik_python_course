# если мы хотим доопределить в качестве класса некий имеющийся где-то класс, мы его наследуем:
class MyList(list):
    def even_length(self):
        return len(self) % 2 == 0


x = MyList()
x.extend([1, 2])
print(x.even_length())

issubclass(MyList, list)  # проверяет, является ли класс list предком класса MyList
isinstance(x, list)  # проверяет, ведет ли x себя как экземпляр класса list

MyList.mro()
# показывает, в каких классах и в каком порядке будет искать методы, вызванные от MyList, в случае множественного
# наследования. Проводится по наследникам определенного класса, затем сам класс. Переход к следующему блоку.
# В случае множественного наследования первым будет названный первым.
# выдаст ошибку, если при наследовании мы сначала указали родителя, потом потомка

class EvenLength:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLength):  # То же самое, но с множественным наследованием. Удобнее тем, что можем создавать
    # несколько классов с данным методом
    # мы также можем переопределять дефолтные методы:
    def pop(self):
        x = super(MyList, self).pop()  # обращаемся к методу pop() родительского класса. в super(x1,x2) x1 - класс,
        # родителей которого мы хотим проверить, x2 - объект, с которымм хотим проассоциировать метод. Можно super()
        print('Last value - ', x)
        return x


class MyDict(dict, EvenLength):
    pass


x = MyList()
x = [1, 2, 3]
print(x.pop())
print(x)

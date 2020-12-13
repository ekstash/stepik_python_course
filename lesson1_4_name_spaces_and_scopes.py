# большая часть урока понятна и так, но есть интересные моменты, о которых я не задумывалась.

for i in range(5):
    x = i * i
print(x)  # здесь x создастся как глобальная переменная.

x = 0


def function():
    global x  # работаем с глобальной переменной x. Именно глобальной, это не работает для функции в функции
    x = 1


print(x)  # x=1


def f():
    x = 0

    def g():
        nonlocal x  # возьмет x из ближайшего пространства имен, содержащего x
        x = 1
class multifilter:

    # допускает элемент, если его допускает хотя бы половина фукнций
    def judge_half(pos, neg):
        if pos >= neg: return True
        return False

    # допускает элемент, если его допускает хотя бы одна функция
    def judge_any(pos, neg):
        if pos >= 1: return True
        return False

    # допускает элемент, если его допускают все функции
    def judge_all(pos, neg):
        if neg == 0: return True
        return False

    # iterable - исходная последовательность
    # funcs - допускающие функции
    # judge - решающая функция
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.i = 0
        self.funcs = funcs
        self.iterable = iterable
        self.judge = judge
        self.pos = 0
        self.neg = 0

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности

    def __next__(self):
        while self.i < len(self.iterable):
            for fun in self.funcs:
                if fun(self.iterable[self.i]) == True:
                    self.pos += 1
                else:
                    self.neg += 1
            pos = self.pos
            neg = self.neg
            self.pos = 0
            self.neg = 0
            if self.judge(pos, neg) == True:
                self.i += 1
                return self.iterable[self.i - 1]
            self.i += 1
        else:
            raise StopIteration


def f_1(x):
    return x % 2 == 0


def f_2(x):
    return x % 3 == 0


x = multifilter([1, 2, 3, 5], f_1, f_2, judge=multifilter.judge_half)

print(list(x))
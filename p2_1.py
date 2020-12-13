# excercize 1

def foo():
    12 / 0


def ex_2_1_1():
    try:
        foo()
    except AssertionError:
        print("AssertionError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ArithmeticError:
        print("ArithmeticError")


# excercize 2


def check_error(error, children, exceptions, errors):
    if error in exceptions:
        if error not in errors:
            print(error)
            errors.append(error)
    else:
        add_all(error, children, exceptions)


def add_all(error, children, exceptions):
    exceptions.add(error)
    if error in children:
        for child in children[error]:
            add_all(child, children, exceptions)


def read(children):
    str = input().split()
    if len(str) >= 3:
        for i in range(2, len(str)):
            if str[i] not in children:
                children[str[i]] = set()
            children[str[i]].add(str[0])


def ex_2_1_2():
    children = dict()
    n = int(input())
    for i in range(n):
        read(children)
    m = int(input())
    exceptions = set()
    errors = []
    for i in range(m):
        error = input()
        check_error(error, children, exceptions, errors)


# excercize 3


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super(PositiveList, self).append(x)

def p_1():
    s, a, b = input(), input(), input()
    res = 0
    if a in b:
        if a in s:
            return "Impossible"
        else:
            return '0'
    while True:
        if a in s:
            res += 1
            s = s.replace(a, b)
        else:
            return str(res)


def p_2():
    s, t = input().strip(), input()
    res = 0
    while True:
        ind = s.find(t)
        if ind == -1:
            return res
        else:
            s = s[ind + 1:]
            res += 1


print(p_2())

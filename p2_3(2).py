def primes():
    simples = [2]
    yield 2
    i = 3
    while True:
        bol = False
        for simple in simples:
            if i % simple == 0:
                bol = True
                break
        if bol == False:
            simples.append(i)
            i += 1
            yield i - 1
        i += 1

gen = primes()
while True:
    print(gen.__next__())

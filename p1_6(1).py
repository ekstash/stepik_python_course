n = int(input())
parents = dict()
childs = dict()


def read():
    cl = input()
    st = ''

    for i in range(len(cl)):  # разбили на созданный класс и его предков
        if cl[i] == ' ':
            st = cl[i + 3:]
            cl = cl[:i]
            break

    if cl not in parents:
        parents[cl] = set()

    if st != '':  # у нашего класса есть предки

        pars = st.split()
        pars1 = set(pars)
        pars1.update(parents[cl])

        for p in pars:  # составили полный список родителей класса
            if p in parents:
                pars1.update(parents[p])
            else:
                parents[p] = set()

        chls = set()  # составили полный список детей класса
        if cl in childs:
            chls = childs[cl]

        for p in pars1:  # всем родителям приписали в дети класс и его детей
            if p in childs:
                childs[p].update(chls)
                childs[p].add(cl)
            else:
                childs[p] = set()
                childs[p].add(cl)
                childs[p].update(chls)

        for c in chls:  # всем детям класса приписали предков
            parents[c].update(pars1)

        parents[cl] = pars1


def search(par, child):
    if par == child:
        return 'Yes'
    if child not in parents:
        return 'No'
    if par in parents[child]:
        return 'Yes'
    return 'No'


for i in range(n):
    read()

n = int(input())

for i in range(n):
    par, child = input().split()
    print(search(par, child))


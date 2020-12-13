n = int(input())

pairs_var = {'global': []}
space_parents = {'global': 'None'}


def search(space, var):
    if space == 'None':
        return 'None'
    elif var in pairs_var[space]:
        return space
    return search(space_parents[space], var)


def read_and_solve():
    global pairs_var
    global space_parents
    command, space, name = input().split()
    if command == 'create':
        space_parents[space] = name
        pairs_var[space] = []
    elif command == 'add':
        pairs_var[space] += [name]
    else:
        print(search(space, name))


for i in range(n):
    read_and_solve()

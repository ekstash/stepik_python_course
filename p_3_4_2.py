import json


def count(x):
    sum = 0
    if x in num:
        return num[x]
    for c in childs[x]:
        sum += 1
        if c in num:
            sum += num[c]
        else:
            sum += count(c)
    num[x] = sum
    return sum


data = input()
dic = json.loads(data)

childs = dict()

for el in dic:
    name = el['name']
    if name not in childs:
        childs[name] = []
    parents = el['parents']
    for p in parents:
        if p not in childs:
            childs[p] = []
        childs[p].append(name)

num = dict()

for c in childs:
    if c not in num:
        num[c] = count(c)

list_keys = list(childs.keys())
list_keys.sort()
for key in list_keys:
    print(key, ':', num[key] + 1)

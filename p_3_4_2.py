import json


def count(x):
    sum = 0
    for c in childs[x]:
        if c in bool_list:
            continue
        bool_list.append(c)
        sum += 1
        sum += count(c)
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
    bool_list=[]
    num[c] = count(c)

list_keys = list(childs.keys())
list_keys.sort()
for key in list_keys:
    print(key, ':', num[key] + 1)

objects = [5, 3, [1, 2], 'hello', 5, [1, 2]]
s = set()
for obj in objects:
    if id(obj) not in s:
        s.add(id(obj))
print('количество разных объектов:', len(s))

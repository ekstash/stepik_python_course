import csv

with open('Crimes.csv') as f:
    reader = csv.DictReader(f)
    a = {}
    for row in reader:
        if str(row['Date']).find('2015') != -1:
            val = row['Primary Type']
            if val not in a:
                a[val] = 1
            else:
                a[val] += 1

    max_num = 0
    max_val = ''
    for v in a:
        if a[v] > max_num:
            max_num = a[v]
            max_val = v
    print(max_val)

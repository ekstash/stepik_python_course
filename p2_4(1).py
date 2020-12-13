with open('input.txt') as f, open('output.txt', 'w') as w:
    lines = f.read().splitlines()
    for i in range(len(lines)-1, -1, -1):
        w.write(lines[i]+'\n')
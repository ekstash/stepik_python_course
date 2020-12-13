import sys
import re


def p_1():
    pattern = r'cat'
    for line in sys.stdin:
        line = line.rstrip()
        if len(re.findall(pattern, line)) > 1:
            print(line)


def p_2():
    pattern = r'\bcat\b'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pattern, line):
            print(line)


def p_3():
    pattern = r'z.{3}z'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pattern, line):
            print(line)


def p_4():
    pattern = r'\\'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pattern, line):
            print(line)


def p_n():
    pattern = r'\b(\w)(\w)(\w*)\b'
    for line in sys.stdin:
        line = line.strip()
        line = re.sub(pattern, r'\2\1\3', line)
        print(line)


def p_k():
    pattern = r'(\w)\1+'
    for line in sys.stdin:
        line = line.strip()
        print(re.findall(pattern, line))
        line = re.sub(pattern, r'\1', line)
        print(line)


def p():
    pattern = r'[^01]'
    for line in sys.stdin:
        line = line.strip()
        if not re.search(pattern, line):
            pattern2 = r'([01])([01])'
            linex = line
            if not len(line) % 2 == 0:
                linex += '0'
            line1 = re.sub(pattern2, r'\1', linex)
            line2 = re.sub(pattern2, r'\2', linex)
            line1 = re.findall('1', line1)
            line2 = re.findall('1', line2)
            if (len(line1) - len(line2)) % 3 == 0:
                print(line)


p()

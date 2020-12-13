from datetime import date, timedelta

from simplecrypt import decrypt, DecryptionException


def ex_2_2_1():
    year, month, day = map(int, input().split())

    d = date(year, month, day)
    delta = timedelta(int(input()))

    data = d + delta

    print(data.year, data.month, data.day)


def ex_2_2_2():

    with open("output.txt", 'w') as output:
        with open("encrypted.bin", "rb") as inp:
            input_file = inp.read()
            with open("passwords.txt", 'rb') as pas:
                passwords = pas.read().splitlines()
                for p in passwords:
                    try:
                        print(p)
                        p = decrypt(p, input_file).decode('utf8')
                        output.write(p)
                    except DecryptionException:
                        print('error')


ex_2_2_2()

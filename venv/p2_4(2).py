import os

os.chdir('C:\\Users\\Lenovo\\Downloads\\main')
list = []
for dir in os.walk(os.getcwd()):
    for file in dir[2]:
        if file[-3:] == '.py':
            list.append(dir[0][26:])
            break

list.sort()

os.chdir('C:\\Users\\Lenovo\\PycharmProjects\\learnStepic_py2')
with open('output.txt', 'w') as file:
    for i in list:
        file.write(i+'\n')
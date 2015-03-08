from functools import reduce
from operator import add

with open("./data/079_keylog.txt", "r") as file:
    content = file.read()

def contentToKeylog(content):
    content = content.splitlines()
    content = list(map(list, content))
    return content

def firstNumber(keylog):
    otherNumbers = list(map(lambda l: l[1:], keylog))
    otherNumbers = reduce(add, otherNumbers)

    for k in range(len(keylog)):
        if not keylog[k][0] in otherNumbers:
            return keylog[k][0]

def removeFirstNumber(keylog, number):
    for k in range(len(keylog)):
        if keylog[k][0] == number:
            keylog[k].pop(0)

    return list(filter(lambda l: len(l) > 0, keylog))

def solveProblem(content=content):
    keylog = contentToKeylog(content)
    password = list()

    while len(keylog) > 0:
        first = firstNumber(keylog)
        keylog = removeFirstNumber(keylog, first)
        password.append(first)

    password = "".join(password)
    return password

if __name__ == '__main__':
    print(solveProblem())
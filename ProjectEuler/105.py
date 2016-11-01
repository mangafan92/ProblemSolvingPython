"""
Principe:
    - on va tout simplement vérifier la définition d'un "special sum set" pour chaque ensemble du fichier
    - cela nécessite de calculer les parties de ensembles donnés
        - ce qui est faisable en temps pas trop long, car les ensembles ont au plus 12 éléments, soit 2^12 = 4096 parties
        - la fonction de vérification est quand même de complexité O(2**n) avec n le nombre d'éléments de l'ensemble, ce qui n'est pas utilisable pour des ensemble de plus de ~25 nombres
"""


def contentToList(content: str) -> list:
    lines = content.splitlines()
    splitline = lambda line: line.split(",")
    lines = list(map(splitline, lines))
    lineToInt = lambda line: list(map(int, line))
    lines = list(map(lineToInt, lines))
    return lines


def subsetsIter(l: list) -> list:
    if not l:
        yield []
    else:
        for e in subsetsIter(l[1:]):
            yield e
            yield [l[0]] + e


def isSpecial(numbers: list) -> bool:
    sumAndSize = list(sorted([(len(s), sum(s)) for s in subsetsIter(numbers)]))

    for k in range(0, len(sumAndSize) - 1):
        if not sumAndSize[k][1] < sumAndSize[k + 1][1]:
            return False

    return True


def solve() -> int:
    filename = "./data/105_sets.txt"
    file = open(filename, "r")
    content = file.read()
    sets = contentToList(content)
    return sum([sum(s) for s in sets if isSpecial(s)])


if __name__ == '__main__':
    print(solve())

"""
Principe:
    - on suppose qu'il n'y a pas de chiffre répété dans le mot de passe
    - chaque ligne du fichier nous informe sur les emplacements des chiffres les uns par rapport aux autres dans un mot de passe correct
    - ijk implique que i est avant j qui est avant k dans un mot de passe correct
    - si un chiffre i n'est présent qu'en première position sur les lignes où il est présent, il est devant tous les autres dans un mot de passe correct
    - on part du mot de passe vide
        - on ajoute à la fin LE chiffre qui est en première position sur toutes les lignes où il est présent
            - si il n'est pas unique, il y a des digits qu'on peut inverser en gardant la validité du mot de passe, il n'y a donc pas unicité du mot de passe minimal, ce qui contredit l'énoncé du problème
            - si ce chiffre n'existe pas, c'est qu'il y a répétition de certains chiffres dans un mot de passe correct (ici, on remarque en faisant tourner l'algorithme que ce n'est pas le cas)
        - on reccommence jusqu'à avoir vidé entièrement toutes les lignes de leurs chiffres
        - on a trouvé un mot de passe minimal, puisqu'on a pas inséré de chiffres "inutiles" (ie des chiffres qu'on pourrait enlever en gardant la validité du mot de passe)
"""

from functools import reduce
from operator import add

with open("./data/079_keylog.txt", "r") as file:
    content = file.read()


def contentToKeylog(content: str) -> list:
    content = content.splitlines()
    content = list(map(list, content))
    return content


def firstNumber(keylog: list) -> int:
    otherNumbers = list(map(lambda l: l[1:], keylog))
    otherNumbers = reduce(add, otherNumbers)

    for k in range(len(keylog)):
        if not keylog[k][0] in otherNumbers:
            return keylog[k][0]


def removeFirstNumber(keylog: list, number: int) -> list:
    for k in range(len(keylog)):
        if keylog[k][0] == number:
            keylog[k].pop(0)

    return list(filter(lambda l: len(l) > 0, keylog))


def solveProblem(content: str = content) -> str:
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

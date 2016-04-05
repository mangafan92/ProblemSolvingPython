"""
Principe:
    - on construit par récurrence des nombres réversibles
    - par exemple, un nombre à 5 chiffres s'écrit abcde, on va fixer les chiffres dans cet ordre: eadbc en s'assurant au fur et à mesure (tous les 2 chiffres fixés) que la fin de la somme du nombre et de son réversible a bien une fin qui s'écrit uniquement avec des impairs
        - en effet, si a et e sont fixés, le dernier chiffre de la somme de abcde et de edcba est fixé
    - ce programme ne respecte pas du tout la règle de la minute, il respecte néanmoins la règle des 10 minutes
"""


def reverse(n: int) -> int:
    return int(str(n)[::-1])


def addReverse(n: int) -> int:
    return n + reverse(n)


def isReversible(n: int, limit: int = None) -> bool:
    """
    :param n: entier
    :param limit: nombre de digit à regarder au maximum dans addReverse(n), on ne regarder que les 3 derniers chiffres si limit = 3, si limit = None alors, on regarde tous les chiffres
    :return: vérifie la définition ?
    """
    np = addReverse(n)
    even = range(0, 10, 2)

    limit = limit + 1 if limit is not None else len(str(np))

    for k in range(0, limit):
        if np // 10 ** k % 10 in even:
            return False
    return True


def reversibles(digits: int):
    """
    :param digits: nombre de digits voulus
    :return: set contenant tous les nombres réversibles possèdant le nombre de chiffres voulu
    """
    output = set()

    def reversiblesRec(n: int, digitToSet: int) -> None:
        """
        :param n: entier qu'on est en train de construire
        :param digitToSet: le chiffre à choisir (on va aussi choisir le chiffre (digits - digitToSet - 1))
        :return: None
        """
        if digits % 2 == 0 and digitToSet == digits // 2:
            if isReversible(n):
                output.add(n)
        elif digits % 2 == 1 and digitToSet == (digits - 1) // 2:
            for k in range(10):
                np = n + k * 10 ** digitToSet
                if isReversible(np):
                    output.add(np)
        else:
            for i in range(0 if digitToSet > 0 else 1, 10):
                for j in range(0 if digitToSet > 0 else 1, 10):
                    np = n + i * 10 ** digitToSet + j * 10 ** (digits - digitToSet - 1)
                    if isReversible(np, digitToSet):
                        reversiblesRec(np, digitToSet + 1)

    reversiblesRec(0, 0)
    return output


def solve(limit: int = 9) -> int:
    return sum(len(reversibles(k)) for k in range(0, limit + 1))


if __name__ == '__main__':
    print(solve())

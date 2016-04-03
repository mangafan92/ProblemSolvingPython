"""
Principe:
    - pour détecter la période de la décomposition en fraction continue, on regarde les restes, dès qu'un reste est répété 2 fois, l'écart entre les 2 répétitions est la période
    - on stocke les restes de manière exacte, les restes s'écrivent (a*(n**(1/2)) + b)/c, 3 coefficients entiers permettent de les définir entièrement
"""

import math
import functools


def dividedByGcd(t: tuple) -> tuple:
    """
    :param t: tuple d'entiers
    :return: tuple divisés par le pgcd de son contenu
    """
    gcd = functools.reduce(math.gcd, t)
    return tuple(map(lambda a: a // gcd, t))


def firstTermAndRemainder(n: int) -> (int, (int, int, int)):
    """
    :param n: entier dont on décompose la racine
    :return: premier terme et premier reste de la décomposition en fraction continue
    """
    term = math.floor(n ** (1 / 2))
    return term, (1, -term, 1)


def nextTermAndRemainder(n: int, lastRemainder: tuple) -> (int, (int, int, int)):
    """
    :param n: entier dont on décompose la racine
    :param lastRemainder: dernier reste calculé
    :return: prochains terme et reste
    """
    a, b, c = lastRemainder
    a, b, c = a * c, -b * c, a ** 2 * n - b ** 2
    a, b, c = dividedByGcd((a, b, c))

    next = math.floor((a * n ** (1 / 2) + b) / c)
    b -= next * c
    return next, (a, b, c)


def addNextTermAndRemainder(n: int, decomposition: list, remainders: list) -> (list, list):
    """
    :param n: entier dont on décompose la racine
    :param decomposition: début décomposition en fraction continue
    :param remainders: debut liste des restes
    :return: decomposition et remainders mis à jour avec les prochaines terme et reste
    """
    an, next = nextTermAndRemainder(n, remainders[-1])
    decomposition.append(an)
    remainders.append(next)
    return decomposition, remainders


def period(n: int) -> int:
    """
    :param n: entier
    :return: période de sa décomposition en fraction continue
    """
    a0, first = firstTermAndRemainder(n)
    decomposition = [a0]
    remainders = [first]

    while remainders[-1] not in remainders[:-1]:  # tant que le reste n'est pas répété, on continue de générer des termes
        decomposition, remainders = addNextTermAndRemainder(n, decomposition, remainders)

    return len(remainders) - remainders.index(remainders[-1]) - 1


def isPerfectSquare(n: int) -> bool:
    """
    :param n: entier
    :return: carré parfait ?
    """
    return int(n ** (1 / 2)) == n ** (1 / 2)


def solve(limit: int = 10000):
    """
    :param limit: paramètre du problème
    :return: solution relative à ce paramètre
    """
    notPerfectSquares = filter(lambda n: not isPerfectSquare(n), range(0, limit + 1))
    periods = map(period, notPerfectSquares)
    oddPeriods = filter(lambda i: i % 2 == 1, periods)
    return len(list(oddPeriods))


if __name__ == '__main__':
    print(solve())

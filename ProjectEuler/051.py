"""
Principe:
    - pas beaucoup d'autres solutions que la force brute:
    - pour chaque premier p, il faut vérifier toutes les manières possibles de remplacer des digits identiques par un autre digit
        - on calcule la liste des emplacements des digits (la case k contient les positions de du digit k dans le nombre)
        - pour chaque digit k, on calcule les parties de la liste des emplacements de ce digit
            - pour chaque partie, on calcule tous les nombres qu'on peut obtenir en changeant les digits de ces emplacements
                - on compte le nombre de premiers qui font partie de la liste de nombres obtenus
                - si on en obtient le nombre voulu, c'est gagné !
"""

from modules.fastPrimalityTest import fastPrimalityTest
from modules.primes import Primes


def powerSet(l: list) -> list:
    if not l:
        yield []
    else:
        for e in powerSet(l[1:]):
            yield e
            yield [l[0]] + e


def digitPositions(n: int) -> list:
    positions = [[] for k in range(10)]
    for position, digit in enumerate(str(n)):
        positions[int(digit)].append(position)
    return positions


def replaceDigitsWith(number: int, positions: list, digit: int) -> int:
    number = list(str(number))
    for position in positions:
        number[position] = str(digit)
    return int("".join(number))


def replaceDigitsWithAllDigit(number: int, positions: list) -> list:
    output = [replaceDigitsWith(number, positions, digit) for digit in range(10)]
    return [e for e in output if len(str(e)) == len(str(number))]


def families(number: int):
    positions = digitPositions(number)
    for i in range(10):
        if positions[i]:
            for replacementPossibility in powerSet(positions[i]):
                if replacementPossibility and (i != 0 or 0 not in replacementPossibility):
                    yield replaceDigitsWithAllDigit(number, replacementPossibility)


def primesInFamily(family: list) -> list:
    isPrime = lambda n: fastPrimalityTest(n, 10)
    return list(filter(isPrime, family))


def solve(familySize: int = 8) -> int:
    primes = Primes()
    for prime in primes:
        for family in families(prime):
            if len(primesInFamily(family)) == familySize:
                return min(primesInFamily(family))


if __name__ == '__main__':
    print(solve(8))

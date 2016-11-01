"""
Principe:
    - on peut décomposer un nombre en somme de premiers récursivement
    - cette méthode fonctionne en pratique: on décompose tous les nombres entiers en somme de premiers jusqu'à en trouver un qui a plus de 1000 décompositions, on trouve une solution assez rapidement
"""

import copy
import modules.primes

primes = modules.primes.Primes()


def decompose(number, elements):
    elements = list(copy.copy(elements))
    elements.sort()
    elements.reverse()
    elements = tuple(elements)

    def decomposeRecur(number, elements):
        decompositions = 0
        for k in range(len(elements)):
            if number - elements[k] == 0:
                decompositions += 1
            elif number - elements[k] >= 0:
                decompositions += decomposeRecur(number - elements[k], elements[k:])
        return decompositions

    return decomposeRecur(number, elements)


def solveProblem(limit=5000):
    k = 10
    while decompose(k, primes.getPrimesBelow(k)) < limit:
        k += 1
    return k


if __name__ == '__main__':
    print(solveProblem())

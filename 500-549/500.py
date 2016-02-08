"""
Principe:
    - le fait que le nombre ait 2^500500 diviseurs nous renseigne beaucoup sur sa décomposition en facteurs premiers, les valuations sont forcéments de la forme 2^k - 1 pour un certain k et la somme des k en question fait 500500
    - on montre assez facilement que cette décomposition ne comporte que des facteurs premiers faisant partie des 500500 plus petits nombres premiers (par l'absurde)
    - on va partir de N=1, et le multiplier par des nombres jusqu'à atteindre 500500 diviseurs, en s'assurant de conserver à tout moment des valuations de la forme 2^k - 1
    - si la valuation d'un premier p est 2^k - 1, on peut la passer à 2^(k+1) - 1 en multipliant N par p^(2^k)
    - on continue jusqu'à atteindre 2^500500 diviseurs, en multipliant à chaque étape par le premier p de valuation k tel que p^(2^k) est minimum
    - on multiplie à chaque étape le nombre de diviseurs de N par 2, en faisant le moins possible grandir N

Optimisation:
    - on va gérer une liste des coûts, qui contient les indices des nombres premiers classés par "coût de multiplication" décroissant (ie, nombre par lequel il faut multiplier pour passer leur valuation dans n à la puissance de 2 suivante)
    - cette liste contient 500500 indices (cela est lié au fait que seuls les 500500 premiers nombres premiers peuvent faire partie de la décomposition du nombre cherché)
    - à chaque étape, on augmente la valuation du premier nombre premier de la liste puis on le déplace à son nouvel emplacement par recherche dichotomique
    - ce programme est le plus rapide que j'ai réussi à faire (après 2 autres essais infructueux), mais il ne respecte pas la règle de la minute...
"""

import math

from modules.primes import Primes
from modules.primeDecomposition import PrimeDecomposition

primes = Primes()


def insert(costs: list, result: PrimeDecomposition) -> None:
    toInsert = costs.pop(0)

    def insertRec(a: int, b: int):
        m = (a + b) // 2
        if b - a > 1:
            if math.log2(primes[costs[m]]) * (result[primes[costs[m]]] + 1) > math.log2(primes[toInsert]) * (result[primes[toInsert]] + 1):  # On passe au log pour éviter de comparer des nombres immenses
                return insertRec(a, m)
            else:
                return insertRec(m, b)
        else:
            costs.insert(b, toInsert)


    insertRec(0, len(costs) - 1)


def solve(n: int = 500500) -> int:
    result = PrimeDecomposition(1)
    costs = list(range(n))  # Liste des coûts de multiplication

    for k in range(n):
        result[primes[costs[0]]] += result[primes[costs[0]]] + 1  # 2**(k+1) - 1 = 2**k - 1 + ((2**k - 1) + 1)
        insert(costs, result)

    return result.value(modulo=500500507)


if __name__ == '__main__':
    print(solve())

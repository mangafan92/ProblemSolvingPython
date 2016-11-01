"""
Principe:
    - on va générer par récurrence toutes les familles qui vérifient cette propriété et dont les éléments sont majorés par p[i+1] premier à partir de celles majorées par p[i]
        - il suffit de vérifier dans quelles familles on peut ajouter p[i+1] et ajouter ces nouvelles familles au set pour générer toutes les familles dont les éléments majorées par p[i+1]
        - on ajoute aussi la famille qui ne contient que p[i+1]
    - dès qu'on trouve une famille qui a la bonne taille, on s'arrête (difficile de prouver que l'on a trouvé la famille avec la somme la plus petite, et pourtant, pour les petites valeurs, ça fonctionne...)

Optimisation:
     - la vérification que la concaténation de p[i] et p[j] est un nombre premier est une opération coûteuse, on stocke les résultats dans un dict pour diminuer le nombre de "vrais" appels de la fonction
"""

from modules.primes import Primes
from modules.fastPrimalityTest import fastPrimalityTest

concatPrimes = dict()


def isConcatPrime(a, b) -> bool:
    try:
        return concatPrimes[(a, b)]
    except:
        isPrime = lambda n: fastPrimalityTest(n, 10)
        concatPrimes[(a, b)] = isPrime(int(str(a) + str(b))) and isPrime(int(str(b) + str(a)))
        return concatPrimes[(a, b)]


def areAllConcatPrimes(p: int, l: list):
    for n in l:
        if not isConcatPrime(p, n):
            return False
    return True


def improveSetList(prime: int, setList: list, lengthSeeked: int):
    newCorrectSets = list()
    setList.append([prime])
    for a in setList:
        if areAllConcatPrimes(prime, a):
            setList.append([prime] + a)
            if len(a) == lengthSeeked - 1:
                newCorrectSets.append([prime] + a)
    return newCorrectSets


def solve(lengthSeeked: int = 5) -> int:
    primes = Primes()
    correctSets = list()

    setList = [[2]]
    i = 1
    while True:
        correctSets += improveSetList(primes[i], setList, lengthSeeked)
        if correctSets:
            correctSets = [min(correctSets, key=sum)]
            break
        i += 1

    return sum(correctSets[0])


if __name__ == '__main__':
    print(solve())

"""
Principe:
    - cela revient à sommer les valeurs de l'indicatrice d'Euler pour  2 <= d <= 1000000
    - on utilise la formule qui donne l'indicatrice en fonction de la décomposition en facteurs premiers
        - source: https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler#Calcul
"""

from modules.primes import Primes


def eulerTotients(limit: int) -> list:
    primes = Primes()
    totients = [k for k in range(limit + 1)]
    p = 0
    while primes[p] < limit + 1:
        k = 1
        while k * primes[p] < limit + 1:
            totients[k * primes[p]] *= 1 - 1 / primes[p]
            k += 1
        p += 1
    return list(map(int, totients))


def solve(limit: int = 10 ** 6) -> int:
    return sum(eulerTotients(limit)[2:])


if __name__ == '__main__':
    print(solve())

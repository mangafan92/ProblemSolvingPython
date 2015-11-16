"""
Principe:
    - on utilise la formule qui donne l'indicatrice d'Euler de n à partir de sa décomposition en facteurs premiers
    - source: https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler#Calcul
"""

from modules.primes import Primes


def solve():
    primes = Primes()
    maximum = (0, 0)

    for k in range(1, 10 ** 6):
        totient = primes.eulerTotient(k)
        maximum = max(maximum, (k / totient, k))

    return maximum[1]


if __name__ == '__main__':
    print(solve())

"""
Principe:
    - on utilise la formule qui donne l'indicatrice d'Euler de n à partir de sa décomposition en facteurs premiers
        - source: https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler#Calcul
    - avec cette formule n/phi(n) = 1/(produit des (1-1/p)) pour p appartenant la la décomposition en facteurs premiers de n
    - on part de n = 1, qu'on va multiplier par des premiers successifs
    - tant que n < 10**6, on multiplie n par le prochain premier
    - si n dépasse la limite, on s'arrête et on renvoie n
"""

from modules.primes import Primes


def solve(limit=10 ** 6) -> int:
    primes = Primes()
    n = 1
    for prime in primes:
        if n * prime < limit:
            n *= prime
        else:
            break
    return n


if __name__ == '__main__':
    print(solve())

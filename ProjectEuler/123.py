"""
Principe:
    - on remarque la suite des reste vaut 2 pour un indice sur 2 et est croissante si on se restreint aux autres indices
    - on effectue donc une recherche dichotomique dans la liste des nombres premiers en se restreignant à ceux qui ont l'indice de la bonne parité
"""

from modules.primes import Primes

primes = Primes()


def remainder(n: int) -> int:
    return ((primes[n] - 1) ** (n + 1) % primes[n] ** 2 + (primes[n] + 1) ** (n + 1) % primes[n] ** 2) % primes[n] ** 2


def dichoRecur(a: int, b: int, limit: int) -> (int, int):
    h = (a + b) // 2
    h += h % 2
    if abs(b - a) > 2:
        if remainder(h) < limit:
            return dichoRecur(h, b, limit)
        else:
            return dichoRecur(a, h, limit)
    else:
        return a, b


def solve(limit: int = 10 ** 10) -> int:
    i = 2
    while remainder(i) < limit:
        i *= 2
    res = dichoRecur(1, i, limit)
    candidates = range(res[0] - 1, res[1] + 1)
    candidates = list(filter(lambda i: remainder(i) >= limit, candidates))
    return min(candidates) + 1


if __name__ == '__main__':
    print(solve(10 ** 10))

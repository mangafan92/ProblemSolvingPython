"""
Principe:
    - les nombres pandigitaux sont des nombres dont l'écriture en base 10 est une permutation des chiffres 0 à 9 ne commençant pas par 0
    - il y en a un nombre pas trop grand, on peut tester la condition voulue pour chaque nombre en temps raisonnable
"""

import itertools


def solve() -> int:
    ok = lambda e: e[0] != "0" and int(e[1:4]) % 2 == 0 and int(e[2:5]) % 3 == 0 and int(e[3:6]) % 5 == 0 and int(e[4:7]) % 7 == 0 and int(e[5:8]) % 11 == 0 and int(e[6:9]) % 13 == 0 and int(e[7:10]) % 17 == 0
    return sum(int("".join(e)) for e in itertools.permutations(map(str, range(0, 10))) if ok("".join(e)))


if __name__ == '__main__':
    print(solve())

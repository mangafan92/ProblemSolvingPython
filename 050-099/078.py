"""
Principe:
    - le problème revient à trouver l'entier le plus petit dont le nombre de partitions est divisé par 1 million
    - on va utiliser l'application du théorème d'Euler qui donne une relation de récurrence sur le nombre de partitions des nombres entiers
        - source: https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_nombres_pentagonaux#Application

Optimisation:
    - on stocke les résultats des appels récursifs dans un dict pour éviter de recalculer plusieurs fois les mêmes valeurs au cours de l'exécution
    - on effectue tous les calculs modulo 1 million
"""

partitionsDict = {0: 1, 1: 1}


def pentagonalNumber(k: int) -> int:
    return k * (3 * k - 1) // 2


def partitions(i: int) -> int:
    try:
        return partitionsDict[i]
    except:
        partitionsDict[i] = 0
        k = 1
        while i - k * (3 * k - 1) // 2 >= 0:
            partitionsDict[i] += (-1) ** (k - 1) * partitions(i - pentagonalNumber(k)) % 10 ** 6
            k += 1

        k = -1
        while i - k * (3 * k - 1) // 2 >= 0:
            partitionsDict[i] += (-1) ** (k - 1) * partitions(i - pentagonalNumber(k)) % 10 ** 6
            k -= 1

        partitionsDict[i] = int(partitionsDict[i]) % 10 ** 6
        return partitionsDict[i]


def solve() -> int:
    i = 1
    while partitions(i) != 0:
        i += 1
    return i


if __name__ == '__main__':
    print(solve())

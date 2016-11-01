"""
Principe:
    - on génère les triplets pythagoriciens dont la somme est inférieure à 1500000 en utilisant la formule d'Euclide (https://fr.wikipedia.org/wiki/Triplet_pythagoricien#Th.C3.A9or.C3.A8me_fondamental)
    - il ne faut pas oublier de prendre en compte aussi tous les triplets multiples de ceux qu'on obtient avec cette formule (sinon on oublie certains triplets)

Optimisation possible:
    - on pourrait rendre ce programme plus rapide en ne produisant via la formule que les triplets primitifs (x, y et z premiers dans leur ensemble)
"""


def pythagoreanTriples(limit):
    i = 1
    while i <= limit:
        j = 1
        while j < i and 2 * i ** 2 + 2 * i * j <= limit:
            yield tuple(sorted((i ** 2 - j ** 2, 2 * i * j, i ** 2 + j ** 2)))
            j += 1
        i += 1


def solve(limit=1500000):
    triples = [set() for k in range(limit + 1)]

    for t in pythagoreanTriples(limit):
        triples[sum(t)].add(t)

        k = 2
        while k * sum(t) < limit:
            triples[k * sum(t)].add(tuple(k * p for p in t))
            k += 1

    count = [len(t) for t in triples]
    return count.count(1)


if __name__ == '__main__':
    print(solve())

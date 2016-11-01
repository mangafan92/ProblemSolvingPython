"""
Principe:
    - les nombres premiers sont en fait des endroits qu'on peut visiter via un certain chemin et d'une certaine façon on cherche le chemin le plus "court" pour aller vers chaque nombre premier depuis 2
    - on peut utiliser Dijkstra pour trouver les chemins en question

Optimisation:
    - on utilise le module heapq comme couche d'abstraction pour gérer la file de priorité, pour passer de O(n) = O(log(n)) pour extraire le prochain élément, l'implémentation bourrin est trop lente
"""

import modules.eratosthenesSieve

import heapq


def relatives(n):
    """Retourne tous les nombres connectés à n sans vérifier leur primalité"""
    l = list(str(n))

    for i in range(1, 10):
        yield int("".join([str(i)] + l))

    for i in range(len(l)):
        for d in range(1 if i == 0 else 0, 10):
            m = list(str(n))
            m[i] = str(d)
            if m != l:
                yield int("".join(m))

    if len(l) >= 2 and l[1] != "0":
        yield int("".join(l[1:]))


def connected(primes, beg=2):
    """Retourne tous les premiers de la liste connectés à beg"""
    primes = set(primes)  # pour accélérer la vérification d'appartenance aux nombres premiers

    awaiting = [(beg, beg)]  # queue de la forme [(maximum, nombre premier)]
    seen = {beg}  # nombre qu'on a déjà vu au cours du processus, et qu'il ne faut plus ajouter à la queue

    maximums = {beg: beg}  # plus petits maximums

    while awaiting:
        p = heapq.heappop(awaiting)[1]

        for r in relatives(p):
            if r in primes and not r in seen:
                maximums[r] = max([maximums[p], p, r])
                seen.add(r)
                heapq.heappush(awaiting, (maximums[r], r))

    return filter(lambda e: e >= maximums[e], maximums)


def solve(limit=10 ** 7 + 1):
    primes = list(modules.eratosthenesSieve.primes(limit))
    return sum(primes) - sum(list(sorted(connected(primes))))


if __name__ == '__main__':
    print(solve())

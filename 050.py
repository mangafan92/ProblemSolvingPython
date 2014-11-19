from modules.primes import *
from time import time

init = time()

limit = 10**6

premiers = Primes()
premiers = premiers.range(0, premiers.firstAbove(limit))

sommes = [premiers[0]]

for k in range(1, len(premiers)):
    sommes.append(sommes[k-1] + premiers[k])

solution = (0, 0)

for i in range(len(sommes)):
    for j in range(i + solution[1], len(sommes)):
        if sommes[j] - sommes[i] > limit:
            break
        elif sommes[j] - sommes[i] in premiers and j-i > solution[1]:
            solution = (sommes[j] - sommes[i], j-i)

print("Le nombre premier inférieur à {} et décomposable en plus grande somme de nombres premiers consécutifs est {} et sa décomposition comporte {} termes.".format(limit, solution[0], solution[1]))
print("{}s".format(round(time() - init, 3)))
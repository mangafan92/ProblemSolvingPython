from modules.anagram import *
from modules.primes import *

primes = Primes()
k = 0
circular = 0

while primes.get(k) < 10**2:
    element = primes.get(k)
    permutations = anagram(str(element), len(str(element)))
    for i in range(len(permutations)):
        permutations[i] = int(permutations[i])
    if primes.arePrimes(permutations):
        circular += 1
        print(element, circular)
    k += 1
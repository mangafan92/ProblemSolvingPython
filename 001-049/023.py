import itertools

import modules.primes

primes = modules.primes.Primes()
limit = 28124
isAbundant = lambda n: sum(primes.divisors(n)) - n > n
abundants = list(filter(isAbundant, range(0, limit)))
numbers = [False for k in range(0, limit)]

for i, j in itertools.product(range(len(abundants)), repeat=2):
    sumTmp = abundants[i] + abundants[j]
    if sumTmp < limit:
        numbers[sumTmp] = True

sumNonAbundants = sum(list(filter(lambda n: not numbers[n], range(limit))))

print(sumNonAbundants)
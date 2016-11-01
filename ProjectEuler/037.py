from modules.primes import Primes
import math

primes = Primes()

def isTruncable(prime):
    size = math.ceil(math.log10(prime))
    for k in range(1, size):
        if not (primes.isPrime(prime//(10**k)) and primes.isPrime(prime%(10**k))):
            return False
    return True

truncables = list()

k = 5

while len(truncables) < 11:
    if isTruncable(primes[k]):
        truncables.append(primes[k])
    k += 1

print(sum(truncables))

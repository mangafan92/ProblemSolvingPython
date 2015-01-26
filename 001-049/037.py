import math

from modules.primes import Primes

primes = Primes()

def isTruncable(n):
    for k in range(1, math.ceil(math.log10(n))):
        if not primes.isPrime(n % 10**k) or not primes.isPrime(n // 10**k):
            return False
    return True

truncables = []

for prime in primes:
    if prime >= 10 and isTruncable(prime) :
        truncables.append(prime)
        print(truncables)
        if len(truncables) >= 11:
            break

print(sum(truncables))
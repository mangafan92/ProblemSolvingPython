from modules.primes import Primes

def isCircular(prime, primes):
    prime = str(prime)

    for k in range(len(prime)):
        prime = prime[1:len(prime)] + prime[0]
        if not int(prime) in primes:
            return False
    return True

primes = Primes()

primesBelowLimit = primes.getPrimesBelow(10**6)

circular = 0

for prime in primesBelowLimit:
    if isCircular(prime, primesBelowLimit):
        circular += 1
        # print(prime)

print(circular)
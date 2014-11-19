from modules.primes import *

primes = Primes()

n = int(input("Nombre:"))

print("Le", n, "-ième nombre premier est", primes.get(n-1), ".")
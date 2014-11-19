from modules.primes import *

primes = Primes()

borne = int(input("Nombre:"))
s = 0
k = 0

while primes.get(k) < borne:
    s += primes.get(k)
    k += 1

print("La somme des nombres premiers inférieurs à", borne, "est", s, ".")
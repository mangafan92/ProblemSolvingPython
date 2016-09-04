"""
Principe:
    - soit f(n) la somme des diviseurs de n en incluant n
    - on a f(nm) = f(n)f(m) pour n et m premiers entre eux
    - on va donc calculer tous les f(n) en utilisant la programmation dynamique et l'algorithme de Brent pour extraire un facteur premier des n
    - ensuite, on utilise encore la programmation dynamique pour calculer toutes les longueurs des chaînes, en faisant bien attention d'exclure les chaînes qui ne sont pas correctes où qui sortent des bornes
"""

import modules.eratosthenesSieve

import random
import math

primes = modules.eratosthenesSieve.primes(10 ** 6 + 1)


def brent(n):
    g = 1
    while g == 1 or g == n:
        if n % 2 == 0:
            return 2
        y, c, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
        g, r, q = 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = ((y * y) % n + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = ((y * y) % n + c) % n
                    q = q * (abs(x - y)) % n
                g = math.gcd(q, n)
                k += m
            r += r
        if g == n:
            while True:
                ys = ((ys * ys) % n + c) % n
                g = math.gcd(abs(x - ys), n)
                if g > 1:
                    break
    return g


def AB(a, b):
    if math.gcd(a, b) == 1:
        return a, b
    else:
        return AB(a // math.gcd(a, b), b * math.gcd(a, b))


def sumDivisorsPrimePower(prime, power):
    return int((prime ** (power + 1) - 1) / (prime - 1))


def primeFactor(n, sums):
    a = brent(n)
    while a == n or (a in sums and sums[a] != a + 1):
        a //= brent(a)

    return a


def powerDivisor(n, divisor):
    power = 0
    while n % divisor == 0:
        n //= divisor
        power += 1
    return power


def sumDivisors(limit):
    primes = list(modules.eratosthenesSieve.primes(limit))
    sums = {0: 0, 1: 0}

    for prime in primes:
        power = 0
        while prime ** power < limit:
            sums[prime ** power] = sumDivisorsPrimePower(prime, power)
            power += 1

    for n in range(2, limit + 1):
        if n not in sums:
            pf = primeFactor(n, sums)
            power = powerDivisor(n, pf)
            sums[n] = sums[pf ** power] * sums[n // (pf ** power)]

    return {n: sums[n] - n for n in sums}


def length(n, sums, limit):
    l = [n]
    while l[-1] <= limit and sums[l[-1]] not in l:
        l.append(sums[l[-1]])

    if l[-1] > limit or l[0] != sums[l[-1]]:
        return [n]
    else:
        return l


def solve(limit=10 ** 6):
    sums = sumDivisors(limit)

    lengths_ = dict()

    for n in range(2, limit + 1):
        if not n in lengths_:
            l = length(n, sums, limit)
            for x in l:
                lengths_[x] = len(l)

    key = lambda a: (a[0], -a[1])

    lengths_ = [(lengths_[n], n) for n in lengths_]

    return max(lengths_, key=key)[1]

if __name__ == '__main__':
    print(solve())


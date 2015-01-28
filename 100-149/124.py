import functools

from modules.primes import Primes

primes = Primes()

radicals = {
    k: primes.decomposeProduct(k) for k in range(1, 10**5+1)
}

for k in radicals:
    try:
        radicals[k] = functools.reduce(lambda a, b: a*b, radicals[k])
    except:
        try:
            radicals[k] = radicals[k][1]
        except:
            radicals[k] = 1

print(radicals)

radicals = list(sorted(radicals, key=lambda k:(radicals[k], k)))

print(radicals)
print(radicals[9999])
import modules.primes

primes = modules.primes.Primes()


def triangular(n):
    return n * (n + 1) // 2


def solveProblem(limit=500):
    k = 0
    while primes.numberOfDivisors(triangular(k)) < limit:
        k += 1
    return triangular(k)


if __name__ == '__main__':
    print(solveProblem())

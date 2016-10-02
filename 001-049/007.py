import modules.eratosthenesSieve


def solveProblem(number=10001):
    limit = 2
    while True:
        try:
            return list(modules.eratosthenesSieve.primes(limit))[number - 1]
        except:
            limit *= 2


if __name__ == '__main__':
    print(solveProblem())

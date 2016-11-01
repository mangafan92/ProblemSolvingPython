import modules.eratosthenesSieve


def solveProblem(limit=2 * 10 ** 6):
    return sum(modules.eratosthenesSieve.primes(limit + 1))


if __name__ == '__main__':
    print(solveProblem())

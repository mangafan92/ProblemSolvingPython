import modules.primes

primes = modules.primes.Primes()

def solveProblem(limit=2*10**6):
    result = 0
    k = 0
    while primes[k] < limit:
        result += primes[k]
        k += 1
    return result

if __name__ == '__main__':
    print(solveProblem())
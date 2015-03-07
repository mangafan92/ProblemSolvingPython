import modules.primes
primes = modules.primes.Primes()

def solveProblem(number=10001):
    return primes[number-1]

if __name__ == '__main__':
    print(solveProblem())
import modules.primes

primes = modules.primes.Primes()

def solveProblem(limit=10000):
    sums = [0] + list(map(lambda n: sum(primes.divisors(n))-n, range(1, limit+1)))
    amical = list()
    for number in range(1, limit+1):
        try:
            if number == sums[sums[number]] and sums[number] != number:
                amical.append(number)
        except:
            pass

    result = sum(amical)
    return result

if __name__ == '__main__':
    print(solveProblem())
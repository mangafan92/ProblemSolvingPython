import modules.primes

primes = modules.primes.Primes()

def calculateProducts(limit, powers):
    numbers = set()
    def calculateProductsRecur(number, powers):
        if len(powers) == 0:
            numbers.add(number)
        else:
            k = 0
            while number + primes[k]**powers[0] <= limit:
                calculateProductsRecur(number + primes[k]**powers[0], powers[1:])
                k += 1

    calculateProductsRecur(0, powers)
    return len(list(numbers))

def solveProblem(limit= 50*10**6, powers=[2, 3, 4]):
    return calculateProducts(limit, powers)

if __name__ == '__main__':
    print(solveProblem())
from modules.primes import Primes

def products(numbers, limit, start=1):
    output = set()

    def productsRec(tmpProduct, numbers):
        if tmpProduct <= limit:
            output.add(tmpProduct)
            if numbers:
                for k in range(len(numbers)):
                    productsRec(tmpProduct*numbers[k], numbers[k:])

    productsRec(start, numbers)
    return output

def solveProblem():
    primes = Primes()
    numbers = primes.getPrimesBelow(100)

    return len(list(products(numbers, 10**9, 1)))

if __name__ == '__main__':
    print(solveProblem())
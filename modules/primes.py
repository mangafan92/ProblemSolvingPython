import os
import pickle


class Primes(list):
    WRITE_FREQUENCY = 5000

    def __init__(self):
        super().__init__([2])
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.file = self.dir + "/data/primes"
        self.read()

    def get(self, n):
        self.addPrimesToId(n + 1)
        return list.__getitem__(self, n)

    def __getitem__(self, item):
        while True:
            try:
                return list.__getitem__(self, item)
            except:
                self.addNextPrime()

    def addPrimesToId(self, n):
        while len(self) < n:
            self.addNextPrime()

    def addPrimeToNumber(self, n):
        while self[-1] < n:
            self.addNextPrime()

    def addNextPrime(self):
        n = self[-1] + 1
        while not self.isNextPrime(n):
            n += 1
        self.append(n)
        if len(self) % Primes.WRITE_FREQUENCY == 0:
            self.write()

    def isPrime(self, n):
        self.addPrimeToNumber(n)

        def isPrimeRecur(a, b):
            m = (a + b) // 2

            if self[m] == n:
                return True
            elif a - b == 0:
                return False
            elif self[m] > n:
                return isPrimeRecur(a, m)
            else:
                return isPrimeRecur(m + 1, b)

        return isPrimeRecur(0, len(self))

    def __contains__(self, item):
        if type(item) == int:
            return self.isPrime(item)
        else:
            return list.__contains__(self, item)

    def arePrimes(self, table):
        for n in table:
            if not self.isPrime(n):
                return False
        return True

    def isNextPrime(self, n):
        for number in self:
            if n % number == 0:
                return False
            elif number > n ** (1 / 2) + 1:
                break
        return True

    def firstAbove(self, n):
        i = 0
        while self.get(i) <= n:
            i += 1
        return i

    def range(self, n, m):
        output = []
        for k in range(n, m):
            output.append(self[k])
        return output

    def getPrimesBelow(self, n):
        primes = list()
        for prime in self:
            if prime > n:
                break
            primes.append(prime)
        return primes

    def decomposeProduct(self, n):
        decomposition = dict()
        k = 0
        while n > 1:
            if n % self[k] == 0:
                n //= self[k]
                try:
                    decomposition[self[k]] += 1
                except:
                    decomposition[self[k]] = 1
            else:
                k += 1

        return decomposition

    def divisors(self, n):
        decomposition = self.decomposeProduct(n)
        divisors = set()

        def divisorsRecur(start, factors):
            if len(list(factors.keys())) > 0:
                smaller = min(factors.keys())
                otherFactors = {n: factors[n] for n in list(sorted(factors.keys()))[1:]}
                for k in range(0, factors[smaller] + 1):
                    divisors.add(start * (smaller ** k))
                    divisorsRecur(start * (smaller ** k), otherFactors)

        divisorsRecur(1, decomposition)
        return list(sorted(divisors))

    def numberOfDivisors(self, n):
        decomposition = self.decomposeProduct(n)
        divisors = 1
        for prime in decomposition:
            divisors *= decomposition[prime] + 1
        return divisors

    def read(self):
        try:
            super().__init__(pickle.load(open(self.file, "rb")))
        except:
            pass

    def write(self):
        try:
            datadir = self.dir + "/data"
            if not os.path.isdir(datadir) and not os.path.isfile(datadir):
                os.mkdir(datadir)
            pickle.dump(self, open(self.file, "wb"))
        except:
            pass

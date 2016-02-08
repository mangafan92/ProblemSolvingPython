from functools import reduce
from operator import mul

import modules.primes

primes = modules.primes.Primes()


class PrimeDecomposition(dict):
    def __init__(self, n):
        super().__init__(primes.decomposeProduct(n))

    def largerPrimeFactor(self) -> int:
        self.cleanZeroes()
        return max(self.keys())

    def __getitem__(self, item) -> int:
        try:
            return dict.__getitem__(self, item)
        except:
            return 0

    def __mul__(self, other):
        keys = list(sorted(set(list(self.keys()) + list(other.keys()))))
        product = {key: self[key] + other[key] for key in keys}
        output = PrimeDecomposition(1)
        super(PrimeDecomposition, output).__init__(product)
        output.cleanZeroes()
        return output

    def __pow__(self, power, modulo=None):
        powed = {key: self[key] * power for key in self}
        output = PrimeDecomposition(1)
        super(PrimeDecomposition, output).__init__(powed)
        return output

    def __truediv__(self, other):
        other = other ** -1
        return self * other

    def value(self, modulo: int = None):
        try:
            factors = [key ** self[key] for key in self]
            reduceFunction = (lambda a, b: (a * b) % modulo) if modulo is not None else mul
            return reduce(reduceFunction, factors)
        except:
            return 1

    def numberOfDivisors(self):
        if self:
            return reduce(mul, map(lambda x: self[x] + 1, self))
        else:
            return 1

    def cleanZeroes(self) -> None:
        keys = list(self.keys())
        for key in keys:
            if self[key] == 0:
                self.pop(key)

    @staticmethod
    def factorial(n):
        if n in (0, 1):
            return PrimeDecomposition(1)
        else:
            return PrimeDecomposition(n) * PrimeDecomposition.factorial(n - 1)

    @staticmethod
    def pascalCoefficient(k, n):
        return PrimeDecomposition.factorial(n) / (PrimeDecomposition.factorial(n - k) * PrimeDecomposition.factorial(k))

import copy


class Polynomial(list):
    @staticmethod
    def constructorEmpty(degree: int):
        return Polynomial([0 for k in range(degree + 1)])

    def simplify(self) -> None:
        while len(self) > 0 and self[-1] == 0:
            self.pop(-1)

    def degree(self) -> int:
        self.simplify()
        return len(self) - 1

    def value(self, x):
        return sum([self[i] * x ** i for i in range(len(self))])

    def __add__(self, other):
        resultDegree = max(self.degree(), other.degree())
        result = Polynomial.constructorEmpty(resultDegree)

        for i in range(len(self)):
            result[i] += self[i]

        for j in range(len(other)):
            result[j] += other[j]

        result.simplify()
        return result

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        resultDegree = self.degree() + other.degree()
        result = Polynomial.constructorEmpty(resultDegree)

        for i in range(len(self)):
            for j in range(len(other)):
                result[i + j] += self[i] * other[j]

        result.simplify()
        return result

    def __imul__(self, other):
        return self * other

    # Interpolation
    @staticmethod
    def constructorLagrangePolynomial(x: list, y: list):
        result = Polynomial([])
        for i in range(0, len(x)):
            result += Polynomial([y[i]]) * Polynomial.constructorSubLagrangePolynomial(x, i)
        return result

    @staticmethod
    def constructorSubLagrangePolynomial(x: list, i: int):
        result = Polynomial([1])
        for k in range(0, len(x)):
            if k != i:
                result *= Polynomial([-x[k], 1])
                result *= Polynomial([1 / (x[i] - x[k])])
        return result


if __name__ == '__main__':
    print(Polynomial.constructorLagrangePolynomial([0, 1, 2], [1, 3, 7]))

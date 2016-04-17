"""
Principe:
    - algorithme naïf, on teste toutes les fractions ayant un dénominateur inférieur à 12000 et on ne garde que les irréductibles
"""

import math


def solve(limit: int = 12000) -> int:
    return sum(1 for denominator in range(2, limit + 1) for numerator in range(denominator // 3 + 1, (denominator - 1) // 2 + 1) if math.gcd(numerator, denominator) == 1)


if __name__ == '__main__':
    print(solve())

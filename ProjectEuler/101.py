"""
Principe:
    - on va tout simplement déterminer les BOP en utilisant l'interpolation de Lagrange puis les évaluer au rang d'après pour obtenir le FIT
    - on sait que seuls les 10 premiers polynômes seront des BOP, et que les 11ème sera le polynôme Un, ainsi, on ne calcule que 10 polynômes par interpolation
    - durant l'interpolation de Lagrange, on effectue beaucoup d'ospérations, et stocker les nombres sous forme de flottants en mémoire propage des erreurs dant les calculs, qui conduisent à un résultat pas assez précis (l'erreur dépasse 1)
        - on corrige cela en sacrifiant un peu de temps de calcul -> on utilise des fractions, puisque tout les nombres sur lesquels on fait des calculs sont rationnels
"""

from fractions import Fraction

from modules.polynomial import Polynomial


def un(n: int) -> int:
    return sum([(-1) ** (k % 2) * n ** k for k in range(0, 11)])


def OP(sequence: list) -> Polynomial:
    return Polynomial.constructorLagrangePolynomial(list(map(Fraction, range(1, len(sequence) + 1))), sequence)


def FIT(sequence: list) -> Fraction:
    return OP(sequence).value(Fraction(len(sequence) + 1))


def solve() -> int:
    sequence = [Fraction(un(k)) for k in range(1, 11)]
    FITs = [FIT(sequence[0:k]) for k in range(1, 11)]
    return int(sum(FITs))


if __name__ == '__main__':
    print(solve())

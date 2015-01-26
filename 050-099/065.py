import functools
import fractions

sequence = [2] + list(functools.reduce(lambda a, b: a+b, [[1, 2*k, 1] for k in range(1, 100)]))
sequence = list(map(lambda x: fractions.Fraction(x), sequence))
sequence = list(reversed(sequence[:100]))

add = lambda a, b: 1/a + b

fraction = functools.reduce(add, sequence)

print("La somme des chiffres du numérateur vaut:", sum(list(map(lambda x: int(x), str(fraction.numerator)))))
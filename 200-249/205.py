import itertools
import fractions

def dice(faces, number):
    probabilities = {k: 0 for k in range(number, number * faces + 1)}
    for results in itertools.product(range(1, faces+1), repeat=number):
        probabilities[sum(results)] += fractions.Fraction(1, faces**number)
    return probabilities

dices = [dice(6, 6), dice(4, 9)]

probability = 0

for i in range(6, 37):
    for j in range(9, 37):
        if j <= i:
            continue
        probability += dices[0][i] * dices[1][j]

print(round(float(probability), 7), probability)
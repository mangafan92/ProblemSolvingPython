import fractions

# Ne retourne qu'une liste de fractions < 3/7 avec le plus grand numérateur pour chaque dénominateur de [1, dmax]
def orderedFractions(dmax):
    output = list()
    for d in range(1, dmax+1):
        for k in range(3*d // 7, 0, -1):
            if fractions.gcd(k, d) > 1:
                continue
            else:
                output.append(fractions.Fraction(k, d))
                break

    output.sort()
    return output

fractions = orderedFractions(1000000)
print(fractions[len(fractions)-2], fractions[-1])

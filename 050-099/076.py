def decompose(number):
    decompositionsDict = [dict() for k in range(number+1)]

    def decomposeRecur(number, limit):
        try:
            return decompositionsDict[number][limit]
        except:
            decompositions = 0
            for k in range(1, limit+1):
                if number - k == 0:
                    decompositions += 1
                elif number - k >= 0:
                    decompositions += decomposeRecur(number - k, k)
            decompositionsDict[number][limit] = decompositions
            return decompositions

    return decomposeRecur(number, number-1)

print(decompose(100))
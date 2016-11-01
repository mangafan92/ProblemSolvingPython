import copy

def decompose(number, elements):
    elements = list(copy.copy(elements))
    elements.sort()
    elements.reverse()
    elements = tuple(elements)

    def decomposeRecur(number, elements):
        decompositions = 0
        for k in range(len(elements)):
            if number - elements[k] == 0:
                decompositions += 1
            elif number - elements[k] >= 0:
                decompositions += decomposeRecur(number - elements[k], elements[k:])
        return decompositions

    return decomposeRecur(number, elements)

elements = (200, 100, 50, 20, 10, 5, 2, 1)
print(decompose(200, elements))
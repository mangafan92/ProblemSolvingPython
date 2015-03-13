n = 15
decompositions = dict()

def decompose(n):
    def decomposeRecur(n):
        try:
            return decompositions[n]
        except:
            if n == 1:
                return 0
            elif n == 2:
                return 1
            elif n%2==0:
                return 1 + decomposeRecur(n//2)
            else:
                maximums = list()
                for k in range(1, n):
                    if ((n-k)/k)%2 == 0:
                        maximums.append(k)
                a = lambda k: decomposeRecur(n-k) + 1
                decompositions[n] = min(map(a, maximums))
                return decompositions[n]
    return decomposeRecur(n)

print(decompose(15))
print(decompositions)

print(sum([decompose(k) for k in range(1, 201)]))
print(decompositions)
print(decompose(119))
number = 10

decompose = lambda n: [[k, n-k] for k in range(1, n//2+1)]

sums = decompose(number)

for k in range(number):
    for sum in sums:
        for decomposition in decompose(sum[-1]):
            tmpSum = sorted(sum[:len(sum) - 1] + decomposition)
            if not tmpSum in sums:
                sums.append(tmpSum)

print(sums)
print(len(sums))
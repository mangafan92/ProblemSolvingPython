def digitsum(number):
    number = str(number)
    sum = 0
    for figure in number:
        sum += int(figure)
    return sum


limit = 100
maxsum = 0

for a in range(limit+1):
    for b in range(limit+1):
        maxsum = max(maxsum, digitsum(a**b))

print("La plus grande somme est:", maxsum)

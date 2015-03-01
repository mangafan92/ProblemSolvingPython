import itertools

def decimal(number):
    number = list(reversed(number))
    result = 0
    for k in range(len(number)):
        result += number[k]*10**k
    return result

def isReversible(number):
    reversedNumber = list(reversed(number))
    number = decimal(number) + decimal(reversedNumber)
    power = 0
    while number // (10**power) > 0:
        if number // (10**power) % 2 == 0:
            return False
        power += 1
    return True

reversibles = 0

for k in range(8):
    for part1 in itertools.product(range(1, 10), repeat=2):
        for part2 in itertools.product(range(10), repeat=k):
            number = (part1[0],) + part2 + (part1[1],)
            if isReversible(number):
                print(number, reversibles)
                reversibles += 1

print(reversibles)
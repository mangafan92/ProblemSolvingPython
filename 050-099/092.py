def nextTerm(number):
    return sum([int(x)**2 for x in str(number)])

def isValid(number):
    if not number in (1, 89):
        return isValid(nextTerm(number))
    else:
        return number == 89

numbers = 0

for k in range(1, 10**7):
    if isValid(k):
        # print(k)
        numbers += 1

print(numbers)
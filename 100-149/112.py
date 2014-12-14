def isbouncy(number):
    return not (isincreasing(number) or isdecreasing(number))

def isincreasing(number):
    number = str(number)
    for k in range(len(number)-1):
        if int(number[k]) > int(number[k+1]):
            return False
    return True

def isdecreasing(number):
    number = str(number)
    for k in range(len(number)-1):
        if int(number[k]) < int(number[k+1]):
            return False
    return True

k = 1
bouncy = 0
percentage = 0.99

while percentage*k > bouncy:
    k += 1
    if isbouncy(k):
        bouncy += 1

print(k)
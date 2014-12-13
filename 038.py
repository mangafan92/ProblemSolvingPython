import math

def isPandigital(number):
    number = str(number)
    figures = list(range(1,10))
    if len(number) != 9:
        return False

    for figure in figures:
        if not str(figure) in number:
            return False

    return True

limit = 10**9
pandigitals = list()

for k in range(1, 10**5):
    tmpstring = ""
    for i in range(1, limit):
        tmpstring += str(k*i)
        if isPandigital(tmpstring):
            pandigitals.append(tmpstring)
        if len(tmpstring) > 9:
            break

print("Le plus grand pandigital qui vérifie cette propriété est:", max(pandigitals))
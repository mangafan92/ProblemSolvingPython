from fractions import gcd

fractions = list()

deleteDigit = lambda x, k: int(str(x).replace(str(k), ""))

def isDigitCancellingFraction(fraction):
    digits = set()
    for k in range(0, 2):
        digits.add(fraction[k]//10)
        digits.add(fraction[k]%10)

    try:
        digits.remove(0)
    except:
        pass

    for k in digits:
        try:
            if deleteDigit(fraction[0], k) / deleteDigit(fraction[1], k) == fraction[0]/fraction[1]:
                return True
        except:
            pass

    return False

for i in range(10, 100):
    for j in range(10, i):
        fractions.append((j, i))

digitCancelling = list(filter(isDigitCancellingFraction, fractions))

numerator = 1
denominator = 1

for k in range(len(digitCancelling)):
    numerator *= digitCancelling[k][0]
    denominator *= digitCancelling[k][1]

print(denominator // gcd(numerator, denominator))





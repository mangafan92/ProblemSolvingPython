def memesDigits(x, y):
    x = str(x)
    y = str(y)
    for k in range(0, len(x)):
        if not x[k] in y:
            return False
    for k in range(0, len(y)):
        if not y[k] in x:
            return False
    return True

def memesDigitsMultiples(x, borne):
    for k in range(2, borne+1):
        if not memesDigits(x, x*k):
            return False
    return True
n = 1

while not memesDigitsMultiples(n, 6):
    n += 1
    
print("Le premier nombre est", n, ".")
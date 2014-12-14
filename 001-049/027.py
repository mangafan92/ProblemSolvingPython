def estPremier(n):
    if n < 0:
        n = -n
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True
    
def nombreTermesPremiers(a, b):
    n = 0
    while estPremier(n**2+a*n+b):
        n += 1
    return n

A = 0
B = 0
nbr = 1

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        nombreTermes = nombreTermesPremiers(a, b)     
        if nombreTermes > nbr:
            A = a
            B = b
            nbr = nombreTermes
print("Les coefficients sont a=", A, "et b=", B, "et leur produit vaut", A*B, ".")
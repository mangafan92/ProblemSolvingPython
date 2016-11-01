def estPremier(n):
    if n == 1:
        return False
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True
    
def estDecomposable(n):
    k = 1
    
    while n - 2*k**2 > 0 and not estPremier(n - 2*k**2):
        k += 1
        
    if n - 2*k**2 < 0:
        return False
    else:     
        return True
        
n = 3

while estDecomposable(n) or estPremier(n):
    n += 2
    
print(n)
        
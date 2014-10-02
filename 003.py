def estPremier(n):
    for k in range(2, int(n**(1/2))):
        if n % k == 0:
            return False
    return True
    
n = 600851475143
k=2

while k < n**(1/2):
    if n % k == 0:
        n /= k
    else:
        k+=1

print(n, estPremier(n))
def estPremier(n):
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True

borne = int(input("Nombre:"))    
n = 1
k = 0

while k < borne:
    n+=1    
    if estPremier(n):
        k += 1

print("Le", k, "-ième nombre premier est", n)
def estPremier(n):
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True
    
borne = int(input("Nombre:"))
s = 0

for k in range(2, borne+1):
    if estPremier(k):
        s += k
    
print("La somme des nombres premiers inférieurs à", borne, "est", s, ".")
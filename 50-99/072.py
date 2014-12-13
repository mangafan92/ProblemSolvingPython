def PGCD1(a, b):   
    if a % b == 0:
        return m
    elif a > b:
        return PGCD(n % m, m)
    elif a  < b:
        return PGCD(m % n, n)
        
def PGCD2(a, b):
    while a % b != 0:
        r = a % b
        a = b
        if r != 0:
            b = r
    return b
    
def estPremier(n, listePremiers):
    k = 0    
    while k < len(listePremiers):
        if n % listePremiers[k] == 0:
            return False
        k+= 1
    return True
    
def genererListeNombresPremiers(borne):
    liste = [2]
    for k in range(3, borne+1):
        if estPremier(k, liste):
            liste.append(k)
    return liste   

def decompositionFacteursPremiers(n, listePremiers):
     k = 0
     liste = []
     while n > 1:
         if n % listePremiers[k] == 0:
             n //= listePremiers[k]
             if not listePremiers[k] in liste:
                 liste.append(listePremiers[k])
         else:
             k += 1
     return liste

nombreFractions = 0
decompositions = []

listePremiers = genererListeNombresPremiers(10**5)

#for k in range(0, 101):
#    decompositions.append(decompositionFacteursPremiers(k, listePremiers))
#
#for i in range(2, 1000000):
#    for j in range(1, i):
#        if sontPremiersEntreEux(i, j, liste):
#            nombreFractions += 1
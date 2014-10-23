from time import time

def estPandigital(n):
    n = str(n)
    for k in range(1, len(n)+1):
        if not str(k) in n:
            return False
    return True
 
debut = time()
   
x = 1
liste = []

while x**2 < 10**9:
    y = x+1
    chaine = str(x)+str(y)+str(x*y)
    while len(chaine) < 10:
        if estPandigital(chaine) and len(chaine) == 9 and not x*y in liste:        
            liste.append(x*y)
        y += 1
        chaine = str(x)+str(y)+str(x*y)
    x += 1
    
somme = 0

for nombre in liste:
    somme += nombre

print("La somme des tous les produits dont l'identité est un nombre pandigital à 9 digits vaut {}.".format(somme))
    
print("\nL'algorithme a mis {}s à s'exécuter.".format(round(time()-debut, 2)))
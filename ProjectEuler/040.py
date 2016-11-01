chaine = ""
k = 1

while len(chaine) < 10**6:
    chaine += str(k)
    k += 1

produit = 1
    
for k in range(0, 7):
    produit *= int(chaine[10**k-1])
    
print("Le produit vaut", produit, ".")
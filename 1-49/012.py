def nombreDiviseurs(n):
    diviseurs = 0
    for k in range(1, n+1):
        if n%k == 0:
            diviseurs += 1
    return diviseurs
    
borne = int(input("Nombre:"))
k = 0
n = 0

while n < borne:
# Le nombre de diviseurs de n(n-1)/2 est égal au produits du nombre de diviseurs de n/2 et de n+1 ou de n et (n+1)/2 car n et n+1 n'ont aucun facteur premier en commun    
    if k % 2 == 0:
        n = nombreDiviseurs(int(k/2)*nombreDiviseurs(k+1))
    else:
        n = nombreDiviseurs(k)*nombreDiviseurs(int((k+1)/2))
    k += 1
  
k -= 1  
print("Le premier nombre triangulaire à avoir plus de", borne, "diviseurs est", int(k*(k+1)/2), ".")
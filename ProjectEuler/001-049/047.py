from time import time

def nombrePremier(n, listeNombresPremiers):
    if n > len(listeNombresPremiers)-1:
        k = listeNombresPremiers[len(listeNombresPremiers)-1]+1
        while len(listeNombresPremiers) < n+1:
            if estPremier(k, listeNombresPremiers):
                listeNombresPremiers.append(k)
            k += 1
    return listeNombresPremiers[n]
            
def estPremier(nombre, liste):
    for k in range(0, len(liste)):
        if nombre % liste[k] == 0:
            return False
    return True
    
def decompositionFacteursPremiers(nombre, liste):
    decomposition = []
    k = 0
    while nombre > 1:
        if nombre % nombrePremier(k, liste) == 0: 
            nombre //= nombrePremier(k, liste)
            if not nombrePremier(k, liste) in decomposition:
                decomposition.append(nombrePremier(k, liste))
        else:
            k += 1
    return decomposition
    
def longueurDecompositionsSuperieurA(nombre, decompositions):
    for element in decompositions:
        if len(element) < nombre:
            return False
    return True

borne = int(input("Nombre:"))
debut = time()
listePremiers = [2]
listeDecompositions = []

# Initialisation tableau décompositions
for k in range(2, 2+borne):
    listeDecompositions.append(decompositionFacteursPremiers(k, listePremiers))
  
nombre = 2+borne-1
  
while not longueurDecompositionsSuperieurA(borne, listeDecompositions):
    nombre += 1    
    for k in range(0, borne-1):
        listeDecompositions[k] = listeDecompositions[k+1]
    listeDecompositions[borne-1] = decompositionFacteursPremiers(nombre, listePremiers)

print("\nLe premier nombre de la série de {} nombres consécutifs ayant {} facteurs premiers distincts est {}.".format(borne, borne, nombre-borne+1))
print("\nL'algorithme a mis {}s à s'exécuter.".format(round(time()-debut, 2)))
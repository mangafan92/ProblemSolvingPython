from time import time

def reorganiser(elements, liste, debut, apparitionsMultiples, longueur):
    if longueur == 1 and len(elements) == 1:
        liste.append(debut + elements[0])
    elif longueur == 1:
        for k in range(0, len(elements)):
            sortie = debut + elements[k]
            liste.append(sortie)
    else:
        for k in range(0, len(elements)):         
            debutTemp = debut
            elementsTemp = list(elements)
            
            debutTemp += elementsTemp[k]
            
            if apparitionsMultiples == False:
                elementsTemp.remove(elements[k])
            reorganiser(elementsTemp, liste, debutTemp, apparitionsMultiples, longueur-1)
            
def annagramme(elements, apparitionsMultiples, longueur):
    liste = []
    debut = ""
    reorganiser(elements, liste, debut, apparitionsMultiples, longueur) 
    return liste
    
debut = time()

elements = ""
for k in range(0, 10):
    elements += str(k)

liste = annagramme(elements, False, 10)
liste.sort()

print("La millionième permutation lexicographique des chiffres allant de 0 à 9 est {}.".format(liste[10**6-1]))

print("\nL'algorithme a mis {}s à s'exécuter.".format(round(time()-debut, 2)))
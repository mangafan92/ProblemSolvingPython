def estPremier(n):
    n = int(n)    
    if n == 1:
        return False
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True

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
    
liste = []

for k in range(2, 9):
    elements = []
    for k in range(1, k):
        elements.append(str(k))
    
    liste += annagramme(elements, False, len(elements))

listePremiers = []

for k in range(0, len(liste)):
    if estPremier(liste[k]):
        listePremiers.append(liste[k])
        
listePremiers.sort()

print("Le plus grand nombre premier pandigital est ", listePremiers[len(listePremiers)-1], ".", sep="")
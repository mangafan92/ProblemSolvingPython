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
    
elements = ""
for k in range(0, 10):
    elements += str(k)

liste = annagramme(elements, False, 10)
somme= 0

for element in liste:
    if int(element[1:4])%2 == 0 and int(element[2:5])%3 == 0 and int(element[3:6])%5 == 0 and int(element[4:7])%7 == 0 and int(element[5:8])%11 == 0 and int(element[6:9])%13 == 0 and int(element[7:10])%17 == 0:
        somme += int(element)

print(somme)
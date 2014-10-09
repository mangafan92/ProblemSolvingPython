def estPremier(n):
    n = int(n)    
    if n == 1:
        return False
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True

def reorganiser(elements, liste, debut):
    if len(elements) == 1:
        liste.append(debut + elements[0])
    else:
        for k in range(0, len(elements)):
            elementsTemp = list(elements)
            debutTemp = debut           
            debutTemp += elements[k]
            elementsTemp.remove(elements[k])
            
            reorganiser(elementsTemp, liste, debutTemp)
        
            
liste = []
elements = []
for k in range(1, 8):
    elements.append(str(k))
    
debut = ""

reorganiser(elements, liste, debut)

listePremiers = []

for k in range(0, len(liste)):
    if estPremier(liste[k]):
        listePremiers.append(liste[k])
        
listePremiers.sort()

print(listePremiers)
def genererListeTripletsPytagore(borne):
    liste = []
    for k in range(1, borne+1):
        for i in range(k, borne+1):
            c = (k**2+i**2)**(1/2)
            if int(c) == c:
                liste.append([k, i, int(c), int(i+k+c)])             
    return liste
    
def nombreMaximum(liste, borne):
    listeOcur = [0]*(borne+1)
    for element in liste:
        if element[3] <= borne:
            listeOcur[element[3]] += 1
    maxi = 0
    for k in range(0, borne+1):
        if listeOcur[k] > listeOcur[maxi]:
            maxi = k            
    return maxi

borne = int(input("Nombre:"))   
liste = genererListeTripletsPytagore(borne)
print("Le périmètre de triangle rectangle inférieur à", borne, "qui permet d'avoir le plus de combinaisons de longueurs entières de côtés possibles est", nombreMaximum(liste, borne), ".")
def triangulaire(n):
    return int(n*(n+1)/2)

def listeTriangulaire(n):
    liste = []    
    for k in range(1, n+1):
        liste.append(triangulaire(k))
    return liste
    
def scoreMot(mot):
    lettres = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    score = 0    
    for k in range(0, len(mot)):
        score += lettres.index(mot[k])+1
    return score
    
with open("./données/042_words.txt") as fichier:
    fichier = fichier.read()
    fichier = fichier.split(",")
    for k in range(0, len(fichier)):
        fichier[k] = fichier[k][1:len(fichier[k])-1]
        
    listeTriangulaire = listeTriangulaire(100)
    
    nombreMotsTriangulaires = 0
    
    for k in range(0, len(fichier)):       
        if scoreMot(fichier[k]) in listeTriangulaire:
            nombreMotsTriangulaires += 1
            
    print("Il y a", nombreMotsTriangulaires, "mots triangulaires dans la liste.")
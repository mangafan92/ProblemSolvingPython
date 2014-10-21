def scoreMot(mot):
    lettres = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    score = 0    
    for k in range(0, len(mot)):
        score += lettres.index(mot[k])+1
    return score
    
with open("./données/022_names.txt") as fichier:
    fichier = fichier.read()
    fichier = fichier.split(",")
    for k in range(0, len(fichier)):
        fichier[k] = fichier[k][1:len(fichier[k])-1]
        
    fichier.sort()
    
    sommeScores = 0
    
    for k in range(0, len(fichier)):       
        sommeScores += (k+1)*scoreMot(fichier[k])
    
    print("La sommes des scores vaut", sommeScores, ".")
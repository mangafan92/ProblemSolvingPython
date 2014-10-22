def nCr(n, r, listeFactorielles):
    return listeFactorielles[n]/listeFactorielles[r]/listeFactorielles[n-r]
    
def genererListeFactorielles(n):
    liste = [1]
    for n in range(1, n+1):
        liste.append(liste[len(liste)-1]*n)
    return liste

borne = 100
listeFactorielles = genererListeFactorielles(borne)
k = 0
  
for n in range(1, borne+1):
    for r in range(1, n+1):
        if nCr(n, r, listeFactorielles) > 10**6:
            k += 1
            
print("Il y a", k, "coefficients.")
def genererListeDiviseurs(n):
    liste = []    
    for k in range(1, n):
        if n % k == 0:
            liste.append(k)
    return liste

def sommeDiviseurs(n):
    listeDiviseurs = genererListeDiviseurs(n)
    s = 0
    for element in listeDiviseurs:
        s += element
    return s

def genererListeNombresAbondants(borne):
    liste = []    
    for k in range(1, borne+1):
        if k < sommeDiviseurs(k):
            liste.append(k)
            print(k)
    return liste
    
def genererSommeAbondants(listeAbondants):
    liste = []
    for k in range(0, len(listeAbondants)):
        for i in range(k, len(listeAbondants)):
            if not listeAbondants[i]+listeAbondants[k] in liste:
                liste.append(listeAbondants[i]+listeAbondants[k])
                print(listeAbondants[i]+listeAbondants[k])
    return liste
    
sommes = genererSommeAbondants(genererListeNombresAbondants(28123))

s = 0

for k in range(0, 28124):
    if not k in sommes:
        s += k
        
print(s)    
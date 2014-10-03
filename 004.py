def estPalindrome(n):
    n = str(int(n))
    p = len(n) - 1
        
    for k in range(0, p):        
        if n[k] != n[p-k]:
            return False
            
    return True

reponse = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if estPalindrome(i*j) and i*j > reponse:
            reponse = i*j
            facteur1 = i
            facteur2 = j

print("Le plus grand nombre premier facteur de 2 nombres de 3 chiffres est", reponse, "qui est facteur de", facteur1, "et", facteur2,".")
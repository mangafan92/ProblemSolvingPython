def estPalindrome(n):
    n = str(n)
    p = len(n) - 1
        
    for k in range(0, p):        
        if n[k] != n[p-k]:
            return False
            
    return True

s = 0
borne = int(input("Nombre:"))
    
for k in range(0, borne):
    binaire = bin(k)
    binaire = binaire[2:len(binaire)]
    if estPalindrome(k) and estPalindrome(binaire):
        s += k
print("La somme de tous les nombres étant des palindromes lorsqu'ils sont écrit en binaire et en décimal inférieurs à", borne,"est", s, ".")
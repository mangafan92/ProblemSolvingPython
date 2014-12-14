def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorielle(n-1)
        
nombre = int(input("Nombre:"))
factorielle = str(factorielle(nombre))
s = 0

for k in range(0, len(factorielle)):
    s += int(factorielle[k])
    
print(nombre, "factorielle est égal à", factorielle, "et la somme des chiffres qui le composent est", s, ".")
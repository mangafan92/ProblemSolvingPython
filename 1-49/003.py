n = int(input("Nombre:"))
p = n
k = 2

while p > 1:    
    if p % k == 0:
        p //= k
    else:
        k += 1

print("Le plus grand diviseur premier de", n, "est", k)

# Le plus petit diviseur positif et supérieur à 1 d'un nombre est un nombre premier.
# Lorsque l'on divise p par k, k est le plus petit diviseur de p donc k est premier.
# De plus, la valeur de k augmente au fur et à mesure de l'exécution du programme, la dernière valeur prise par k est donc la plus grande qu'il prend.
# Elle est par conséquent le plus grand diviseur premier de n.
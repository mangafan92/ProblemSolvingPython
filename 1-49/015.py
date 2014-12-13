def nombreRoutes(a, b, table):
    if table[a][b] != 0:
        return table[a][b]
    else:
        if a == 0 or b == 0:
            return 1
        out = nombreRoutes(a-1, b, table) + nombreRoutes(a, b-1, table)
        table[a][b] = out
        return out

nombre = int(input("Nombre:"))

grid = []
for k in range(0,nombre+1):
    grid.append([0]*(nombre+1))

print("Le nombre de chemins différents qui permettent d'aller d'un coin au point opposé d'un carré de", nombre, "cotés est", nombreRoutes(nombre, nombre, grid), ".")
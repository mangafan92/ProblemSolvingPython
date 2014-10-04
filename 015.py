def nombreRoutes(a, b, table):
    if table[a][b] != 0:
        return table[a][b]
    else:
        if a == b:
            out = 2*nombreRoutes(a, b-1, table)
            table[a][b] = out             
            return out
        if a == 0 or b == 0:
            return 1
        out = nombreRoutes(a-1, b, table) + nombreRoutes(a, b-1, table)
        table[a][b] = out
        return out

grid = []
for k in range(0,21):
    grid.append([0]*21)

print(nombreRoutes(20,20, grid))
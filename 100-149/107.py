"""
    Principe:
        - on applique l'algorithme de Prim au graphe https://fr.wikipedia.org/wiki/Algorithme_de_Prim
        - ici, on a gardé la représentation originale du problème pour représenter le graphe de sortie, soit un tableau de valeurs des arêtes, avec pour convention que coût vaut 0 lorqu'aucune arête ne relie les sommets
"""


def contentToGraph(content: str) -> list:
    lines = content.splitlines()
    splitline = lambda line: line.split(",")
    lines = list(map(splitline, lines))
    toInt = lambda s: int(s) if s != "-" else 0
    lineToInt = lambda line: list(map(toInt, line))
    return list(map(lineToInt, lines))


def primAlgorithm(graph: list, start: int) -> list:
    visited = [False for i in range(len(graph))]
    visited[start] = True

    minimalGraph = [[0 for j in range(len(graph))] for i in range(len(graph))]

    expansionPossible = {(graph[start][i], (start, i)) for i in range(len(graph))}

    while expansionPossible:
        cost, (p1, p2) = min(expansionPossible)
        expansionPossible.remove((cost, (p1, p2)))

        if not visited[p2] and cost > 0:
            visited[p2] = True
            minimalGraph[p1][p2] = minimalGraph[p2][p1] = graph[p1][p2]
            expansionPossible = expansionPossible.union({(graph[p2][i], (p2, i)) for i in range(len(graph))})

    return minimalGraph


def solve():
    filename = "./data/107_network.txt"
    file = open(filename, "r")
    content = file.read()
    graph = contentToGraph(content)
    minimalGraph = primAlgorithm(graph, 0)
    return (sum([sum(e) for e in graph]) - sum([sum(e) for e in minimalGraph])) // 2


if __name__ == '__main__':
    print(solve())

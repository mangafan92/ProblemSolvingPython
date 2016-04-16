"""
Principe:
    - 2 méthodes sont implémentées ici:
        - M1:
            - on simule une partie aléatoire
            - on débute à la case 0, et on simule n lancers de dés en notant les casees par lesquelles on passe
            - en prenant n assez grand (n= 10^6 par exemple), on peut classer les cases par ordre de probabilité de visite en regardant le nombre de visites de chaque case durant la simulation
        - M2:
            - on calcule un tableau dont la case (c, d, c', d') contient la probabilité de partir de la case c en étant dans une série de d doubles et d'arriver dans la case c' en étant dans une série de d' doubles
            - on en déduit la probabilité que, après n tours, on soit dans la case c en étant dans une série d doubles si au tour 1 on était à la case départ dans une série de 0 doubles
            - cette probabilité converge quand n devient grand
            - il suffit de prendre n=300 et on a une précision suffisante pour classer les cases par ordre de probabilité de visite
            - on note qu'avec cette méthode on ne choisit les cartes piochées au hasard et on ignore complètement la règle qui consiste à mettre la carte piochée au fond du paquet sans remélanger -> ça ne change rien
"""

import enum
import itertools
import random


class SquareType(enum.Enum):
    GO = 0
    Normal = 1
    CommunityChest = 2
    Chance = 3
    RailwayCompany = 4
    UtilityCompany = 5
    GoToJail = 6
    Jail = 7


monopolyBoard = [
    SquareType.GO,
    SquareType.Normal,
    SquareType.CommunityChest,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.RailwayCompany,
    SquareType.Normal,
    SquareType.Chance,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.Jail,
    SquareType.Normal,
    SquareType.UtilityCompany,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.RailwayCompany,
    SquareType.Normal,
    SquareType.CommunityChest,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.Chance,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.RailwayCompany,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.UtilityCompany,
    SquareType.Normal,
    SquareType.GoToJail,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.CommunityChest,
    SquareType.Normal,
    SquareType.RailwayCompany,
    SquareType.Chance,
    SquareType.Normal,
    SquareType.Normal,
    SquareType.Normal,
]


def nextType(monopolyBoard: list, square: int, type: SquareType) -> int:
    while monopolyBoard[square] != type:
        square += 1
        square %= len(monopolyBoard)
    return square


# M1

def simulation(monopolyBoard: list, throws: int, sides: int) -> list:
    res = [0 for k in range(len(monopolyBoard))]
    square = 0
    doubles = 0
    cc = list(range(16))
    ch = list(range(16))
    random.shuffle(cc)
    random.shuffle(ch)

    for k in range(throws):
        res[square] += 1
        square, doubles, cc, ch = nextSimulationState(monopolyBoard, square, doubles, cc, ch, sides)

    return list(reversed(sorted(range(len(monopolyBoard)), key=lambda k: res[k])))


def nextSimulationState(monopolyBoard: list, square: int, doubles: int, cc: list, ch: list, sides: int) -> (int, int, list, list):
    d1, d2 = random.randrange(1, sides + 1), random.randrange(1, sides + 1)
    nextDoubles = doubles + 1 if d1 == d2 else 0
    nextSquare = (square + d1 + d2) % len(monopolyBoard)
    nextcc = cc
    nextch = ch

    if nextDoubles == 3 or monopolyBoard[nextSquare] == SquareType.GoToJail:
        nextSquare = monopolyBoard.index(SquareType.Jail)
        nextDoubles = 0

    if monopolyBoard[nextSquare] == SquareType.Chance:
        card = ch[0]
        nextch = ch[1:] + [ch[0]]
        if card == 1:  # Go to GO
            nextSquare = monopolyBoard.index(SquareType.GO)
        elif card == 2:  # Go to Jail
            nextSquare = monopolyBoard.index(SquareType.Jail)
            nextDoubles = 0
        elif card == 3:  # Go to C1
            nextSquare = 11
        elif card == 4:  # Go to E3
            nextSquare = 24
        elif card == 5:  # Go to H2
            nextSquare = 39
        elif card == 6:  # Go to R1
            nextSquare = 5
        elif card in (7, 8):  # Go to next R
            nextSquare = nextType(monopolyBoard, nextSquare, SquareType.RailwayCompany)
        elif card == 9:  # Go to U
            nextSquare = nextType(monopolyBoard, nextSquare, SquareType.UtilityCompany)
        elif card == 10:  # Go back 3 squares
            nextSquare = (nextSquare - 3) % len(monopolyBoard)

    if monopolyBoard[nextSquare] == SquareType.CommunityChest:
        card = cc[0]
        nextcc = cc[1:] + [cc[0]]

        if card == 1:  # Go to GO
            nextSquare = monopolyBoard.index(SquareType.GO)
        elif card == 2:  # Go to Jail
            nextSquare = monopolyBoard.index(SquareType.Jail)
            nextDoubles = 0

    return nextSquare, nextDoubles, nextcc, nextch


def solveM1(sides: int = 4, throws: int = 10 ** 6) -> str:
    beg = simulation(monopolyBoard, throws, sides)[:3]
    beg = [str(e) for e in beg]
    beg = ["0" + e if len(e) == 1 else e for e in beg]
    return "".join(beg)


# M2



def probabilitiesFromSquare(monopolyBoard: list, square: int, doubles: int, sides: int) -> int:
    p = [[0 for k in range(3)] for square in range(len(monopolyBoard))]
    for d1, d2 in itertools.product(range(1, sides + 1), repeat=2):
        nextDoubles = doubles + 1 if d1 == d2 else 0
        nextSquare = (square + d1 + d2) % len(monopolyBoard)
        if nextDoubles == 3 or monopolyBoard[nextSquare] == SquareType.GoToJail:
            p[monopolyBoard.index(SquareType.Jail)][0] += 1 / sides ** 2
        elif monopolyBoard[nextSquare] == SquareType.CommunityChest:
            p[monopolyBoard.index(SquareType.GO)][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to GO
            p[monopolyBoard.index(SquareType.Jail)][0] += 1 / 16 * 1 / sides ** 2  # Go to Jail
            p[nextSquare][nextDoubles] += 14 / 16 * 1 / sides ** 2  # Stay
        elif monopolyBoard[nextSquare] == SquareType.Chance:
            p[monopolyBoard.index(SquareType.GO)][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to GO
            p[monopolyBoard.index(SquareType.Jail)][0] += 1 / 16 * 1 / sides ** 2  # Go to Jail
            p[11][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to C1
            p[24][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to E3
            p[39][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to H2
            p[5][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to R1
            p[nextType(monopolyBoard, nextSquare, SquareType.RailwayCompany)][nextDoubles] += 2 / 16 * 1 / sides ** 2  # Go to next R
            p[nextType(monopolyBoard, nextSquare, SquareType.UtilityCompany)][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go to next U
            if monopolyBoard[(nextSquare - 3) % len(monopolyBoard)] != SquareType.CommunityChest:
                p[(nextSquare - 3) % len(monopolyBoard)][nextDoubles] += 1 / 16 * 1 / sides ** 2  # Go back 3 squares
            else:
                p[monopolyBoard.index(SquareType.GO)][nextDoubles] += 1 / 16 * 1 / 16 * 1 / sides ** 2  # Go to GO
                p[monopolyBoard.index(SquareType.Jail)][0] += 1 / 16 * 1 / 16 * 1 / sides ** 2  # Go to Jail
                p[(nextSquare - 3) % len(monopolyBoard)][nextDoubles] += 1 / 16 * 14 / 16 * 1 / sides ** 2  # Stay
            p[nextSquare][nextDoubles] += 6 / 16 * 1 / sides ** 2  # Stay
        else:
            p[nextSquare][nextDoubles] += 1 / sides ** 2

    return p


def nextDistribution(monopolyBoard: list, current: list, probabilities: list):
    next = [[0 for k in range(3)] for square in range(len(monopolyBoard))]
    for square in range(len(monopolyBoard)):
        for doubles in range(3):
            for nextSquare in range(len(monopolyBoard)):
                for nextDoubles in range(3):
                    next[nextSquare][nextDoubles] += current[square][doubles] * probabilities[square][doubles][nextSquare][nextDoubles]
    return next


def distribution(monopolyBoard: list, sides: int, throws: int):
    probabilities = [[probabilitiesFromSquare(monopolyBoard, square, doubles, sides) for doubles in range(0, 3)] for square in range(len(monopolyBoard))]
    dist = [[0 for k in range(3)] for square in range(len(monopolyBoard))]
    dist[0][0] = 1

    for k in range(throws):
        dist = nextDistribution(monopolyBoard, dist, probabilities)

    return [sum(dist[i][j] for j in range(len(dist[i]))) for i in range(len(monopolyBoard))]


def solveM2(sides: int = 4, throws: int = 300) -> str:
    dist = distribution(monopolyBoard, sides, throws)
    beg = list(reversed(sorted(range(len(monopolyBoard)), key=lambda k: dist[k])))[:3]
    beg = [str(e) for e in beg]
    beg = ["0" + e if len(e) == 1 else e for e in beg]
    return "".join(beg)


# M1,5


def solve(sides: int = 4) -> str:
    a = random.randrange(1)
    if a == 0:
        return solveM1(sides)
    else:
        return solveM2(sides)


if __name__ == '__main__':
    print(solve())

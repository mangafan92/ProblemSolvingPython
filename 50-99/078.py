def startrecur(coins):
    partition = []
    piles = []
    recur(coins, partition, piles)
    for pile in piles:
        pile.sort()
    cleanpiles(piles)
    return piles

def recur(coins, partition, piles):
    if coins > 0:
        for k in range(1, coins+1):
            tmppartition = list(partition)
            tmppartition.append(k)
            recur(coins-k, tmppartition, piles)
    else:
        piles.append(partition)

def cleanpiles(piles):
    tmppiles = list(piles)
    for pile in tmppiles:
        while piles.count(pile) > 1:
            piles.remove(pile)

piles = startrecur(7)
print(piles, len(piles))
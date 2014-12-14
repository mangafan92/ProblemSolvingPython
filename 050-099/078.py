# TODO

def startrecur(coins):
    partition = []
    piles = []
    recur(coins, piles)
    while not isover(piles, coins):
        for k in range(coins**2):
            recur(coins, piles)
        cleanpiles(piles)
    return piles

def recur(coins, piles):
    if not piles == []:
        for pile in piles:
            if sum(pile) < coins:
                for k in range(1, coins - sumpile(pile) + 1):
                    tmppile = list(pile)
                    tmppile.append(k)
                    piles.append(tmppile)
                piles.remove(pile)
                break
    else:
        for k in range(1, coins+1):
            piles.append([k])

def cleanpiles(piles):
    for pile in piles:
        pile.sort()
    tmppiles = list(piles)
    for pile in tmppiles:
        while piles.count(pile) > 1:
            piles.remove(pile)

def isover(piles, coins):
    for pile in piles:
        if sumpile(pile) < coins:
            return False
    return True

def sumpile(pile):
    sum = 0
    for number in pile:
        sum += number
    return sum

for k in range(4, 41):
    piles = startrecur(k)
    print(k, len(piles), piles)
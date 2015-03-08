class PokerHand:
    suitConversion = ["H", "D", "C", "S"]
    valueConversion = list(map(str, range(2, 10))) + ["T", "J", "Q", "K", "A"]

    def __init__(self, hand):
        self.hand = hand

    def values(self):
        return list(map(lambda l: l[0], self.hand))

    def suits(self):
        return list(map(lambda l: l[1], self.hand))

    def sortedHand(self):
        return list(reversed(sorted(self.hand, key=lambda l:l[0])))

    def highCard(self):
        return self.sortedHand()[0]

    def pairs(self):
        cards = self.values()
        pairs = set()
        for card in cards:
            if cards.count(card) == 2:
                pairs.add(card)
        return list(pairs)

    def isOnePair(self):
        return len(self.pairs()) == 1

    def isTwoPairs(self):
        return len(self.pairs()) == 2

    def isThreeOfAKind(self):
        cards = self.values()
        for card in cards:
            if cards.count(card) == 3:
                return True
        return False

    def isStraight(self):
        cards = self.values()
        cards = list(sorted(cards))
        for k in range(len(cards)-1):
            if cards[k]+1 != cards[k+1]:
                return False
        return True

    def isFlush(self):
        for k in range(1, len(self.hand)):
            if self.hand[0][1] != self.hand[k][1]:
                return False
        return True

    def isFullHouse(self):
        return self.isOnePair() and self.isThreeOfAKind()

    def isFourOfAKind(self):
        cards = self.values()
        for card in cards:
            if cards.count(card) == 4:
                return True
        return False

    def isStraightFlush(self):
        return self.isStraight() and self.isFlush()

    def isRoyalFlush(self):
        return self.isStraightFlush() and min(self.values()) == PokerHand.valueConversion.index("10")

    def getHandId(self):
        if self.isRoyalFlush():
            return 0
        if self.isStraightFlush():
            return 1
        if self.isFourOfAKind():
            return 2
        if self.isFullHouse():
            return 3
        if self.isFlush():
            return 4
        if self.isStraight():
            return 5
        if self.isThreeOfAKind():
            return 6
        if self.isTwoPairs():
            return 7
        if self.isOnePair():
            return 8
        return 9

    def __gt__(self, other):
        if self.getHandId() != other.getHandId():
            return self.getHandId() < other.getHandId()
        elif self.getHandId() in (7, 8):
            return max(self.pairs()) > max(other.pairs())
        else:
            return max(self.values()) > max(other.values())

    @staticmethod
    def convertHand(hand):
        hand = hand.split(" ")
        return list(map(PokerHand.convertCard, hand))

    @staticmethod
    def convertCard(card):
        return PokerHand.valueConversion.index(card[0]), PokerHand.suitConversion.index(card[1])

with open("./data/054_poker.txt", "r") as file:
    content = file.read()

def solveProblem(content=content):
    content = content.splitlines()
    content = list(map(lambda line: [line[:15].strip(" "), line[15:].strip(" ")], content))

    result = 0

    for hands in content:
        hands = PokerHand(PokerHand.convertHand(hands[0])), PokerHand(PokerHand.convertHand(hands[1]))
        if hands[0] > hands[1]:
            result += 1

    return result

if __name__ == '__main__':
    print(solveProblem())
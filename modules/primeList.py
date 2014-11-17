class PrimeList:
    def __init__(self):
        self.liste = [2]

    def get(self, n):
        if n > len(self.liste)-1:
            self.addPrimesToId(n)
        return self.liste[n]

    def addPrimesToId(self, n):
        while len(self.liste)-1 < n:
            self.addNextPrime()

    def addPrimeToNumber(self, n):
        while self.lastPrime() < n:
            self.addNextPrime()

    def addNextPrime(self):
        n = self.lastPrime()
        while not self.isNextPrime(n):
            n += 1
        self.liste.append(n)

    def isPrime(self, n):
        if n > self.lastPrime():
            self.addPrimeToNumber(n)
        return n in self.liste

    def isNextPrime(self, n):
        for number in self.liste:
            if n % number == 0:
                return False
        return True

    def lastPrime(self):
        return self.liste[len(self.liste)-1]
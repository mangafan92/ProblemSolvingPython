import os


class Primes(list):
    def __init__(self):
        list.__init__(self, [2])
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.file = self.dir + "/data/primes.txt"
        self.read()

    def get(self, n):
        while len(self) < n + 1:
            self.addNextPrime()
        return self[n]

    def addPrimesToId(self, n):
        while len(self) < n:
            self.addNextPrime()

    def addPrimeToNumber(self, n):
        while self.lastPrime() < n:
            self.addNextPrime()

    def addNextPrime(self):
        n = self.lastPrime() + 1
        while not self.isNextPrime(n):
            n += 1
        self.append(n)
        if len(self) % 5000 == 0:
            self.write()

    def isPrime(self, n):
        if n > self.lastPrime():
            self.addPrimeToNumber(n)
        return n in self

    def arePrimes(self, table):
        for n in table:
            if not self.isPrime(n):
                return False
        return True

    def isNextPrime(self, n):
        for number in self:
            if n % number == 0:
                return False
            elif number > n ** (1 / 2) + 1:
                break
        return True

    def lastPrime(self):
        return self[len(self) - 1]

    def firstAbove(self, n):
        i = 0
        while self.get(i) <= n:
            i += 1
        return i

    def range(self, n, m):
        output = []
        for k in range(n, m):
            output.append(self[k])
        return output

    def read(self):
        try:
            if not os.path.isfile(self.file):
                raise FileNotFoundError
            file = open(self.file)
            content = file.read()
            list.__init__(self, content.splitlines())

            for k in range(len(self)):
                self[k] = int(self[k])

            if len(self) == 0:
                list.__init__(self, [2])

        except (ValueError, FileNotFoundError):
            print("Fichier primes.txt non trouvé.")
            list.__init__(self, [2])
            self.write()

    def write(self):
        datadir = self.dir + "/data"
        if not os.path.isdir(datadir) and not os.path.isfile(datadir):
            os.mkdir(datadir)
        with open(self.file, "w") as file:
            output = ""
            for n in self:
                output += str(n) + "\n"
            file.write(output)
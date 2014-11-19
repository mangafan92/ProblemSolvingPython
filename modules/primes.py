import os.path
import os

class Primes:
    def __init__(self):
        self.primes = [2]
        self.file = "./data/primes.txt"
        self.read()

    def get(self, n):
        while len(self.primes) < n+1:
            self.addNextPrime()
        return self.primes[n]


    def addPrimesToId(self, n):
        while len(self.primes) < n:
            self.addNextPrime()

    def addPrimeToNumber(self, n):
        while self.lastPrime() < n:
            self.addNextPrime()

    def addNextPrime(self):
        n = self.lastPrime()+1
        while not self.isNextPrime(n):
            n += 1
        self.primes.append(n)
        if len(self.primes) % 1000 == 0:
            self.write()

    def isPrime(self, n):
        if n > self.lastPrime():
            self.addPrimeToNumber(n)
        return n in self.primes

    def isNextPrime(self, n):
        for number in self.primes:
            if n % number == 0:
                return False
            elif number > n**(1/2)+1:
                break
        return True

    def lastPrime(self):
        return self.primes[len(self.primes)-1]

    def firstAbove(self, n):
        i = 0
        while self.get(i) <= n:
            i += 1
        return i

    def range(self, n, m):
        output = []
        for k in range(n, m):
            output.append(self.primes[k])
        return output

    def read(self):
        try:
            if not os.path.isfile(self.file):
                raise FileNotFoundError
            file = open(self.file)
            self.primes = file.read()
            self.primes = self.primes.splitlines()

            for k in range(len(self.primes)):
                self.primes[k] = int(self.primes[k])

            if len(self.primes) == 0:
                self.primes = [2]

        except (ValueError, FileNotFoundError):
            self.primes = [2]
            self.write()

    def write(self):
        if not os.path.isdir("./data") and not os.path.isfile("./data"):
            os.mkdir("./data")
        with open(self.file, "w") as file:
            output = ""
            for n in self.primes:
                output += str(n) + "\n"
            file.write(output)
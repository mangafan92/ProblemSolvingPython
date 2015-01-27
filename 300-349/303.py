from modules.permutations import permute

length = 10
permutations = list()

def generatePermutations():
    global length
    global permutations
    length += 1
    characters = list(map(str, range(0, 3)))
    permutations = permute(characters, length, repeat=True)
    permutations = list(map(int, permutations))
    permutations.pop(0)

def smallestMultiple(n):
    for permutation in permutations:
        if permutation % n == 0:
            print(n, permutation)
            return permutation

    generatePermutations()
    return smallestMultiple(n)

def base3(n):
    n = str(n)
    for char in n:
        if char in map(str, range(3, 10)):
            return False
    return True

numbers = list(range(1, 10001))
numbers = list(map(lambda n: smallestMultiple(n) // n, numbers))

print(sum(numbers))
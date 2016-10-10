from modules.primeDecomposition import PrimeDecomposition


def solveProblem(number=600851475143):
    decomposition = PrimeDecomposition(number)
    filtered = filter(lambda key: decomposition[key] > 0, decomposition.keys())
    return max(filtered)


if __name__ == '__main__':
    print(solveProblem())
import re


def wordScore(word: str) -> int:
    letters = list([chr(l) for l in range(ord("A"), ord("A") + 26)])
    letterScore = lambda letter: letters.index(letter.upper()) + 1
    return sum(map(letterScore, word))


def contentToNames(content: str) -> list:
    name = re.compile(r'"([A-Za-z]+)"')
    return name.findall(content)


def solve() -> int:
    with open("./data/022_names.txt") as file:
        content = file.read()

    names = list(sorted(contentToNames(content)))
    return sum((k + 1) * wordScore(name) for k, name in enumerate(names))


if __name__ == '__main__':
    print(solve())

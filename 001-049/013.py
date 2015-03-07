with open("./data/013_numbers.txt", "r") as file:
    content = file.read()

def contentToList(content):
    content = content.splitlines()
    content = list(map(int, content))
    return content

def solveProblem(content=content):
    result = sum(contentToList(content))
    result = int(str(result)[:10])
    return result

if __name__ == '__main__':
    print(solveProblem())
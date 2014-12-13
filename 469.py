def proportion(n):
    output = 0
    results = startrecur(n)
    print(len(results))
    for result in results:
        print(result)
        output += (n-result[0]) * result[1]
    output /= n
    return output

def startrecur(seats):
    results = list()
    recur(seats-3, 1, 1, results)
    return results

def recur(available, occupied, probability, results):
    if available == 0:
        results.append([occupied, probability])
    else:
        if available > 2:
            recur(available-2, occupied+1, probability * 2/available, results)
            recur(available-3, occupied+1, probability * (1-2/available), results)
        elif available == 2:
            recur(available-2, occupied+1, probability, results)
        elif available == 1:
            recur(available-1, occupied+1, probability, results)

while True:
    try:
        n = int(input("Number:"))
        break
    except Exception:
        pass

output = proportion(n)
print(str(output)[:14])
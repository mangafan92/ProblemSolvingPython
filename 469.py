import time
import math

def proportion(n):
    output = 0
    check = 0
    results = startrecur(n)
    print(len(results))
    for result in results:
        print(result)
        output += (n-result[1]) * result[2]
        check += result[2]
    output /= n
    print(check)
    return output

def startrecur(seats):
    results = [[seats-3, 1, 1]] # available, occupied, probability
    while not finished(results):
        for k in range(int(round(math.log(seats, 10),0))):
            recur(results)
        combine(results)
    return results

def recur(results):
    if not round(results[0][2], 30) == 0:
        if results[0][0] == 0:
            results.append(results[0])
        else:
            if results[0][0] > 2:
                results.append([results[0][0]-2, results[0][1]+1, results[0][2] * 2/results[0][0]])
                results.append([results[0][0]-3, results[0][1]+1, results[0][2] * (1-2/results[0][0])])
            elif results[0][0] == 2:
                results.append([results[0][0]-2, results[0][1]+1, results[0][2]])
            elif results[0][0] == 1:
                results.append([results[0][0]-1, results[0][1]+1, results[0][2]])
    results.pop(0)

def finished(results):
    for result in results:
        if result[0] > 0:
            return False
    return True

def combine(results):
    number = 20
    for result1 in results:
        for result2 in results:
            if result1 != result2 and result1[0] == result2[0] and result1[1] == result2[1]:
                result1[2] += result2[2]
                results.remove(result2)

def main(n):
    n = 10**n
    print(n)

    output = proportion(n)
    print("Proportion:", round(output, 15))

if __name__ == '__main__':
    while True:
        try:
            n = int(input("Number:"))
            break
        except Exception:
            pass
    start = time.time()
    main(n)
    print("Time:", round(time.time()-start, 0))
def solutionEquation(D):
    y = 1
    x = 1.2
    while x != round(x, 0):
        x = (1+D*y**2)**(1/2)
        y += 1
    return (int(x), y)
        
xMax = 0

for k in range(62, 100):
    if int(k**(1/2)) != k**(1/2):
        xTemp= solutionEquation(k)[0]
#        print(xTemp, k)
        if xTemp > xMax:
            xMax = xTemp
print(xMax)
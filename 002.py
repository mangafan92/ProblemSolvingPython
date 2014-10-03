def fibonacci(n):
    U1 = 1
    U2 = 2
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:    
        for k in range(0, n-2):
            temp = U2
            U2 = U2 +U1
            U1 = temp
            
        return U2
    else:
        return 0;

s = 0
n = 1
fn = 0

while fn < 4000000:
    fn = fibonacci(n)   
    if fn < 4000000 and fn % 2 == 0:
        s += fn
    n+=1
    
print("La somme des termes pairs et inférieurs à 4 000 000 de la suite de Fibonacci est", s,".")
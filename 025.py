def fibonacci(n):
    U1 = 1
    U2 = 1
    
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
        
borne = int(input("Nombre:"))
n = 1

while len(str(fibonacci(n))) < borne:
    n += 1
    
print("Le premier nombre de la suite de Fibonacci a avoir plus de", borne, "digits est le", n, "-ième.")
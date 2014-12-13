borne = int(input("Nombre:"))
s = 0

for k in range (1,borne):
    if k % 3 == 0 or k % 5 == 0:
        s+=k
        
print("La sommme des multiples de 3 ou 5 inférieurs à", borne, "est", s, ".")
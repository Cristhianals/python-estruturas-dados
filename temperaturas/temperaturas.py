t = [-10,-8,0,1,2,5,-2,-4]
maximo = t[0]
minimo = t[0]
m = 0
im = 0
IM = 0
for i,v in enumerate(t):
    if v > maximo:
        maximo = v
        IM = i 
    if v < minimo:
        minimo = v
        im = i
    m += v
print(f"a maior temperatura foi de {maximo} localizada no indice {[IM]}")
print(f"a menor temperatura foi de {minimo} localizada no indice {[im]}")
print(f"e a temperatura media é de {m / len(t):5.2f}")

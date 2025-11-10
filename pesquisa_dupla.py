l = [15,7,27,39]
p = int(input("digite o valor a procurar:"))
v = int(input("digite outro valor a procurar:"))
achou = False
x = 0
one = []
temp = False
temv = False
while x < len(l):
    if l[x] == p:
        one.append(p)
        temp = True
        print(f"{p} achado na posicao {x}")
    elif l[x]== v:
        one.append(v)
        temv = True  
        print(f"{v} achado na posicao {x}")
    x += 1
if len(one) >= 1:
    print(f"o primeiro valor encontrado foi {one[0]}")
if len(one) >= 1 and temp == False:
    print(f"{p} nao foi encontrado")
if len(one) >= 1 and temv == False:
    print(f"{v} nao foi encontrado")
if not one:
    print("nenhum dos valores foi encontrado")

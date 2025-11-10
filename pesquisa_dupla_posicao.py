l = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
x = 0
temp = -1
temv = -1
while x < len(l):
    if l[x] == p:
        temp = x
    elif l[x] == v:
        temv = x
    x += 1
if temp != -1:
    print(f"{p} achado primeiro na posição {temp}")
else:
    print(f"{p} nao foi encontrado")
if temv != -1:
    print(f"{v} achado primeiro na posição {temv}")
else:
    print(f"{v} nao foi encontrado")

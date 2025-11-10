
l = [15,7,27,39]
p = int(input("digite o valor a procurar:"))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        print(f"{p} achado em posicao {x}")
        print("se quiser vericar todos os valores digite l")
        print(f"se quiser verificar o valor na posicao digite (l[posicao])")
        break
    x += 1
else:
    print(f"{p} nao encontrado")


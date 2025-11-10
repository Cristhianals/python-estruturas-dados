estoque = {"tomate": [1000, 2.30],
           "alface": [ 500, 0.45],
           "batata": [2001, 1.20],
           "feijao": [ 100, 1.50]}
print("digite a o produto,e a quantidade.\nquanto terminar de digitar todos os produtos")
print("digite 0\n")
venda = []
total = 0
while True:
    produto = input("digite o produto")
    quantidade = int(input("digite a quantidade"))
    print("\n")
    if produto == "0":
        break
    else:
        venda.append([produto, quantidade])
print("vendas\n")
for operacao in venda:
    produto, quantidade = operacao
    if operacao[0] in estoque:
        preço = estoque[produto][1]
        custo = preço * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
        estoque[produto][0] -= quantidade
        total += custo
    else:
        print(f"nao temos {produto} em estoque")
print(f" custo total: {total:21.2f}\n")
print("estoque:\n")
for chave,dados in estoque.items():
    print(f"{chave}\n{dados}")
    print("descricao: ", chave)
    print("quantidade: ", dados[0])
    print(f"preço: {dados[1]:6.2f}\n")

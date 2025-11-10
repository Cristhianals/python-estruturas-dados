ultimo = 10
ultimo2 = 10
fila = list(range(1,ultimo + 1))
fila2 = list(range(1,ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na primeira fila, \nE {len(fila2)} na segunda fila")
    print(f"digite F para adicionar um cliente ao fim da primeria fila,\nou G para adicionar no fim da segunda fila")
    print(f"A, para realizar o atendimento a primeria fila, \nou B, para o atendimento a segunda fila. S para sair.")
    operacao = list(input("quais operacoes (F, G, A, B ou S):" ))
    top = operacao.copy()
    while len(operacao) > 0:
        if operacao[0] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"cliente {atendido} da primeira fila atendido")
                feito = operacao.pop(0)
                print(f"a operacao {feito} foi realizada")
            else:
                print("primeira fila vazia! ninguem para atender.")
                feito = operacao.pop(0)
                print(f"a operacao {feito} foi realizada")
        elif operacao[0]== "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"cliente {atendido} na segunda fila atendido")
                feito = operacao.pop(0)
                print(f"a operacao {feito} foi realizada")
            else:
                print("segunda fila vazia! ninguem para atender.")
                feito = operacao.pop(0)
                print(f"a operacao {feito} foi realizada")
        elif operacao[0] == "F":
            ultimo += 1 
            fila.append(ultimo)
            feito = operacao.pop(0)
            print(f"a operacao {feito} foi realizada")
        elif operacao[0] == "G":
            ultimo2 += 1 
            fila2.append(ultimo2)
            feito = operacao.pop(0)
            print(f"a operacao {feito} foi realizada")
        elif operacao[0] == "S":
            feito = operacao.pop(0)
            print(f"a operacao {feito} foi realizada")
            break
        else:
            print("operacao invalida! digite apenas F, G, A, B ou S")
            feito = operacao.pop(0)
            print(f"a operacao {feito} foi realizada")
    print(f"as operacoes ({top}) foram realizadas")

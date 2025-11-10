ultimo = 10
ultimo2 = 10
fila = list(range(1,ultimo + 1))
fila2 = list(range(1,ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na primeira fila, \nE {len(fila2)} na segunda fila")
    print(f"digite F para adicionar um cliente ao fim da primeira fila,\nou G para adicionar no fim da segunda fila")
    print(f"A, para realizar o atendimento a primeria fila, \nou B, para o atendimento a segunda fila. S para sair.")
    operacao = list(input("quais operacoes (F, G, A, B ou S):" ))
    top = operacao.copy()
    for i, x in enumerate(operacao):
        if x == "F":
            ultimo += 1
            fila.append(ultimo)
            print(f"cliente {ultimo} adicionado na primeira fila")
            print(f"a operacao {x} realizada.")
        elif x == "G":
            ultimo2 += 1
            fila2.append(ultimo2)
            print(f"cliente {ultimo2} adicionado na segunda fila")
            print(f"a operacao {x} realizada.")
        elif x == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"cliente {atendido} atendido na primeira fila")
                print(f"a operacao {x} realizada.")
            else:
                print("primeira fila vazia! ninguem para atender")
        elif x == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"cliente {atendido} atendido na segunda fila")
                print(f"a operacao {x} realizada.")
            else:
                print("segunda fila vazia! ninguem para atender")
        elif x == "S":
            print(f"a operacao {x} sera realizada.")
            print("desligando")
            break
        else:
            print(f"a operacao {x} é invalida! figite apenas (F, G, A, B ou S")
        #if i == len(operacao)-1: desnecessario
            #print(f"as operacoes {top} foram realizadas")
print(f"as operacoes {top} foram realizadas")

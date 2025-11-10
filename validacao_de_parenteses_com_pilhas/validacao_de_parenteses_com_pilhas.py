expressao = []
while True:
    print("digite S para adiconar uma expressao")
    print("ou N para parar")
    operacao = input("oq deseja fazer?, S ou N: ")
    if operacao == "N":
        print("desligando")
        break
    elif operacao == "S":
        expressao = list(input("digite a expressao"))
        if "(" not in expressao and ")" not in expressao:
            print("a expressao nao possui nenhum parenteses")
            print(expressao)
            continue
        x = 1
        pilha =[]
        ide = []
        while x <= len(expressao):
            if expressao[x - 1] == "(":
                pilha.append(expressao[x - 1])
                ide.append(str(x) + "°")
            elif expressao[x - 1] == ")":
                if len(pilha) < 1:
                    print("Erro")
                    print(f"vc fechou um parenteses sem abrir um antes,\nno {x}° elemento da expressao{expressao}")
                    break
                else:
                    pilha.pop()
                    ide.pop()
            x += 1
        else:  
            if not pilha:
                print("OK, a expressao esta correta")
            else:
                print("Erro")
                print(f"o(s) parente(s) que foram abertos em {ide} lugar(s) nao foram fechados")
    else:
        print("operacao nao existe!. Digite apenas S ou N")
    
            

        

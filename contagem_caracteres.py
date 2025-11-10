dic = {
    }
print("digite uma palavra, ou 0 pra parar")
palavra = input()
for e in palavra:
    numero = 0
    for i in palavra:
        if i == e:
            numero += 1
    dic[e] = numero
print(dic)
v = dic.values()
c = dic.keys()
print(f"chaves: {c}\nvalores: {v} ")
print(dic.keys(),dic.values())
#mais simples
'''
dic = {
    }
print("digite uma palavra, ou 0 pra parar")
palavra = input()
for e in palavra:
    if letra in dic:
        dic[letra] = dic[letra] + 1
    
    else:
        dic[letra] = 1
print(dic)
'''

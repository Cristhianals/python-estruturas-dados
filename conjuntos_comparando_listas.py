print("digite os elementos da primeria lista")
l = list(input())
print("digite os elementos da segunda lista")
l2 = list(input())
l2c = set(l2)
repetidos = set()
lapenas = set()
for e in l:
    if e in l2:
        repetidos.add(e)
    else:
        lapenas.add(e)
l2apenas = l2c - repetidos
unicos = lapenas | l2apenas
print(f"os valores comuns nas duas listas sao {repetidos}")
print(f"os valores que so existem na primeria lista sao {lapenas}")
print(f"os valores que so existem na sugunda lista sao {l2apenas}")
print(f"os valores que nao se repetem, e so aparecem uma vez,em uma das lista sao {unicos}")
print(f"print a primeira lista sem os elementos repetidos na segunda sao {lapenas}")
#melhorado
print()
l = []
print("Digite os elementos da lista (digite 'fim' pra parar):")
while True:
    item = input()
    if item == 'fim':
        break
    l.append(item)
l2 = []
print("Digite os elementos da segunda lista (digite 'fim' pra parar):")
while True:
    item = input()
    if item == 'fim':
        break
    l2.append(item)
c = set(l)
c2 = set(l2)
unicos2 = c ^ c2
repetidos2 = c & c2  
capenas = c - repetidos2
c2apenas = c2 - repetidos2
print(f"os valores comuns nas duas listas sao {repetidos2}")
print(f"os valores que so existem na primeria lista sao {capenas}")
print(f"os valores que so existem na sugunda lista sao {c2apenas}")
print(f"os valores que nao se repetem, e so aparecem uma vez,em uma das lista sao {unicos2}")
print(f"print a primeira lista sem os elementos repetidos na segunda sao {capenas}")
#tambem posso fazer isso aqui pra saber os elmentos repetidos dos conjuntos
#(A | B) - ((A - B) | (B - A)) == A & B. iguais = (A | B) - ((A - B) | (B - A))

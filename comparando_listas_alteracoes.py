l = []
print("Digite os elementos da lista (digite 'fim' pra parar):")
while True:
    item = input()
    if item == 'fim':
        break
    l.append(item)
l2 = []
print("Digite os elementos da nova lista (digite 'fim' pra parar):")
while True:
    item = input()
    if item == 'fim':
        break
    l2.append(item)
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
if len(repetidos) > 0:
    print(f"os valores que se manteram{repetidos}")
else:
    print("nhenum valor se repetiu na nova lista")
if len(l2apenas) > 0:
    print(f"os novos valores sao {l2apenas}")
else:
    print("nao ha novos elementos na nova lista")
if len(lapenas) > 0:
    print(f"os elemetos que foram removidos {lapenas}")
else:
    print("nehnum elemento foi removido")


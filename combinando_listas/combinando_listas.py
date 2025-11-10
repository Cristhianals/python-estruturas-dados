l = []
while True:
    n = int(input("digite os valores da primeira lista(0 para sai)"))
    if n == 0:
        x = 1
        print("os elementos da primeria lista sao")
        while x <= len(l):
            print(l[x - 1])
            x += 1
        break
    l.append(n)

l2 = []
while True:
    n2 = int(input("digite os valores da segunda lista(0 para sai)"))
    if n2 == 0:
        x = 1
        print("os elementos da segunda lista sao")
        while x <= len(l2):
            print(l2[x - 1])
            x += 1
        break
    l2.append(n2)
print("")
l3 = [] 
l3.extend(l)
l3.extend(l2)
print(f"a juncao das duas lista é {l3}")

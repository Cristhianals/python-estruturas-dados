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
x = 1
a = 1
l3 = [] 
l3.append(l[0])
while x <= len(l):
    if a > len(l3):
        x += 1
        a = 1
    if l[x - 1] != l3[a - 1]:
        while True:
            if a == len(l3):
                l3.append(l[x - 1])
                a += 1
                break
            else:
                a += 1
                break
    elif l[x - 1] == l3[a - 1]:
        x += 1
        a = 1
x = 1
a = 1
while x <= len(l2):
    if a > len(l3):
        x += 1
        a = 1
    if l2[x - 1] != l3[a - 1]:
        while True:
            if a == len(l3):
                l3.append(l2[x - 1])
                a += 1
                break
            else:
                a += 1
                break
    elif l2[x - 1] == l3[a - 1]:
        x += 1
        a = 1
print(f"a juncao das duas lista é {l3}")


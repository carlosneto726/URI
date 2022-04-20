casos_de_testes = int(input())
for c in range(0, casos_de_testes):
    tomadas = 0
    l = input().split(" ")
    for i in range(1, int(l[0])+1):
        if i == len(l) - 1:
            tomadas += int(l[i])
        else:
            tomadas += (int(l[i]) -1)
    print(tomadas)
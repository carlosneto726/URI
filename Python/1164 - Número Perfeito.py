testes = int(input())
for x in range(0, testes):
    N = int(input())
    c = p = 0
    while c != N - 1:
        c += 1
        if N % c == 0:
            p += c
    if p == N:
        print(f"{N} eh perfeito")
    else:
        print(f"{N} nao eh perfeito")
    
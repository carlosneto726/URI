# 0.164
testes = int(input())
for c in range(0, testes):
    r1, r2 = input().split(" ")
    print(int(r1) + int(r2))


# 0.057
testes = int(input())
for c in range(0, testes):
    r1, r2 = input().split(" ")
    d1 = int(r1) * 2
    d2 = int(r2) * 2
    dt = d1 + d2
    rt = dt / 2
    print(int(rt))
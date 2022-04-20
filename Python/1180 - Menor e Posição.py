X = []
N = int(input())
Xv = input().split()

for c in range(0, N):
    X.append(int(Xv[c]))

menor = X[0]
posicao = 0

for pos in range(0, N):
    if X[pos] < menor:
        menor = X[pos]
        posicao = pos 

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")

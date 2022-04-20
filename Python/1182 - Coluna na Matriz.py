matrizes = [[], [], [], [], [], [], [], [], [], [], [], []]
coluna = int(input())
tipo = input().upper()

for matriz in range(0, 12):
    for c in range(0, 12):
        m = float(input())
        matrizes[matriz].append(m)

media = 0
soma = 0

if tipo == "S":
    for s in range(0, 12):
        soma += matrizes[s][coluna]
    print(f"{soma:.1f}")

elif tipo == "M":
    for m in range(0, 12):
        media += matrizes[m][coluna]
    mediaf = media / 12
    print(f"{mediaf:.1f}")

matrizes = [[], [], [], [], [], [], [], [], [], [], [], []]
tipo = input().upper()

for matriz in range(0, 12):
    for c in range(0, 12):
        m = float(input())
        matrizes[matriz].append(m)

media = 0
soma = 0
col = 0

if tipo == "S":

    for linha in range(0, 12):
        for coluna in range(0, col):
            soma += matrizes[linha][coluna]
        col = col + 1

    print(f"{soma:.1f}")

elif tipo == "M":

    for linha in range(0, 12):
        for coluna in range(0, col):
            media += matrizes[linha][coluna]
        col = col + 1

    mediaf = media / 66
    print(f"{mediaf:.1f}")

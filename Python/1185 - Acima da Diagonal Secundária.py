matrizes = [[], [], [], [], [], [], [], [], [], [], [], []]
tipo = input().upper()

for matriz in range(0, 12):
    for c in range(0, 12):
        m = float(input())
        matrizes[matriz].append(m)

media = 0
soma = 0
col = 12

if tipo == "S":

    for linha in range(0, 12):
        col = col - 1
        for coluna in range(0, col):
            soma += matrizes[linha][coluna]

    print(f"{soma:.1f}")

elif tipo == "M":

    for linha in range(0, 12):
        col = col - 1
        for coluna in range(0, col):
            media += matrizes[linha][coluna]

    mediaf = media / 66
    print(f"{mediaf:.1f}")

matrizes = [[], [], [], [], [], [], [], [], [], [], [], []]
tipo = input().upper()

for matriz in range(0, 12):
    for c in range(0, 12):
        m = float(input())
        matrizes[matriz].append(m)

operacao = 0
qtd = 0

col = 12
n = -1
aux = False

for linha in range(1, 11):

    if aux:
        n = 1

    elif col == 7:
        col -= 1
        n = 1
        aux = True
        
    col += n

    for coluna in range(col, 12):
        operacao += matrizes[linha][coluna]
        qtd += 1


if tipo == "S":
    print(f"{operacao:.1f}")
else:
    print(f"{(operacao / qtd):.1f}")

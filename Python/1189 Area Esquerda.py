matrizes = [[], [], [], [], [], [], [], [], [], [], [], []]
tipo = input().upper()

for matriz in range(0, 12):
    for c in range(0, 12):
        m = float(input())
        matrizes[matriz].append(m)

operacao = 0
qtd = 0

col = 0
n = 1
aux = False

for linha in range(1, 11):

    if aux:
        n = -1

    elif col == 5:
        n = -1
        col += 1
        aux = True
        
    col += n

    for coluna in range(0, col):
        operacao += matrizes[linha][coluna]
        qtd += 1



if tipo == "S":
    print(f"{operacao:.1f}")
else:
    print(f"{(operacao / qtd):.1f}")

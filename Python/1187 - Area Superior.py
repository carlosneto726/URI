matrizes = [[], [], [], [], [], [], [], [], [], [], [], []]
tipo = input().upper()

for matriz in range(0, 12):
    for c in range(0, 12):
        m = float(input())
        matrizes[matriz].append(m)

operacao = 0
qtd = 0
col_incio = 0
col_fim = 12

for linha in range(0, 5):
    col_incio = col_incio + 1
    col_fim = col_fim - 1
    for coluna in range(col_incio, col_fim):
        operacao += matrizes[linha][coluna]
        qtd += 1

if tipo == "S":
    print(f"{operacao:.1f}")
else:
    print(f"{(operacao / qtd):.1f}")

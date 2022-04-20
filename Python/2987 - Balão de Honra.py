# Tempo = 0.054s
# Tamanho = 39 Bytes

letra = input()
print(ord(letra) - 64)


# Tempo = 0.177s
# Tempo = 147 Bytes
letra = input()
alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for c in alfabeto:
    if c == letra:
        print(alfabeto.index(c) + 1)
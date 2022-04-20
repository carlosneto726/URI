x = 0
for c in range(1, 101):
    n = int(input())
    x = x + n
    if n > x - n:
        maior = n
        pos = c
print(maior)
print(pos)
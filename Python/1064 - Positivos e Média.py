s = 0
i = 0
for c in range(0, 6):
    n = float(input())
    if n > 0:
        i += 1
        s = s + n
print(f"{i} valores positivos")
print(f"{s/i:.1f}")
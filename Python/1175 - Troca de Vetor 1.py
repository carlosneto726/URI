N = []
for c in range(0, 20):
    v = int(input())
    N.append(v)
x = 0
for i in range(19, -1, -1):
    print(f"N[{x}] = {N[i]}")
    x += 1
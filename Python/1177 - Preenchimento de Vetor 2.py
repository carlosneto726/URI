i = 0
N = []
T = int(input())
for c in range(0, 1000):
    N.append(i)
    i += 1
    if i >= T:
        i = 0
    print(f"N[{c}] = {N[c]}")
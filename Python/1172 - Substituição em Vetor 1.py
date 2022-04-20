X = []
for c in range(0, 10):
    N = int(input())
    if N <= 0:
        X.append(1)
    else:
        X.append(N)
    print(f"X[{c}] = {X[c]}")
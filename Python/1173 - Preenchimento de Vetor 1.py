N = int(input())
X = []
for c in range(0, 10):
    X.append(N)
    N += N
    print(f"N[{c}] = {X[c]}")
X = float(input())
N = []
for c in range(0, 100):
    N.append(X)
    X = X / 2
    print(f"N[{c}] = {(N[c]):.4f}")

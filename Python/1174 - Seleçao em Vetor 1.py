A = []
for c in range(0, 100):
    N = float(input())
    A.append(N)
    if N <= 10:
        print(f"A[{c}] = {A[c]}")
N = int(input())
for c in range(1, N+1):
    v = input().split()
    if float(v[1]) == 0:
        print("divisao impossivel")
    else:
        print(f"{(float(v[0]) / float(v[1])):.1f}")
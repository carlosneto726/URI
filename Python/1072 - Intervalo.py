i = o = 0
N = int(input())
for c in range(1, N+1):
    X = int(input())
    if 10 <= X <= 20:
        i += 1
    else:
        o += 1
print(f"{i} in")
print(f"{o} out")
